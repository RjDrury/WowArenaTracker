
from app import app, db, bcrypt
from models import User, Friend
from helper import wow_arena_call, wow_parser, history
from flask import render_template, request, redirect, jsonify, session


@app.route('/')
def hello_world():
    if not session.get('logged_in'):
        return redirect('/login')

    username = session.get('username')

    friends_list = Friend.query.filter_by(account_name=username).all()
    history = []
    for friend in friends_list:
        ratings = wow_arena_call(friend.character_name, friend.realm)
        friend.twos_rating = ratings["twos"]
        friend.threes_rating = ratings["threes"]
        friend.rbgs_rating = ratings["rbg"]
        history.append({
            'character_name': friend.character_name,
            'realm': friend.realm,
            'twos_rating': friend.twos_rating,
            'threes_rating': friend.threes_rating,
            'rbgs_rating': friend.rbgs_rating
        })

    return render_template("index.html", data=history, user=username, logged_in=True)


@app.route('/addfriend', methods=['POST'])
def wow_post():
    username = session.get('username')
    name = request.form.get('name')
    realm = request.form.get('realm')

    if name and realm:  # make sure name and realm aren't empty
        ratings = wow_arena_call(name, realm)
        if ratings:
            new_friend = Friend(username, name.capitalize(), realm.capitalize(
            ), ratings['twos'], ratings['threes'], ratings['rbg'])
            db.session.add(new_friend)
            db.session.commit()

    return redirect("/")


@app.route('/login')
def login_page():
    return render_template("login.html")


@app.route('/login', methods=['POST'])
def verify_login():

    username = request.form.get('username')
    testPassword = request.form.get('password')
    user = User.query.filter_by(username=username).first()

    if user is not None and bcrypt.check_password_hash(user.password, testPassword):
        session['logged_in'] = True
        session['username'] = username
        return redirect("/")
    else:
        return render_template("login.html", logged_in=False)


@app.route('/signup', methods=['POST'])
def sign_up():

    email = request.form.get('email_register')
    username = request.form.get('username_register')
    password = request.form.get('password_register')

    if email and username and password:  # if its not empty lets say its valid
        password = bcrypt.generate_password_hash(password).decode('utf-8')
        new_user = User(username, email, password)
        # see if the name  or email is in use
        if not User.query.filter_by(username=username).first() or not User.query.filter_by(email=email).first():
            db.session.add(new_user)
            db.session.commit()
    return redirect('/')


@app.route('/history')
def history_api():
    return jsonify({'data': history})


@app.route('/logout', methods=['POST'])
def logout():
    session['logged_in'] = False
    return redirect("/login")

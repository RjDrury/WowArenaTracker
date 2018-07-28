from app import db

class User(db.Model):
    """ User accounts """
    
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(120), nullable=False)
    
    def __repr__(self):
        return '<User %r>' % self.username

    def __init__(self, username, email, password):
        self.username = username
        self.email = email
        self.password = password


class Friend(db.Model):
    """ Tracks friends accounts """

    id = db.Column(db.Integer, primary_key=True)
    account_name = db.Column(db.String(80), nullable=False)
    character_name = db.Column(db.String(120), nullable=False)
    realm = db.Column(db.String(120), nullable=False)
    twos_rating= db.Column(db.String(120), nullable=False)
    threes_rating = db.Column(db.String(120), nullable=False)
    rbgs_rating = db.Column(db.String(120), nullable=False)
    
    def __init__(self, account_name,character_name, realm, twos_rating, threes_rating,rbgs_rating):
        self.account_name = account_name
        self.character_name = character_name
        self.realm = realm
        self.twos_rating = twos_rating
        self.threes_rating = threes_rating
        self.rbgs_rating = rbgs_rating
    



        

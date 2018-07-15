import requests
from flask import Flask, render_template, request, redirect, jsonify

app = Flask(__name__)

history = []

def wow_arena_call(name, server):
    # try exception - done
        try:
            response = requests.get(f'https://us.api.battle.net/wow/character/{server}/{name}?fields=pvp&locale=en_US&apikey=jfccb66vhqt3eggxg4y5srt5qbcf5mw2')
            return wow_parser(response.json())
        except requests.exceptions.RequestException as e:  
            print (e)
           
def check__if_duplicate(name,server): # return true if its not a duplicate
    for i in history:
        if name.capitalize() == i['name']: #capatilize first letter of name because of the way it is stored
            return False
    return True

def wow_parser(data):
    # check if the data is valid - done
    #print(data , "hi")
    if 'pvp' in data:
        brackets = data['pvp']['brackets']
        twos = brackets['ARENA_BRACKET_2v2']
        threes = brackets['ARENA_BRACKET_3v3']
        rbg = brackets['ARENA_BRACKET_RBG']
        return {
            'twos': twos['rating'],
            'threes':threes['rating'],
            'rbg':rbg['rating'],
            'name':data['name']
        }
    return {
            'twos': 'N/A',
            'threes':'N/A',
            'rbg':'N/A',
            'name':'N/A'
    }
   
@app.route('/')
def hello_world():
    return render_template("index.html", data = history)

@app.route('/update', methods=['POST'])
def wow_post():    
    name = request.form.get('name')
    realm = request.form.get('realm')
    #check if duplicate - done
    if check__if_duplicate(name,realm) and name and realm: #make sure name and realm aren't empty
            ratings = wow_arena_call(name,realm)
            history.append(ratings)
    return redirect("/")

@app.route('/history')
def history_api():
    return jsonify({'data': history})

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)


"""
todo
- read comments above
- GET = login page /login 
- POST = form with username and password -> print to console username and password
- bug free
"""
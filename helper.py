import requests

history = []

def wow_arena_call(name, server):
    """
    Calls WoW API

    :params name: String, WoW character name
    :params server: String, Server name
    :return: JSON response
    """

    try:
        response = requests.get(f'https://us.api.battle.net/wow/character/{server}/{name}?fields=pvp&locale=en_US&apikey=jfccb66vhqt3eggxg4y5srt5qbcf5mw2')
        return wow_parser(response.json())
    except requests.exceptions.RequestException as e:  
        return {}

def wow_parser(data):
    """ Parses a JSON """

    if 'status' not in data:
        brackets = data['pvp']['brackets']
        twos = brackets['ARENA_BRACKET_2v2']
        threes = brackets['ARENA_BRACKET_3v3']
        rbg = brackets['ARENA_BRACKET_RBG']
      
        return {
            'twos': twos['rating'],
            'threes':threes['rating'],
            'rbg':rbg['rating'],
            'name':data['name'].capitalize(),
            'realm':data['realm'].capitalize()
        }
    return {}
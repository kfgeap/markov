import json
from requests_oauthlib import OAuth1Session
from GenerateText import GenerateText

def markovbot():
    keysfile = open('keys.json')
    keys = json.load(keysfile)
    oath = create_oath_session(keys)

    generator = GenerateText(1)

    tweetmarkovstring(oath, generator)

def create_oath_session(oath_key_dict):
    oath = OAuth1Session(
    oath_key_dict['dukxusBDK3V2jFvqeU1hy6Grk'],
    oath_key_dict['iq5VK8g80KNk8gscXl702CfEu3ELuLTjba0sxXbwBsRkM8VTGX'],
    oath_key_dict['2351277440-6A7Me8lE80twEaClraU0QKeMPTKtMGRUxg8jlea'],
    oath_key_dict['uNktGwx2U3FxiidhH1orHOOFcocIxSd2VQ5iRb1X7AUTp']
    )
    return oath

def tweetmarkovstring(oath, generator):
    url = 'https://api.twitter.com/1.1/statuses/update.json'
    markovstring = generator.generate()
    params = {'status': markovstring+'[bot]'}
    req = oath.post(url, params)

    if req.status_code == 200:
        print('tweet succeed!')
    else:
        print('tweet failed')


if __name__ == '__main__':
    markovbot()
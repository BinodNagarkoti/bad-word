
import requests, json

url = ' https://neutrinoapi.com/bad-word-filter?user-id=PrinceOfDevil&api-key=dkBIk1GQnUDqeZast6Q5x3gUQnlJG4ALw8dNLzEdIs95RK46&censor-character=*&content=dick fuck suck pussy cum'
# params = {
#   'user-id': 'PrinceOfDevil',
#   'api-key': 'dkBIk1GQnUDqeZast6Q5x3gUQnlJG4ALw8dNLzEdIs95RK46',
#   'content': 'dick sick fuck suck pussy',
#   'censor-character': '*'
# }
response = requests.get(url)
# req = urllib2.Request(url, urllib.urlencode(params))
# response = urllib2.urlopen(req)
# result = json.loads(response.read())
if response.status_code == 200:
        result=json.loads(response.content.decode('utf-8'))
        print (result['censored-content'])
        print (result['is-bad'])
        print (result['bad-words-list'])
        print (result['bad-words-total'])

# print (result['censored-content'])
# print (result['is-bad'])
# print (result['bad-words-list'])
# print (result['bad-words-total'])
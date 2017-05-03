import requests, json

url = '''http://finance.yahoo.com/webservice/v1/symbols/allcurrencies/quote?format=json'''
data = json.loads(requests.get(url).text)


for i in data['list']['resources']:
    print(i['resource']['fields']['symbol'],
          i['resource']['fields']['price'],
          i['resource']['fields']['name'])
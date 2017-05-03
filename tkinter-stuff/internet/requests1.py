import requests, json

url = '''http://finance.yahoo.com/webservice/v1/symbols/allcurrencies/quote?format=json'''
response = requests.get(url).text
#data = json.loads(requests.get(url).text)
print(response)
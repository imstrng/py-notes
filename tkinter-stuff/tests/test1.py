import requests

url = '''https://www.google.com/finance/getprices?i=60&p=1d&f=d,o,v&x=AMS&q=AGN'''
data = requests.get(url).text
print(data)
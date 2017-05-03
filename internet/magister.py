import json, requests, re



prefix = '000'
username = 'username'
password = 'password'


headers = { 'Content-Type': 'application/json' }
payload = { 'Gebruikersnaam': username, 'Wachtwoord': password, 'IngelogdBlijven': 'false'}
session = requests.Session()


with session as s:
    s.delete('https://{0}.magister.net/api/sessies/huidige'.format(prefix))
    res = s.post('https://{0}.magister.net/api/sessies'.format(prefix), headers = headers, data = json.dumps(payload))
    if res.status_code == 403 and res.json()["Status"] == 1: raise Exception("Wrong username and/or password.")

    data = json.loads(s.get('https://{0}.magister.net/api/account'.format(prefix)).text)

    id = data["Persoon"]["Id"]
    person_url = "https://{0}.magister.net/api/personen/{1}".format(prefix, id)
    pupil_url = "https://{0}.magister.net/api/leerlingen/{1}".format(prefix, id)

    afspraken = json.loads(s.get('{0}/afspraken?van=2017-04-01&tot=2017-04-14'.format(person_url)).text)
from flask import Flask
import os
import datetime
import json

mon = {}
info = {}

info['starttime'] = datetime.datetime.today()



def readSettings():
    if os.path.isfile('settings.json'):
        f = open("settings.json", "r")
        mon = json.load(f)
        f.close()
    return mon


def writeSettings(mon):
    f = open("settings.json", "w")
    f.write(json.dumps(mon, indent=4, sort_keys=True))
    f.close()




app = Flask(__name__)

@app.route('/')
def index():
    return json.dumps(mon, sort_keys=True, indent=4, separators=(',', ': '))

# ----------- MORE ROUTING --------------

@app.route('/info')
def hello():
    return json.dumps(info, sort_keys=True, indent=4, separators=(',', ': '))

@app.route('/save')
def save():
    writeSettings(mon)
    return '{"status":"OK"}'


@app.route('/<name>/<k>', defaults={'v': None})
@app.route('/<name>/<k>/<v>')
def instance(name,k,v):
    now = str(datetime.datetime.today())

    if name not in mon:
        mon.update({name : {'enable':'0', 'start':'', 'end':'', 'snooze': '', 'interval':'', 'last':'', 'status':'', 'descr':'','timeout':''}})

    if k in ['ERROR','WARNING','OK']:
        mon[name].update({'last': now, 'status': k, 'descr': v})
        return '{"status":"OK"}'
    elif k in ['enable','start','end','snooze','interval','timeout']:
        mon[name].update({k: v})
        return '{"status":"OK"}'
    else:
        return '{"status":"ERROR"}'





# ----------- RUN APP --------------------

mon = readSettings()
if __name__ == '__main__':
    app.run(host='0.0.0.0', debug= True)
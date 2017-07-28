#!/usr/bin/python3

import asyncio
import os
import time
import json
import copy
mon = {}

store_path='store'
info_seconds = 120

header = """HTTP/1.0 200 OK
Content-Type: application/json

"""

def loadSettings():
    global mon
    if os.path.isfile('sparkpug.json'):
        f = open("sparkpug.json", "r")
        mon = json.load(f)
        f.close()
        print('Settings loaded.')
    return mon

def saveSettings(mon):
    try:
        f = open("sparkpug.json", "w")
        f.write(json.dumps(mon, indent=4, sort_keys=True))
        f.close()
        print('Settings saved.')
    except:
        pass

def store(topic, now, key, val):
    now = str(time.strftime('%Y-%m-%d', time.localtime(int(now))))
    with open(store_path+'/'+now[:10]+'_'+topic+'.log', 'a') as f:
            f.write(now+' '+key+' '+val+'\n')

def itemInit(topic):
    if topic not in mon:
        mon.update({topic : {'enable':'0', 'start':'', 'end':'', 'snooze': '', 'interval':'', 'checkedin':'', 'status':'', 'descr':'','timeout':'', 'reporter':'', 'url1':'', 'url2':''}})

def itemUpdateStatus(topic, now, key, val, reporter):
    itemInit(topic)
    mon[topic].update({'checkedin': now, 'status': key, 'desc': val, 'reporter': reporter})
    store(topic, now, key, val)

def itemUpdateParams(topic, now, key, val):
    itemInit(topic)
    mon[topic].update({key: val})
    store(topic, now, key, val)

def getAlerts():
    out  = {}
    for item in mon:
        if mon[item]['status'] != 'OK' \
                or (mon[item]['status'] == 'INFO' and int(time.time())-int(mon[item]['checkedin']) <  info_seconds):

            out[item] = copy.deepcopy(mon[item])
            out[item]['checkedin'] = str(time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(int(out[item]['checkedin']))))

    out = header + json.dumps(out, indent=4, sort_keys=True) + '\n'
    return out

class Server(asyncio.Protocol):

    def connection_made(self, transport):
        self.transport = transport
        self.reporter = transport.get_extra_info('peername')[0]

    def data_received(self, data):
        global mon
        self.now = str(int(time.time()))
        try:
            self.msg = data.decode().strip('\r\n').split(' ', 2)
            self.empty = [''] * (3 - len(self.msg) )
            self.topic, self.key, self.val = self.msg + self.empty
        except:
            self.transport.close()
            return

        if self.key in ['INFO','ERROR','WARN','OK']:
            itemUpdateStatus(self.topic, self.now, self.key, self.val, self.reporter)

        elif self.key in ['enable','start','end','snooze','interval','timeout','descr','url1','url2']:
            itemUpdateParams(self.topic, self.now, self.key, self.val)

        elif self.topic in ['GET']:
            if self.key == '/':
                self.out = getAlerts()
                self.transport.write(self.out.encode())
            else:
                try:
                    self.topic, self.key, self.val  = self.key[1:].split('/', 2)
                except:
                    self.out = header + json.dumps({'status': 'error'}, indent=4, sort_keys=True) + '\n'
                    self.transport.write(self.out.encode())
                    self.transport.close()
                    return

                if self.topic in mon:
                    if self.key in ['enable','start','end','snooze','interval','timeout','descr','url1','url2']:
                        itemUpdateParams(self.topic, self.now, self.key, self.val)
                        self.out = header + json.dumps({'status': 'ok'}, indent=4, sort_keys=True) + '\n'
                        self.transport.write(self.out.encode())

                    elif self.key in ['INFO','ERROR','WARN','OK']:
                        itemUpdateStatus(self.topic, self.now, self.key, self.val, self.reporter)
                        self.out = header + json.dumps({'status': 'ok'}, indent=4, sort_keys=True) + '\n'
                        self.transport.write(self.out.encode())
                    else:
                        self.out = header + json.dumps({'status': 'error'}, indent=4, sort_keys=True) + '\n'
                        self.transport.write(self.out.encode())
                else:
                    self.out = header + json.dumps({'status': 'error'}, indent=4, sort_keys=True) + '\n'
                    self.transport.write(self.out.encode())
        self.transport.close()


if __name__ == '__main__':
    mon = loadSettings()
    loop = asyncio.get_event_loop()
    coro = loop.create_server(Server, '0.0.0.0', 5000)
    server = loop.run_until_complete(coro)
    print('Listing on {}'.format(server.sockets[0].getsockname()))
    try:
        loop.run_forever()
    except KeyboardInterrupt:
        saveSettings(mon)
    server.close()
    loop.run_until_complete(server.wait_closed())
    loop.close()

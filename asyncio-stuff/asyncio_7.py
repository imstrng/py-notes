#!/usr/bin/python3

import asyncio
import os
import datetime
import json
mon = {}

store_path='store'

jsonheader = """HTTP/1.0 200 OK
Content-Type: text/html
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
    with open(store_path+'/'+now[:10]+'_'+topic+'.log', 'a') as f:
            f.write(now+' '+key+' '+val+'\n')

class Server(asyncio.Protocol):

    def connection_made(self, transport):
        self.transport = transport
        self.reporter = transport.get_extra_info('peername')[0]

    def data_received(self, data):
        global mon
        self.now = str(datetime.datetime.today())
        try:
            self.msg = data.decode().strip('\r\n')
            self.topic, self.key, self.val = self.msg.split(' ', 2)
        except:
            self.transport.close()
            return

        if self.key in ['ERROR','WARN','OK']:
            if self.topic not in mon:
                mon.update({self.topic : {'enable':'0', 'start':'', 'end':'', 'snooze': '', 'interval':'', 'last':'', 'status':'', 'descr':'','timeout':'', 'reporter':''}})
            mon[self.topic].update({'last': self.now, 'status': self.key, 'desc': self.val, 'reporter': self.reporter})
            store(self.topic, self.now, self.key, self.val)

        elif self.key in ['enable','start','end','snooze','interval','timeout']:
            print(self.topic,self.key,':',self.val)
            if self.topic not in mon:
                mon.update({self.topic : {'enable':'0', 'start':'', 'end':'', 'snooze': '', 'interval':'', 'last':'', 'status':'', 'descr':'','timeout':'', 'reporter':''}})
            mon[self.topic].update({self.key: self.val})
            store(self.topic, self.now, self.key, self.val)

        elif self.topic == 'admin':
            if self.val == '1':
                if self.key == 'save':
                    saveSettings(mon)
                if self.key == 'load':
                    mon = loadSettings()
                if self.key == 'shutdown':
                    saveSettings(mon)
                    print('Shutting down')
                    exit()

        elif self.topic == 'GET':
            print(self.val)

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

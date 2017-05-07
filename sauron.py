#!/usr/bin/python3

import asyncio
import os
import datetime
import json

mon = {}
info = {}

info['starttime'] = str(datetime.datetime.today())
info['requests'] = 0

jsonheader = """HTTP/1.0 200 OK
Content-Type: text/html

"""

def readSettings():
    print('reading settings.')
    global mon
    if os.path.isfile('sauron.json'):
        f = open("sauron.json", "r")
        mon = json.load(f)
        f.close()
    return mon


def writeSettings(mon):
    f = open("sauron.json", "w")
    f.write(json.dumps(mon, indent=4, sort_keys=True))
    f.close()



class Server(asyncio.Protocol):
    def connection_made(self, transport):
        #peername = transport.get_extra_info('peername')
        self.transport = transport
        #print(peername)

    def data_received(self, data):

        info['requests'] += 1

        try:
            msg = data.decode().strip('\r\n')
            m = msg.split(' ', 2)
        except:
            m = 'fail'


        if len(m) == 3:

            if m[0] == 'GET':

                if m[1] == '/root':
                    out = json.dumps(mon, indent=4, sort_keys=True)+'\n'
                    out = jsonheader + out

                else:
                    info['instances'] = len(mon)
                    out = json.dumps(info, indent=4, sort_keys=True)+'\n'
                    out = jsonheader + out + m[1]

                self.transport.write(out.encode())
                self.transport.close()










            elif m[0] not in mon:
                mon.update({m[0] : {'enable':'0', 'start':'', 'end':'', 'snooze': '', 'interval':'', 'last':'', 'status':'', 'descr':'','timeout':''}})


            if m[1] in ['enable','start','end','snooze','interval','timeout']:
                mon[m[0]].update({m[1]: m[2]})
                out = json.dumps(mon[m[0]], indent=4, sort_keys=True)+'\n'
                self.transport.write(out.encode())


            elif m[1] in ['ERROR','WARNING','OK']:
                now = str(datetime.datetime.today())
                mon[m[0]].update({'last': now, 'status': m[1], 'desc': m[2]})
                self.transport.close()


        elif len(m) == 1:
            if m[0] == 'info':
                info['instances'] = len(mon)
                out = json.dumps(info, indent=4, sort_keys=True)+'\n'
                self.transport.write(out.encode())


            elif m[0] in mon:
                out = json.dumps(mon[m[0]], indent=4, sort_keys=True)+'\n'
                self.transport.write(out.encode())

            elif m[0] == 'all':
                out = json.dumps(mon, indent=4, sort_keys=True)+'\n'
                self.transport.write(out.encode())

            elif m[0] == 'exit':
                self.transport.close()


            elif m[0] == 'save':
                writeSettings(mon)
                out = 'OK\n'
                self.transport.write(out.encode())

            else:
                out = 'ERROR\n'
                self.transport.write(out.encode())

        else:
            self.transport.close()




mon = readSettings()

loop = asyncio.get_event_loop()
coro = loop.create_server(Server, '0.0.0.0', 8080)
server = loop.run_until_complete(coro)

print('Listing on {}'.format(server.sockets[0].getsockname()))

try:
    loop.run_forever()
except KeyboardInterrupt:
    pass


server.close()
loop.run_until_complete(server.wait_closed())
loop.close()
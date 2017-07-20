#!/usr/bin/python3

import asyncio
import os
import datetime
import json
mon = {}

store_path='store'

header = """HTTP/1.0 200 OK
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


def itemInit(topic):
    if topic not in mon:
        mon.update({topic : {'enable':'0', 'start':'', 'end':'', 'snooze': '', 'interval':'', 'last':'', 'status':'', 'descr':'','timeout':'', 'reporter':''}})


def itemUpdateStatus(topic, now, key, val, reporter):
    itemInit(topic)
    mon[topic].update({'last': now, 'status': key, 'desc': val, 'reporter': reporter})
    store(topic, now, key, val)


def itemUpdateParams(topic, now, key, val):
    itemInit(topic)
    mon[topic].update({key: val})
    store(topic, now, key, val)


def getAlerts():
    out = mon
    return out



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
            itemUpdateStatus(self.topic, self.now, self.key, self.val, self.reporter)

        elif self.key in ['enable','start','end','snooze','interval','timeout']:
            itemUpdateParams(self.topic, self.now, self.key, self.val)

        elif self.topic in ['GET']:
            if self.key == '/':
                self.out = getAlerts()
                self.out = header + json.dumps(mon, indent=4, sort_keys=True) + '\n'
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
                    if self.key in ['enable','start','end','snooze','interval','timeout']:
                        itemUpdateParams(self.topic, self.now, self.key, self.val)
                        self.out = header + json.dumps({'status': 'ok'}, indent=4, sort_keys=True) + '\n'
                        self.transport.write(self.out.encode())
                    
                    elif self.key in ['enable','start','end','snooze','interval','timeout']:
                        itemUpdateParams(self.topic, self.now, self.key, self.val)
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


'''
<html>
<body>
<table border=1>
<?php
$json = file_get_contents('http://amam1w211:5000');
$json = json_decode($json, true);
foreach ($json as $k => $v){
   echo '<tr>';
   echo '<td>'.$k.'</td>';
   echo '<td>'.$v['status'].'</td>';
   echo '<td>'.$v['last'].'</td>';
   echo '</tr>';
}
?>
</table>
<pre><?php #print_r($json['nl.aap.test1']); ?></pre>
</body>
</html>
'''
'''
ssh user@remotehost 'bash -s' < remotescript.sh > logfile.log
'''
'''
echo "nl.aap.test1 OK 1" > /dev/tcp/localhost/5000
curl  localhost:5000/nl.aap.test1/enable/1
'''

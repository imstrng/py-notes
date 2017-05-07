#!/usr/bin/python3

import asyncio





class Server(asyncio.Protocol):
    def connection_made(self, transport):
        #peername = transport.get_extra_info('peername')
        self.transport = transport
        #print(peername)

    def data_received(self, data):
        message = data.decode().strip('\n')
        print(message)
        #self.transport.write(data)
        self.transport.close()








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
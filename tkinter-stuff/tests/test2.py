import socket
import time
import struct

multicast_group = ('224.3.29.71', 10000)

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

ttl = struct.pack('b', 32)
sock.setsockopt(socket.IPPROTO_IP, socket.IP_MULTICAST_TTL, ttl)


f = open('price.txt')
prices = f.readlines()
f.close()

for r in range(100000):
    for i in prices:
        i.strip('\n')
        sent = sock.sendto(i.encode(), multicast_group)
        #time.sleep(0.01)

sock.close()

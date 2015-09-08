#!/bin/env python

import socket,sys
dest = ('<broadcast>',18080)
udp_client = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)

udp_client.setsockopt(socket.SOL_SOCKET,socket.SO_BROADCAST,1)

udp_client.sendto("hello", dest)

while True:
    (buf , address) = udp_client.recvfrom(2048)
    if not len(buf):
        break
    print "Receive From %s;%s" %(address,buf)
    



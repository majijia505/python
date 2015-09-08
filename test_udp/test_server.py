#!/bin/env python
import socket , sys , traceback

addr=('',18080)
udp_server = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)

udp_server.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1)

udp_server.setsockopt(socket.SOL_SOCKET,socket.SO_BROADCAST,1)

udp_server.bind(addr)

while True:
    try:
        message , address = udp_server.recvfrom(8192)
        print "Got Connection from:" , address
        udp_server.sendto("i am here",address)
        
    except(KeyboardInterrupt,SystemExit):
        raise
    except:
        traceback.print_exc()
        
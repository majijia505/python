#!/bin/env python

import socket

s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

s.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR ,1)

s.bind(('',49999))

s.listen(5)

while 1:
    clientsock,clientaddr = s.accept()
    print "Got connection from ",clientsock.getpeername()
    clientsock.close()


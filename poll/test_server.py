#!/bin/env python

import socket,sys,time,traceback
host = ''
port = 49999
server = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

server.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1)

server.bind((host,port))

server.listen(1)

while True:
    try:
        client_sock , address = server.accept()
    except(KeyboardInterrupt,SystemExit):
        raise
    except:
        traceback.print_exc()
        
    print "Got Connection from :" ,client_sock.getpeername()
    try:
        while True:
            try:
                client_sock.sendall(time.asctime()+"\n")
            except:
                print traceback.print_exc()
                break
            time.sleep(5)
    except(KeyboardInterrupt,SystemExit):
        raise
    except:
        traceback.print_exc()
    
    
    try:
        client_sock.close()
    except(KeyboardInterrupt,SystemExit):
        raise
    except:
        traceback.print_exc()
    
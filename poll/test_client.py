#!/bin/env python

import socket,sys,select
host = ''
port = 49999
client = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

spinsize = 10
spinpos = 0
spindir = 1

def my_love():
    print "hello"
    
client = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

client.connect((host,port))

p = select.poll()
p.register(client.fileno(),select.POLLIN|select.POLLERR|select.POLLHUP)

while 1:
    results = p.poll(50)
    if len(results):
        if results[0][1] == select.POLLIN:
            data = client.recv(2048)
            if not len(data):
                print "The remote host may be closed;exting\n",
                break
            sys.stdout.write("\rReceived: "+data)
            sys.stdout.flush()
            
        else:
            print "\rProblem occured ;exting"
        
    my_love()
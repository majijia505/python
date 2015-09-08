#!/bin/env python
import struct , sys

def htons(num):
	return struct.pack('!H',num)

def htonl(num):
	return struct.pack('!I',num)

def ntons(num):
	return struct.unpack('!H',data)[0]

def ntohs(num):
	return struct.unpack('!I',data)[0]


def sendstr(str):
	return htonl(len(str)) + str


print "please enter a string:"
str = sys.stdin.readline().rstrip()

print repr(sendstr(str))

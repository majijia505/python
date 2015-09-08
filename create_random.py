#!/bin/env python

import random
f = open('random.txt','w')
for i in xrange(1,100000000):
    num = random.randint(1,200000000000)
    #print num
    f.write(str(num)+"\n")
    if (i % 100) == 0:
        f.flush()
        print "i have flush 100 integer"

f.close() 

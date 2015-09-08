#!/bin/env python
#encoding:utf-8
import heapq
import time

#定义函数get_origin，从文件获取前10个数字作为基础值进行比较

def get_origin(f):
    origin_list = []
    for i in range(1000000):
        num = int(f.readline().strip())
        heapq.heappush(origin_list,num)
    
    return origin_list
    
def get_top(f):
    origin_list = get_origin(f)
    while True:
        big_list = f.readlines(100000000)
        if not big_list:
            break
        for i in big_list:
            num = int(i.strip())
            num = heapq.heappushpop(origin_list,num)
            #heapq.heappush(origin_list,num)

    return origin_list
    
    
if __name__ == '__main__':
    start_time = time.clock()
    with open('random.txt','r') as f:
        top_list = get_top(f)
     
    while top_list:
        print heapq.heappop(top_list)
    stop_time = time.clock()
    print "the program processed has been %.2f" %(stop_time - start_time)
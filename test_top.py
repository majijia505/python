#!/bin/env python
#encoding:utf-8
#定义函数get_origin，从文件获取前10个数字作为基础值进行比较
import time
def get_origin(f):
    origin_list = []
    for i in range(10):
        num = int(f.readline().strip())
        origin_list.append(num)
    origin_list.sort()   
    return origin_list
    
    
#定义函数，对每个函数进行对比，如果获取的值比origin_list的最小值大，则删除最小值，并用该值替换最小值并排序
#返回top 10

def top_sort(f):
    origin_list = get_origin(f)
    #count = 0
    for i in f:
        num = int(i.strip())
        if num >= origin_list[0]:
            origin_list[0] = num
            origin_list.sort()
        #count +=1
        #if  (count >= 10000) and ((count % 10000)  == 0):
            #print "i have processed %d number to be sorted" %count
    return origin_list

if __name__ == "__main__":
    start_time = time.clock()
    f = open('random.txt','r')
    sored_list = top_sort(f)
    for i in sored_list:
        print "%d" %i
    stop_time = time.clock()
    print "the program processed has been %.2f" %(stop_time - start_time)
        
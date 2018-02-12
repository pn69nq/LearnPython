# -*-coding:utf-8-*-
import os.path
def hello():
    print('hello world')
#循环
def loop():
    lst = [1,2,3,4]
    for name in lst:
         print(name)
#数据类型         
def datastruct():
    #list
    list = ['test',1,2]
    #for l in list:
       # print(l)
    dict = {'test':1,'good':'2'}
    for key,value in dict.iteritems():
        #print(key,value)
        print(key)
        print("======")
        print(value)
    for key,value in dict.items():
        print key,value
    for key in dict.keys():
        print key
    for value in dict.values():
        print value
#列表生成式
def listcreate():
    L = list(x*x for x in range(1,12))
    print(L)
    

#分片
def slices():
    s = [1,2,3,4]
    print(s[2:3])

if __name__ == '__main__':
    #loop()
    #slices()
    #datastruct()
    listcreate()


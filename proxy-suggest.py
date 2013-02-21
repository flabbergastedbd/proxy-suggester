# -*- coding: utf-8 -*-
"""
Created on Sat Feb 16 12:05:31 2013

@author: tunnelshade
"""

import connection, details_extractor
import time, threading

def keyFromValue(dictionary, value):
    for key in dictionary.keys():
        if dictionary[key] == value:
            return(key)

def getTime(start):
    instant = round(time.time()-start,0)
    return("[%2d:%2d]"%(int(instant//60),int(instant%60)))    
    
start = time.time()    

flag, user_data = details_extractor.extractData()
if not flag:
    print(user_data)
    exit(0)
global running

class ConnectThread(threading.Thread):
    def __init__(self,host,port,username,password,delay):
        super(ConnectThread, self).__init__()
        self.delay = delay
        self.host = host
        self.password = password
        self.port = port
        self.username = username
    def run(self):
        while True:
            sock_object = connection.ConnectionSocket(self.delay)
            status = sock_object.tryToConnect(self.host,self.port,self.username,self.password)
            if status == 200:
                print(getTime(start)+" Proxy "+str(self.host)+" is accepting connections at delay "+str(self.delay))
                if self.delay != 0.1:
                    self.delay -= 0.1
                time.sleep(10)
            elif status == 408:
                print(getTime(start)+" Proxy "+str(self.host)+" is not responding at delay "+str(self.delay))
                self.delay += 0.1
                time.sleep(1)
            elif status == 407:
                print(getTime(start)+" Incorrect credentials provided for "+str(self.host))
                exit()
            elif status == 404:
                print(getTime(start)+" Proxy "+str(self.host)+" seems down or Invalid")
            elif status == 504:
                print(getTime(start)+" Proxy "+str(self.host)+" is refusing connections")
                time.sleep(600)
 
count = 0 
thread_list = []
if __name__ == "__main__":
    for proxy_data in user_data:            
        thread_list.append(ConnectThread(proxy_data[2],int(proxy_data[3]),proxy_data[0],proxy_data[1],0.5))
        thread_list[count].start()
        count += 1
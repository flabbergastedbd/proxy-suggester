# -*- coding: utf-8 -*-
"""
Created on Sat Feb 16 12:05:31 2013

@author: tunnelshade
"""

import connection, details_extractor
import time

def keyFromValue(dictionary, value):
    for key in dictionary.keys():
        if dictionary[key] == value:
            return(key)

flag, user_data = details_extractor.extractData()
if not flag:
    print(user_data)
    exit(0)

connected_flag = False

delay = 5

while flag:
    if not connected_flag:
        running_proxies = {}
        for proxy_data in user_data:
            
            sock_object = connection.ConnectionSocket(delay)
            status = sock_object.tryToConnect(proxy_data[2],int(proxy_data[3]),proxy_data[0],proxy_data[1])
            if status == "Success":
                running_proxies[proxy_data[2]] = delay
                
        print("\n")
        
        if not running_proxies.keys():
            delay += 2
            connected_flag = False
        elif len(running_proxies.keys()) == 1:
            delay_list = running_proxies.values()
            delay_list.sort()
            if delay != 1:
                delay -= 2
            print("The immediate choice for you right now is "+keyFromValue(running_proxies,delay_list[0]))
            print("\n")            
            connected_flag = True
        else:
            print("The immediate choices for you right now are "+str(running_proxies.keys()))
            print("\n")
            time.sleep(5)
            if delay != 1:
                delay -= 2
            connected_flag = False
            
    else:
        time.sleep(30)
        connected_flag = False
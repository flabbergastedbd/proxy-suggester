# -*- coding: utf-8 -*-
"""
Created on Sat Feb 16 12:08:59 2013

@author: tunnelshade
"""

import os

def extractData():
    
    working_dir = os.getcwd()
    config_path = os.path.join(working_dir,'config.txt')    
    
    if os.path.isfile(config_path):
        print("Yeah, config file exists")
        
        proxy_list = []
        proxy_data = file(config_path,'r')

        for line in proxy_data.readlines():
            details = line.split(':')
            details.pop()
            proxy_list.append(details)

        return(True, proxy_list)
        
    else:
        print("\n")
        print("Config.txt is not present at "+working_dir)
        return(False, "Failed")

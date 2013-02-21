# -*- coding: utf-8 -*-
"""
Created on Sat Feb 16 10:11:13 2013

@author: tunnelshade
"""

import socket
import base64

            # The same port as used by the server

class ConnectionSocket():
    
    def __init__(self,delay = 3):
        self.s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        self.s.settimeout(delay)
        self.delay = delay

    def tryToConnect(self,host,port,username,password):       
        try:
            socket.gethostbyaddr(host)
        except Exception:
            #print("Proxy "+host+" is not valid")
            return(404)
        
        try:
            self.s.connect((host,port))
            message = "GET http://www.google.co.in/ HTTP/1.1\r\n"
            auth_phrase = str(base64.b64encode(str(username)+":"+str(password)))
            message += "Proxy-Authorization: Basic " + auth_phrase + "\r\n\r\n"
            self.s.sendall(message)
            data = str(self.s.recv(13))
            data = data.split()
            if data[-1] == '407':
                #print("Your credentials of "+host+" are incorrect")
                return(407)
            
            #print("Proxy Server at "+host+" is accepting connections at "+str(self.delay)+" seconds delay")
            return(200)
         
        except socket.timeout:
            #print("Proxy Server at "+host+" is not responding at "+str(self.delay)+" seconds delay")
            return(408)
            
        except socket.error:
            #print("Proxy Server at "+host+" is refusing connections")
            return(504)
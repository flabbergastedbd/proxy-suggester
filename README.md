proxy-suggester
===============

Until this version this script tells you the status & delay time of various proxies. So based on this data, user can pick his best catch. Rather
than pinging each proxy individually, try to use this script as this script also checks whether the proxy server is allowing connections.
So you can know the list of proxies that are working in matter of seconds. The future version of this script is supposed to use TorCtl
library of python for controlling tor.

Usage 
=====

python proxy-suggest.py

Make sure the config file is written in correct format & the delay times are to be varied manually as per the network conditions in users place.


Platforms 
=========
This script is tested on linux where it works fine. 


Version Specs
=============

The previous version of this script worked in a synchronous manner, but in this version multi threading has been used.

'''
Created on 01/10/2013

@author: jmacias
'''

# Send UDP broadcast packets

PORT = 8500

import sys, time
from socket import *

s = socket(AF_INET, SOCK_DGRAM)
s.bind(('', 0))
s.setsockopt(SOL_SOCKET, SO_BROADCAST, 1)

while 1:
    data = repr(time.time()) + '\n'
    s.sendto(data, ('', PORT))
    print "SENT %s" % data
    time.sleep(2)



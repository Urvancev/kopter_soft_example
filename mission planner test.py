import sys
sys.path.append(r"c:\python27\lib")

import socket

print 'Start Script'

print "roll = ",cs.roll
print "pitch = ",cs.pitch
print "yaw = ",cs.yaw

Script.WaitFor('ARMING MOTORS',30000)
Script.SendRC(4,1500,True)
print 'Motors Armed!'

Script.SendRC(1,1100,True)
Script.SendRC(2,1200,True)
Script.SendRC(3,1300,True)
Script.SendRC(4,1400,True)


s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
print "sock ok"
s.connect(('127.0.0.1',9010))
print "connect"
s.send("hello")
data = s.recv(1024)
print data

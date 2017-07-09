import socket

s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
print "sock ok"

s.bind(('127.0.0.1',9010))
print 'bind ok'

s.listen(2)
conn,addr = s.accept()
print addr
data = conn.recv(1024)
print data
conn.send(data)

import socket
c=socket.socket()
c.connect((socket.gethostname(),8990))
name=input('Enter your name') 
c.send(bytes(name,'utf-8'))
print(c.recv(10).decode())
import socket
c=socket.socket()
c.connect(('localhost',8990))
#ip adress and port number written above
name=input('Enter your name')
c.send(bytes(name,'utf-8'))
#recieving and decoding
    print(c.recv(1024).decode())
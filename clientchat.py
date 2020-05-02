import socket
c=socket.socket()   
c.connect(('localhost',8990))
#ip adress and port number written above
#q=str(input('Ask:'))
#c.send(bytes(q,'utf-8'))
while True:
    n=input('Client:')
    c.send(bytes(n,'utf-8'))
    print(c.recv(1024).decode())
print(c.recv(1024).decode())
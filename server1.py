import socket
s= socket.socket()
print('Socket Created')
#bind,used tuple cause bind accepts one arg
s.bind((socket.gethostname(),8990))
s.listen(3)  
while True: 
#    accept connection.....it wil read 2 value client and addr
    c, addr=s.accept() 
    a=c.recv(10).decode() 
    print("connection with",addr)
    print(a)
# send message to client,convert the bytes into string therefore used utf-8
    c.send(bytes('Sneha Singg','utf-8'))
    c.close() 
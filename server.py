import socket
s= socket.socket()
#no arg in the above then --tcp otherwise udp
print('Socket created')
#bind,used tuple cause bind accepts one arg
s.bind(('localhost',8990))
s.listen(3)
#queue size=3
print('Waiting for connection') 
#after accepting connection
while True:
#    accept connection.....it wil read 2 value client and addr
    c, addr=s.accept()
    a=c.recv(1024).decode()
    print("connection with",addr)
    print(a)
# send message to client,convert the bytes into string therefore used utf-8
    c.send(bytes('Sneha Singg','utf-8'))
    c.close()
#arithmetic o/p and server will perfrom and send result
#    chat window predefined q and ans
#    symptoms for fever --server will answer
#    create dict in server,match the q asked by client int key of the dict and return value to client
#    key--q, value-ans
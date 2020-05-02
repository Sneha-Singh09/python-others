import socket
s=socket.socket()
print('Socket created')
#bind,used tuple cause bind accepts one arg
s.bind(('localhost',8990))
s.listen(3)
#queue size=3
print('Waiting for connection')
#after accepting connection
def arith_op(c,addr):
    o=c.recv(1024).decode()
    a=c.recv(1024).decode()
    b=c.recv(1024).decode()
    a=int(a)
    b=int(b)
    if(o=='+'):
        ans=a+b
    if(o=='-'): 
        ans=a-b
    if(o=='*'):
        ans=a*b
    if(o=='/'):
        ans=a/b
    if(o=='%'):
        ans=a%b
    print(ans)
    c.send(bytes(str(ans),'utf-8'))
while True:
    c, addr=s.accept()
#    o=c.recv(1024).decode()
#    a=c.recv(1024).decode()
#    b=c.recv(1024).decode() 
    
    print("connection with",addr)
#    a=int(a)
#    b=int(b)
#    if(o=='+'):
#        ans=a+b
#    if(o=='-'): 
#        ans=a-b
#    if(o=='*'):
#        ans=a*b
#    if(o=='/'):
#        ans=a/b
#    if(o=='%'):
#        ans=a%b
#    or
    arith_op(c,addr)
#    c.send(bytes(str(ans),'utf-8'))
    c.close()
import socket
s= socket.socket()
#no arg in the above then --tcp
print('Socket created')
#bind,used tuple cause bind accepts one arg
s.bind(('localhost',8990))
s.listen(1) 
#queue size=3
print('Waiting for connection')
#after accepting connection
def chat(c,addr):
    print('Chat Started')
    connected=True
#while so that we can continue to talk till wewant
    while connected==True:
        n=c.recv(1024).decode()
        if(n=='BYE'):
            connected=False
            print(n)
        else:
          print('Client:',n)
#            qa={'What is your good name':'Sneha Singh','Current Fav Song':'Pal','Whose the Boss':'Sneha Always','Sneha loves':'Ofcourse food and deerinks'}
#            ans=''
#            for k,v in qa.items():
#                if k==n:
#                    ans=v
#        reply='Server:'+ans
        reply=input('Server: ')
        reply='Server: '+ reply
        c.send(bytes(reply,'utf-8')) 
    c.close()
while True:
#    accept connection.....it wil read 2 value client and addr
    c, addr=s.accept() 
    chat(c,addr)
#    qa={'What is your good name':'Sneha Singh','Current Fav Song':'Pal','Whose the Boss':'Sneha Always','Sneha loves':'Ofcourse food and deerinks'}
#    a=c.recv(1024).decode()
#    print("connection with",addr)
#    if(a=='What is your good name'):
#        print(qa['What is your good name'])
#        c.send(bytes(qa['What is your good name'],'utf-8'))
#    if(a=='Current Fav Song'):
#        print(qa['Current Fav Song'])
#        c.send(bytes(qa['Current Fav Song'],'utf-8'))
#    if(a=='Whose the Boss'):
#        print(qa['Whose the Boss'])
#        c.send(bytes(qa['Whose the Boss'],'utf-8'))
#    if(a=='Sneha loves'):
#        print(qa['Sneha loves'])
#        c.send(bytes(qa['Sneha loves'],'utf-8'))                                                         
    c.close()
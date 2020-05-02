from tkinter import *
from PIL import ImageTk,Image
root=Tk()
root.title('CALCULATOR')
root.iconbitmap('Calci.ico')
e1=Entry(root,width=33)
e1.place(x=50,y=50)
l1=[]
l2=[]
def store(num):
     var=e1.get()
     e1.delete(0,END)
     l2.append(num)
     e1.insert(0,var + str(num))
     print(l2)
def equal():
    var1=e1.get()
    l1.append(var1)
    e1.delete(0,END)
    if(operator=='add'):
        e1.insert(0,int(first_num) + int(var1))
    if(operator=='sub'):
        e1.insert(0,int(first_num) - int(var1))
    if(operator=='mul'):
        e1.insert(0,int(first_num) * int(var1))
    if(operator=='div'):
        e1.insert(0,int(first_num) / int(var1))

def clr():
    e1.delete(0,END)
    l2.clear()
    l1.clear()
    print(l1)
def add():
    var=e1.get()
    global first_num
    global operator
    first_num=var
    operator='add'
    e1.delete(0,END)
def subtract():
    var=e1.get() 
    global first_num
    first_num=var
    global operator
    operator='sub'
    e1.delete(0,END)
def multiply():
    var=e1.get()
    global first_num
    first_num=var
    global operator
    operator='mul'
    e1.delete(0,END)
def divide():
    var=e1.get()
    global first_num
    first_num=var
    global operator
    operator='div'
    e1.delete(0,END)
eq=Button(root,text='=',height=3,width=6,fg='green',command=equal)
eq.place(x=150,y=250)
cl=Button(root,text='clear',height=3,width=6,fg='green',command=clr)
cl.place(x=50,y=250)
zero=Button(root,text='0',height=3,width=6,fg='green',command=lambda: store(0))
zero.place(x=100,y=250)
one=Button(root,text='1',height=3,width=6,fg='green',command=lambda: store(1))
one.place(x=50,y=200)
two=Button(root,text='2',height=3,width=6,fg='green',command=lambda: store(2))
two.place(x=100,y=200)
three=Button(root,text='3',height=3,width=6,fg='green',command=lambda: store(3))
three.place(x=150,y=200)
four=Button(root,text='4',height=3,width=6,fg='green',command=lambda: store(4))
four.place(x=50,y=150)
five=Button(root,text='5',height=3,width=6,fg='green',command=lambda: store(5))
five.place(x=100,y=150)
six=Button(root,text='6',height=3,width=6,fg='green',command=lambda: store(6))
six.place(x=150,y=150)
seven=Button(root,text='7',height=3,width=6,fg='green',command=lambda: store(7))
seven.place(x=50,y=100)
eight=Button(root,text='8',height=3,width=6,fg='green',command=lambda: store(8))
eight.place(x=100,y=100)
nine=Button(root,text='9',height=3,width=6,fg='green',command=lambda: store(9))
nine.place(x=150,y=100)
add=Button(root,text='+',height=3,width=6,fg='green',command=add)
add.place(x=200,y=250)
sub=Button(root,text='-',height=3,width=6,fg='green',command=subtract)
sub.place(x=200,y=200)
mul=Button(root,text='*',height=3,width=6,fg='green',command=multiply)
mul.place(x=200,y=150)
div=Button(root,text='/',height=3,width=6,fg='green',command=divide)
div.place(x=200,y=100)



root.mainloop()

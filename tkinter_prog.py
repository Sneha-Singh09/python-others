#tkinter-- develop desktop applications
#
#from tkinter import *
#root=Tk()
#
#root.mainloop()
##widget
#from tkinter import *
#root=Tk()
#label1=Label(root,text='Name',fg='red',bg='blue')
##fg-colour,or use colourcode from google,bg-backgroun
#label1.pack()
#root.mainloop()
##root.mainloop-holds the screen,visibilty for infinite intervals
##otherwise the screen will disappear
#
#from tkinter import *
#root=Tk()
#label1=Label(root,text='name')
#label1.grid(row=0,column=0)
#label1=Label(root,text='id')
#label1.grid(row=1,column=0)
#label1=Label(root,text='contact')
#label1.grid(row=2,column=0)
#root.mainloop()
#
#from tkinter import *
#root=Tk()
#label1=Label(root,text='name',width=10)
#label1.place(x=0,y=0)
#label1=Label(root,text='id',width=10)
#label1.place(x=0,y=20)
#label1=Label(root,text='contact',width=10)
#label1.place(x=0,y=40)
#root.mainloop() 
#-----------button
#from tkinter import *
#root=Tk()
#b1=Button(root,text='submit',width=20,fg='green')
#b1.pack()
#root.mainloop()
#
#from tkinter import *
#root=Tk()
#b1=Button(root,text='submit',width=20,fg='green')
#b1.place(x=100,y=100)
#root.mainloop()
#operations on the button
#from tkinter import *
#root=Tk()
#def submit():
#    label1=Label(root,text='name',width=10)
##    label1.place(x=0,y=0)---overwrites if performed many times
#    label1.pack()
#b1=Button(root,text='submit',width=20,fg='green',command=submit)
#b1.place(x=100,y=50)
#root.mainloop()
#
#from tkinter import *
#root=Tk()
#def submit():
#     print('Sneha')
#b1=Button(root,text='submit',width=20,fg='green',command=submit)
#b1.place(x=100,y=50)
#root.mainloop()
#
#from tkinter import *
#root=Tk()
#l1=[]
#def submit():
#    label1=Label(root,text='SNEHA',width=10)
##    label1.place(x=0,y=0)---overwrites if performed many times
#    label1.pack()
#    l1.append('Sneha')
#b1=Button(root,text='submit',width=20,fg='green',command=submit)
#b1.place(x=100,y=50)
#root.mainloop()
#print(l1)
#entry
#from tkinter import *
#root=Tk()
#e1=Entry(root,width=50)
#e1.pack()
#root.mainloop()
#
#from tkinter import *
#root=Tk()
#e1=Entry(root,width=50)
#e1.place(x=100,y=50)
#root.mainloop()
#to get label and entry on same line y should be same
#from tkinter import *
#root=Tk()
#e1=Entry(root,width=50)
#e1.place(x=100,y=50)
#label1=Label(root,text='Name',width=10)
#label1.place(x=10,y=50)
#root.mainloop()
#print on console
#from tkinter import *
#root=Tk()
#e1=Entry(root,width=50)
#e1.place(x=100,y=50)
#label1=Label(root,text='Name',width=10)
#label1.place(x=10,y=50)
#def submit():
#    var1=e1.get()
#    print(var1)
#b1=Button(root,text='submit',width=20,fg='green',command=submit)
#b1.place(x=50,y=150)
#root.mainloop()
#entered input extracted on the window itself
#from tkinter import *
#root=Tk()
#e1=Entry(root,width=50)
#e1.place(x=100,y=50)
#e2=Entry(root,width=50)
#e2.place(x=100,y=100)
#label1=Label(root,text='Name',width=10)
#label1.place(x=10,y=50)
#label1=Label(root,text='output',width=10)
#label1.place(x=10,y=100)
#def submit():
#    var1=e1.get()
#    e2.delete(0,END)#to remove previous value and not append
#    e2.insert(0,var1)
#b1=Button(root,text='submit',width=20,fg='green',command=submit)
#b1.place(x=50,y=150)
#root.mainloop()
##username password and reset
#from tkinter import *
#root=Tk()
#e1=Entry(root,width=50)
#e1.place(x=100,y=50)
#e2=Entry(root,width=50)
#e2.place(x=100,y=100)
#
#label1=Label(root,text='Username',width=10)
#label1.place(x=10,y=50)
#label1=Label(root,text='password',width=10)
#label1.place(x=10,y=100)
#def submit():
#    var1=e1.get()
#    var2=e2.get()
#    print(var1,var2)
#def reset():
#    e1.delete(0,END)
#    e2.delete(0,END)#to remove previous value and not append
#b1=Button(root,text='submit',width=20,fg='green',command=submit)
#b1.place(x=50,y=150)
#b1=Button(root,text='reset',width=20,fg='green',command=reset)
#b1.place(x=250,y=150)
#root.mainloop()
##add in list
#from tkinter import *
#root=Tk()
#e1=Entry(root,width=50)
#e1.place(x=100,y=50)
#e2=Entry(root,width=50)
#e2.place(x=100,y=100)
#l1=[]
#label1=Label(root,text='Username',width=10)
#label1.place(x=10,y=50)
#label1=Label(root,text='password',width=10)
#label1.place(x=10,y=100)
#def submit():
#    var1=e1.get()
#    var2=e2.get()
##    print(var1,var2)
#    l1.append(var1)
#    l1.append(var2)
#def reset():
#    e1.delete(0,END)
#    e2.delete(0,END)#to remove previous value and not append
#    print(l1)
#    l1.clear()
#b1=Button(root,text='submit',width=20,fg='green',command=submit)
#b1.place(x=50,y=150)
#b1=Button(root,text='reset',width=20,fg='green',command=reset)
#b1.place(x=250,y=150)
#root.mainloop()
#to create log file(for login) don't clear the list
#netse liya
#from tkinter import *
#class GraphicsInterface:
#
#    def __init__(self):
#        self.window = Tk()
#        self.window.geometry("720x500")
#
#        self.clicked=[]
#        button1 = Button(self.window, text="Dice 1", width=13)
#        button2 = Button(self.window, text="Dice 2", width=13)
#        button1.pack()
#        button2.pack()
#
#        button1.configure(command=lambda btn=button1: self.OnClick(btn))
#        button2.configure(command=lambda btn=button2: self.OnClick(btn))
#
#        self.window.mainloop()
#
#    def OnClick(self, btn):
#        text = btn.cget("text")
#        self.clicked.append(text)
#        print("clicked:", self.clicked)
#
#app = GraphicsInterface()
##CALCI
#from tkinter import *
#root=Tk()
#e1=Entry(root,width=33)
#e1.place(x=50,y=50)
#l1=[]
#l2=[]
#def store():
#    var=e1.get()
#    e1.insert(0,
#    l2.append(var)
#def equal():
#    var1=e1.get()
#    l2.append(var1)
#    if(l1[0]=='1'):
#        ans=l2[0]+l2[1]
#        e1.insert(0,ans)
#    if(l1[0]=='2'):
#        ans=l2[0]-l2[1]
#        e1.insert(0,ans)
#    if(l1[0]=='3'):
#        ans=l2[0]*l2[1]
#        e1.insert(0,ans)
#    if(l1[0]=='4'):
#        ans=l2[0]/l2[1]
#        e1.insert(0,ans)
#    l2.clear()
#    l1.clear()
#def clr():
#    e1.delete(0,END)
#    l2.clear()
#    l1.clear()
#    print(l1)
#def add(i,j):
#    e1.delete(0,END)
#    l1.append('1')
#    print(l1)
#def diff(i,j):
#     e1.delete(0,END)
#     l1.append('2')
#     print(l1)
#def multiply(i,j):
#     e1.delete(0,END)
#     l1.append('3')
#     print(l1)
#def divide(i,j):
#     e1.delete(0,END)
#     l1.append('4')
#     print(l1)
#eq=Button(root,text='=',height=3,width=6,fg='green',command=equal)
#eq.place(x=150,y=250)
#cl=Button(root,text='clear',height=3,width=6,fg='green',command=clr)
#cl.place(x=50,y=250)
#zero=Button(root,text='0',height=3,width=6,fg='green',command=store)
#zero.place(x=100,y=250)
#one=Button(root,text='1',height=3,width=6,fg='green',command=store)
#one.place(x=50,y=200)
#two=Button(root,text='2',height=3,width=6,fg='green',command=store)
#two.place(x=100,y=200)
#three=Button(root,text='3',height=3,width=6,fg='green',command=store)
#three.place(x=150,y=200)
#four=Button(root,text='4',height=3,width=6,fg='green',command=store)
#four.place(x=50,y=150)
#five=Button(root,text='5',height=3,width=6,fg='green',command=store)
#five.place(x=100,y=150)
#six=Button(root,text='6',height=3,width=6,fg='green',command=store)
#six.place(x=150,y=150)
#seven=Button(root,text='7',height=3,width=6,fg='green',command=store)
#seven.place(x=50,y=100)
#eight=Button(root,text='8',height=3,width=6,fg='green',command=store)
#eight.place(x=100,y=100)
#nine=Button(root,text='9',height=3,width=6,fg='green',command=store)
#nine.place(x=150,y=100)
#add=Button(root,text='+',height=3,width=6,fg='green',command=add)
#add.place(x=200,y=250)
#sub=Button(root,text='-',height=3,width=6,fg='green',command=diff)
#sub.place(x=200,y=200)
#mul=Button(root,text='*',height=3,width=6,fg='green',command=multiply)
#mul.place(x=200,y=150)
#div=Button(root,text='/',height=3,width=6,fg='green',command=divide)
#div.place(x=200,y=100)
#root.mainloop()
#images
#from tkinter import *
#from PIL import ImageTk,Image
#
#root=Tk()
#root.title('CARS')
#root.iconbitmap('Caricon.ico')
#my_img=ImageTk.PhotoImage(Image.open('car2.jpg'))
#my_label=Label(image=my_img)
#my_img1=ImageTk.PhotoImage(Image.open('car.jpg'))
#my_label1=Label(image=my_img1)
#my_img2=ImageTk.PhotoImage(Image.open('classiccar.jpg'))
#my_label2=Label(image=my_img2)
#def f_img():
#    global img_no
#    img_no=1
#    my_label.grid(row=0,column=0) 
#def s_img():
#    global img_no
#    img_no=2
#    my_label1.grid(row=0,column=0) 
#def t_img():
#    global img_no
#    img_no=3
#    my_label2.grid(row=0,column=0)
#def to_quit(): 
#    root.destroy()
#def next_pic():
#    if(img_no==1):
#         my_label.grid_remove()     
#         s_img()
#    else:
#         my_label1.grid_remove()     
#         t_img()
##    if(img_no==3):
##          break
#def previous_pic():
##    if(img_no==1):
##          
#    if(img_no==2):
#         my_label1.grid_remove()
#         f_img()
#    if(img_no==3): 
#         my_label2.grid_remove()    
#         s_img()
#f_img()    
#b_prev=Button(root,text='<<',command=previous_pic)
#b_prev.grid(row=10,column=0,columnspan=1)
#b_quit=Button(root,text="QUIT",command=to_quit) 
#b_quit.grid(row=10,column=1)
#b_next=Button(root,text='>>',command=next_pic)
#b_next.grid(row=10,column=10)
#root.mainloop()
#-------top and opening second window------------
#from tkinter import *
#root=Tk()
#root.title('LOGIN')
#root.iconbitmap('Graphics-Google.ico')
#def open():
#    top=Toplevel()
#    top.title('Google')
#    top.iconbitmap('Google.ico')
#    l1=Label(top,text='REGISTER',fg='green').pack()
#    b1=Button(top,text='Close',command=top.destroy).pack()
#b2=Button(root,text='open new page',command=open).pack()
#root.mainloop()
##-------MESSAGEBOX------------
#from tkinter import *
#from tkinter import messagebox
#root=Tk()
#root.title('LOGIN')
#root.iconbitmap('Graphics-Google.ico')
##showinfo askokcancel askquestion showerror showwarning askyesno....many more
#def popup():
#    response=messagebox.showwarning("Authentication",'Invalid username password')
#    print(response)
#b1=Button(root,text='submit',command=popup).pack()
#root.mainloop()
#filedialog-----------------------------
#from tkinter import *
#from tkinter import filedialog
#from PIL import ImageTk,Image
#root=Tk()
#root.title('Sneha')
#root.filename=filedialog.askopenfilename(initialdir='/desktop',title='Select',filetypes=(('JPG image','*.jpg'),("icon image",'*.ico'),('all files','*.*')))
#print(root.filename)
#my_img=ImageTk.PhotoImage(Image.open(root.filename))
#l1=Label(image=my_img).pack()
#root.mainloop()
#-------------frame--------------
from tkinter import *
root=Tk()
frame=LabelFrame(root,text='1',padx=100,pady=50)
frame.pack(padx=15,pady=15)
#l1=Label(frame,text='name')
#l1.grid(row=0,column=0)
#button=Button(frame,text='submit')
#button.grid(row=1,column=0)
root.mainloop()
##-------2 frames---------
#from tkinter import *
#root=Tk()
#frame=LabelFrame(root,text='1',padx=100,pady=250)
#frame.pack(padx=15,pady=15)
#button=Button(frame,text='submit')
#button.pack()
#frame2=LabelFrame(frame,text='2 frame',padx=100,pady=50)
#frame2.pack(padx=15,pady=15)
#b1=Button(frame2,text='again we are here')
#b1.pack()
#root.mainloop()
#radiobutton
#from tkinter import *
#root=Tk()
#r=StringVar()
#r.set('Female')
#rb=Radiobutton(root,text='Female',variable=r,value='Female').grid(row=0,column=1)
#rb1=Radiobutton(root,text='male',variable=r,value='male').grid(row=0,column=2)
#lb1=Label(root,text='Gender').grid(row=0,column=0)
#root.mainloop()
#-------radiobutton forloop------------
#from tkinter import *
#from PIL import ImageTk,Image
#root=Tk()
#root.title('F.R.I.E.N.D.S.')
#root.iconbitmap('friends.ico')
#my_img=ImageTk.PhotoImage(Image.open('Friends-1-icon.png'))
#lb1=Label(image=my_img).grid(row=7,column=3)
#
#friends=StringVar()
#friends.set('Female')
#lb1=Label(root,text='Choose you fav:').grid(row=0,column=0)
#fr=[('Ross','Ross'),('Rachel','Rachel'),('Monica','Monica'),('Joey','Joey'),('Chandler','Chandler'),('Phoebe','Phoebe')]
#r=0
#c=1
#def sub():
#    ans=friends.get()
#    print(ans)
#for text1,value1 in fr:
#    rb=Radiobutton(root,text=text1,variable=friends,value=value1)
#    rb.grid(row=r,column=c)
#    r+=1
#b=Button(root,text='submit',command=sub).grid(row=7,column=1)
#root.mainloop()
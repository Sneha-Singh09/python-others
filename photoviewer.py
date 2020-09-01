#to view the demo of this project checkout this link: https://github.com/Sneha-Singh09/python-others/blob/master/CARS%202020-08-28%2022-29-06.mp4
from tkinter import *
from PIL import ImageTk,Image

root=Tk()
root.title('CARS')
root.iconbitmap('Caricon.ico')
my_img=ImageTk.PhotoImage(Image.open('car2.jpg'))
my_label=Label(image=my_img)
my_img1=ImageTk.PhotoImage(Image.open('car.jpg'))
my_label1=Label(image=my_img1)
my_img2=ImageTk.PhotoImage(Image.open('classiccar.jpg'))
my_label2=Label(image=my_img2)
def f_img():
    global img_no
    img_no=1
    my_label.grid(row=0,column=0) 
def s_img():
    global img_no
    img_no=2
    my_label1.grid(row=0,column=0) 
def t_img():
    global img_no
    img_no=3
    my_label2.grid(row=0,column=0)
def to_quit(): 
    root.destroy()
def next_pic():
    if(img_no==1):
         my_label.grid_remove()     
         s_img()
    else:
         my_label1.grid_remove()     
         t_img()
def previous_pic():         
    if(img_no==2):
         my_label1.grid_remove()
         f_img()
    if(img_no==3): 
         my_label2.grid_remove()    
         s_img()
f_img()    
b_prev=Button(root,text='<<',command=previous_pic)
b_prev.place(x=0,y=455)
b_quit=Button(root,text="QUIT",command=to_quit) 
b_quit.place(x=300,y=455)
b_next=Button(root,text='>>',command=next_pic)
b_next.place(x=570,y=455)

root.mainloop()

from tkinter import *
from tkinter import messagebox
from tkinter import Scrollbar
from PIL import ImageTk,Image
root=Tk()
root.title('GOOGLE ACCOUNTS')
root.iconbitmap('googlelogo.ico')
my_img=ImageTk.PhotoImage(Image.open('g.jpg'))
gl_img=ImageTk.PhotoImage(Image.open('glogo.jpg')) 
g_img=ImageTk.PhotoImage(Image.open('glogo2.jpg'))
hide=ImageTk.PhotoImage(Image.open('hide.jpg')) 
unhide=ImageTk.PhotoImage(Image.open('unhide.jpg'))
personal=ImageTk.PhotoImage(Image.open('personal.jpg'))
icon=ImageTk.PhotoImage(Image.open('icon.jpg'))
flag=ImageTk.PhotoImage(Image.open('flag.jpg'))
welc=ImageTk.PhotoImage(Image.open('welcome.jpg'))
def final():
    top4=Toplevel()
    top4.title('GMAIL')
    top4.iconbitmap('Gmail.ico')
    lab=Label(top4,image=welc)
    lab.pack()
    
def privacypolicy(): 
    top3=Toplevel()
    top3.title('GMAIL')
    top3.iconbitmap('Gmail.ico') 
    frame3=LabelFrame(top3,text='PRIVACY AND TERMS',font=('Helvetica', 15, 'bold'),border=7,padx=50,pady=50)
    frame3.pack(padx=10,pady=10)
    

    sb=Scrollbar(frame3,orient=VERTICAL)
    sb.pack(fill=Y,side=RIGHT)  
#    sb1=Scrollbar(frame3,orient=HORIZONTAL)
#    sb1.pack(fill=X,side=BOTTOM)
   
    op=['To create a Google Account, you’ll need to agree to the Terms of Service below.',
        ' In addition, when you create an account, we process your information as described in our Privacy Policy, including these key points:',
        'Data we process when you use Google',
        'When you set up a Google Account, we store information you give us like your name, email address, and telephone number.',
        'When you use Google services to do things like write a message in Gmail or comment on a YouTube video, we store the information you create.',
        'When you search for a restaurant on Google Maps or watch a video on YouTube, for example, we process information about that activity – including information like the video you watched, device IDs, IP addresses, cookie data, and location.',
        'We also process the kinds of information described above when you use apps or sites that use Google services like ads, Analytics, and the YouTube video player.',
        'Why we process it',
        'We process this data for the purposes described in our policy, including to:',
        'Help our services deliver more useful, customized content such as more relevant search results;',
        'Improve the quality of our services and develop new ones;',
        'Deliver personalized ads, depending on your account settings, both on Google services and on sites and apps that partner with Google;',
        'Improve security by protecting against fraud and abuse; and',
        'Conduct analytics and measurement to understand how our services are used. We also have partners that measure how our services are used. Learn more about these specific advertising and measurement partners.',
        'Combining data',
        'We also combine this data among our services and across your devices for these purposes. For example, depending on your account settings, we show you ads based on information about your interests, which we can derive from your use of Search and YouTube, and we use data from trillions of search queries to build spell-correction models that we use across all of our services.',
        'You’re in control',
        'Depending on your account settings, some of this data may be associated with your Google Account and we treat this data as personal information.You can always adjust your controls later or withdraw your consent for the future by visiting My Account (myaccount.google.com).'
        ]
    txtbox = Text(frame3, yscrollcommand = sb.set )
    txtbox.pack()
    for e in op:
        txtbox.insert(END,str(e))
    txtbox.pack( side = LEFT )  
    sb.config( command = txtbox.yview )  
#    sb1.config( command = txtbox.xview )  
    b_next=Button(frame3,text='I AGREE',bg='Blue',font=7,fg='White',command=final)
    b_next.place(x=500,y=400)
    b_next=Button(frame3,text='BACK',fg='Blue',font=7,bg='White',command=top3.destroy)
    b_next.place(x=10,y=400) 
#    img_per=Label(frame3,image=personal)
#    img_per.place(x=600,y=10)
    
def tocheck():
#    global e_1,e_u,enp,ecp
#    if len(e_1.get())==0 or len(e_l.get())==0 or len(e_u.get())==0 or len(enp.get())==0 or len(ecp.get())==0:
#        res=messagebox.showwarning('Authentictaion','Please fill all the details')
#    else:
#        if enp.get()!=ecp.get():
#            re=messagebox.showerror('Error','Passwords not matching')
#        else:
            thirdwin()
    
def thirdwin():
        global e_u,e_1
        top2=Toplevel()
        top2.title('GMAIL REGISTER')
        top2.iconbitmap('Gmail.ico')
        frame2=LabelFrame(top2,text='GOOGLE',font=('Helvetica', 15, 'bold'),border=7,padx=50,pady=50)
        frame2.pack(padx=10,pady=10)
        name=e_1.get()
        lb_1n=Label(frame2,text=f'{name}, welcome to Google',font=('Helvetica',13, 'bold'),fg='Black')
        lb_1n.grid(row=0,column=0,columnspan=1)
        lb_icon=Label(frame2,image=icon) 
        lb_icon.grid(row=1,column=0)
        email=e_u.get()
        lb_email=Label(frame2,text=f'{email}',font=('Helvetica',13, 'bold'))
        lb_email.grid(row=2,column=0)
        lb_1n=Label(frame2,text='Phone Number',font=('Helvetica',13, 'bold'),fg='Black')
        lb_1n.grid(row=3,column=0)
        lb_f=Label(frame2,image=flag)
        lb_f.grid(row=3,column=1)
        e_1=Entry(frame2,width=30,font=10) 
        e_1.grid(row=3,column=2,columnspan=3)
        lb_opp=Label(frame2,text="*Optional",font=13,fg='Grey')
        lb_opp.grid(row=3,column=5)
        lb_1n=Label(frame2,text="(We will use your number for account security.It won't be visible to others)",font=13,fg='Black')
        lb_1n.grid(row=4,column=1,columnspan=4)
        lb_re=Label(frame2,text='Recovery email address',font=('Helvetica',13, 'bold'),fg='Black')
        lb_re.grid(row=5,column=0)
        e_re=Entry(frame2,width=40,font=10) 
        e_re.grid(row=5,column=1,padx=0,pady=5,columnspan=3)
        lb_opp=Label(frame2,text="*Optional",font=13,fg='Grey')
        lb_opp.grid(row=5,column=4)
        lb_rem=Label(frame2,text="(We will use it to keep your account secure)",font=13,fg='Black')
        lb_rem.grid(row=6,column=1,columnspan=3)
        lb_b=Label(frame2,text='Your Birthday',font=('Helvetica',13,'bold'),fg='Black')
        lb_b.grid(row=7,column=0)
        m_list=['January','February','March','April','May','June','July','August','September',
                'October','November','December' ] 
        variable = StringVar(frame2)
        variable.set('Month')  
        m=OptionMenu(frame2, variable, *m_list)
        m.config(width=7, font=('Helvetica', 13),bg='White')
        m.grid(row=7,column=1)
        lb_b=Label(frame2,text='DAY',font=('Helvetica', 15),fg='Black')
        lb_b.grid(row=7,column=2)
        e_b=Entry(frame2,width=8,font=10) 
        e_b.grid(row=7,column=3,padx=5,pady=5)
        lb_b=Label(frame2,text='YEAR',font=('Helvetica', 15),fg='Black')
        lb_b.grid(row=7,column=4)
        e_b=Entry(frame2,width=8,font=10) 
        e_b.grid(row=7,column=5,padx=5,pady=10)
        lb_b=Label(frame2,text='Gender',font=('Helvetica',13,'bold'),fg='Black')
        lb_b.grid(row=8,column=0)
        g_list=['Female','Male','Transgender','Other' ] 
        variable = StringVar(frame2)
        variable.set('Select one')
        g=OptionMenu(frame2, variable, *g_list)
        g.config(width=9, font=('Helvetica', 15),bg='White')
        g.grid(row=8,column=1)
        b_next=Button(frame2,text='Next',bg='Blue',font=7,fg='White',command=privacypolicy)
        b_next.grid(row=9,column=4,padx=10,pady=10)
        b_si=Button(frame2,text='BACK',font=7,bg='White',fg='Blue',command=top2.destroy)
        b_si.grid(row=9,column=1,padx=10,pady=15)
        img_per=Label(frame2,image=personal)
        img_per.grid(row=3,column=8,rowspan=6)
def pop_u():
    response=messagebox.showerror('Errrr',"Even I don't remember... Next time please do")
def pop_up(): 
    if  len(e.get())==0 or len(ep.get())==0:
                    res=messagebox.showwarning('Errrrr','Not Valid Email and Password')
    else:
        res=messagebox.showinfo('Sorry','Not done this part... have to wait')
        
def newwin():
    top=Toplevel()
    top.title('GMAIL REGISTER')
    top.iconbitmap('Gmail.ico')
    frame1=LabelFrame(top,text='Create Your Google Account',font=('Helvetica', 15, 'bold'),border=7,padx=50,pady=50)
    frame1.pack(padx=15,pady=15)
#    this padx and pady show the frame +15 more on the   screen
#    frame1.config(bg='White')
    lb_1n=Label(frame1,text='First name: ',font=('Helvetica',13, 'bold'),fg='Black')
    lb_1n.grid(row=2,column=0)
    global e_1,e_l
    e_1=Entry(frame1,width=25,font=10) 
    e_1.grid(row=2,column=1,columnspan=1)
    lb_ln=Label(frame1,text='Last name: ',font=('Helvetica',13, 'bold'),fg='Black')
    lb_ln.grid(row=2,column=2)
    e_l=Entry(frame1,width=25,font=10)
    e_l.grid(row=2,column=3,pady=20)
    lb_un=Label(frame1,text='Username: ',font=('Helvetica',13, 'bold'),fg='Black')
    lb_un.grid(row=3,column=0)
    global e_u,enp,ecp
    e_u=Entry(frame1,text='Username',width=43,font=10)
    e_u.grid(row=3,column=1,columnspan=2)
    e_u.delete(0,END)
#    e_u.insert(0,"username@gmail.com")
    lb_un=Label(frame1,text='*You can use letters,numbers&periods',fg='Grey')
    lb_un.grid(row=3,column=3)
    lb_np=Label(frame1,text='Password: ',font=('Helvetica', 13, 'bold'),fg='Black')
    lb_np.grid(row=4,column=0)
    enp=Entry(frame1,width=25,font=10,show='*')
    enp.grid(row=4,column=1,columnspan=1)
    lb_cp=Label(frame1,text='Confirm Password: ',font=('Helvetica', 13, 'bold'),fg='Black')
    lb_cp.grid(row=4,column=2)
    ecp=Entry(frame1,width=25,font=10,show='*')
    ecp.grid(row=4,column=3,padx=0,pady=10)
    def un_hide2():
        bt_uh=Button(frame1,image=unhide,width=20,height=20,command=b_hide2)
        bt_uh.grid(row=4,column=4,padx=10)
        enp.config(show="")
        ecp.config(show="")
    def b_hide2():
        bt_h=Button(frame1,image=hide,width=20,height=20,command=un_hide2)
        bt_h.grid(row=4,column=4,padx=10)
        enp.config(show="*")
        ecp.config(show="*")
    b_hide2() 
    b_next=Button(frame1,text='Next',bg='Blue',font=7,fg='White',command=tocheck)
    b_next.grid(row=6,column=3,padx=10,pady=10)
    img_lab=Label(frame1,image=my_img)
    img_lab.grid(row=1,column=6,rowspan=5)
    img_lab2=Label(frame1,image=g_img)
    img_lab2.grid(row=0,column=0,columnspan=4)
    b_si=Button(frame1,text='Sign in instead',font=7,bg='White',fg='Blue',command=top.destroy)
    b_si.grid(row=6,column=1,padx=10,pady=15)
def un_hide():
    bt_uh=Button(frame,image=unhide,width=20,height=20,command=b_hide)
    bt_uh.grid(row=3,column=3)
    ep.config(show="")
def b_hide():
    bt_h=Button(frame,image=hide,width=20,height=20,command=un_hide)
    bt_h.grid(row=3,column=3)
    ep.config(show="*")
frame=LabelFrame(root,text='SIGN IN',font=('Helvetica', 15, 'bold'),border=7,padx=50,pady=50)
frame.pack(padx=15,pady=15)
img_lab1=Label(frame,image=gl_img)
img_lab1.grid(row=0,column=2,columnspan=2)
lb_t=Label(frame,text='Use Your Google Account',font= 20)
lb_t.grid(row=1,column=2)
lb_e=Label(frame,text='Email',font=('Helvetica',13, 'bold'),fg='Blue')
lb_e.grid(row=2,column=1)
e=Entry(frame,width=30,font=10)
e.grid(row=2,column=2,padx=10,pady=10)
lb_p=Label(frame,text='Password',font=('Helvetica', 13, 'bold'),fg='Blue')
lb_p.grid(row=3,column=1)
ep=Entry(frame,width=30,font=10,show='*')
ep.grid(row=3,column=2,padx=10,pady=10)
b_hide()
b_next=Button(frame,text='Next',bg='Blue',font=7,fg='White',command=pop_up)
b_next.grid(row=7,column=4,padx=10,pady=10)
b_new=Button(frame,text='Create new account',font=7,bg='White',fg='Blue',command=newwin)
b_new.grid(row=7,column=1,padx=10,pady=15)
b_fp=Button(frame,text='Forgot password?',font=7,bg='White',fg='Blue',command=pop_u)
b_fp.grid(row=7,column=2,padx=10,pady=15)

root.mainloop()
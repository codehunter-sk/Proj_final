from tkinter import *
from tkinter import messagebox
from Attendance import attendpage, myconn
from ViewPart import viewpartpage
from AddPart import addpartpage
from Adduser import adduserpage
from Modifyuser import modifypage
from Addevent import addeventpage
import main as m
bgcolour='#074463'

def cnx():
    global connection , cursor, ds
    connection = myconn.myconn()
    cursor = connection.cursor()
    # cursor.execute("SET TRANSACTION ISOLATION LEVEL READ COMMITTED")
    cursor.execute('use eventide04')
    ds=myconn.ds

def exit_app():
    op=messagebox.askyesno('Exit','Do you really want to exit?')
    if op>0:
        root.destroy()
        m.main()
def attendance_upload():
#--------------attendance frame-----------------------
    # att_f=LabelFrame(root,bd=10,relief=GROOVE,text='Update Attendance',font=('times new roman ',15 ,'bold'),fg='gold',bg=bgcolour)
    # att_f.place(x=0,y=250,relwidth=1,height=350)
    root.destroy()
    attendpage.main(userID)
def view_part():
#--------------view participants-----------------------
    # viewpart_f=LabelFrame(root,bd=10,relief=GROOVE,text='List Of Participants',font=('times new roman ',15 ,'bold'),fg='gold',bg=bgcolour)
    # viewpart_f.place(x=0,y=250,relwidth=1,height=350)
    # scroly=Scrollbar(viewpart_f,orient=VERTICAL)
    # txtarea=Text(viewpart_f,yscrollcommand=scroly.set)
    # scroly.pack(side=RIGHT,fill=Y)
    # scroly.config(command=txtarea.yview)
    # txtarea.pack(fill=BOTH,expand=1)
    # for i in range (1,10000):
    #     txtarea.insert(END,str(i))
    root.destroy()
    viewpartpage.main(userID)
def add_event():
#--------------add event-----------------------
    addevent_f=LabelFrame(root,bd=10,relief=GROOVE,text='New Event',font=('times new roman ',15 ,'bold'),fg='gold',bg=bgcolour)
    addevent_f.place(x=0,y=250,relwidth=1,height=350)
    addeventpage.evefr(root,cursor,bgcolour)

def add_user():
#--------------add new user-----------------------
    adduser_f=LabelFrame(root,bd=10,relief=GROOVE,text='New User',font=('times new roman ',15 ,'bold'),fg='gold',bg=bgcolour)
    adduser_f.place(x=0,y=250,relwidth=1,height=350)
    # root.destroy()
    # adduserpage.main(userID)
    adduserpage.loginfr(root,cursor,bgcolour)


def mod_user():
#--------------modify user role-----------------------
    moduser_f=LabelFrame(root,bd=10,relief=GROOVE,text='Modify user role',font=('times new roman ',15 ,'bold'),fg='gold',bg=bgcolour)
    moduser_f.place(x=0,y=250,relwidth=1,height=350)
    modifypage.main(root,moduser_f,userID)

def add_part():
#--------------add new participants-----------------------
    addpart_f=LabelFrame(root,bd=10,relief=GROOVE,text='Add participants',font=('times new roman ',15 ,'bold'),fg='gold',bg=bgcolour)
    addpart_f.place(x=0,y=250,relwidth=1,height=350)
    # root.destroy()
    addpartpage.add_part_func(ds,root,cursor,bgcolour)


def eventide(username,admin):
    global root

    root=Tk()
    root.geometry('1200x600')
    root.resizable(FALSE,FALSE)
    root.title('EVENTIDE')

    Frame(root,bg=bgcolour,height=600,width=1200).place(x=0,y=0)
    title=Label(root,text='EVENTIDE',bd=12,relief=GROOVE,bg=bgcolour,fg='white',font=('times new roman',30,'bold')).pack(fill=X)


#--------------user frame-------------------
    usr_f=Frame(root,bd=10,relief=GROOVE,bg=bgcolour)
    usr_f.place(x=0,y=71,relwidth=1,height=80)
    wlcstr="Logged in as "+username
    if(admin=='y'):
        wlcstr+=" (admin)"
    else:
        wlcstr+=" (regular)"
#-------------------------------------------------

#----------------button frame-------------------------
    btn_f=Frame(root,bd=10,relief=GROOVE,bg=bgcolour)
    btn_f.place(x=0,y=150,relwidth=1,height=100)
    Label(usr_f,text=wlcstr,font=('times new roman',24,'bold'),bg=bgcolour,fg='white').grid(row=2,column=0,padx=20,pady=10,sticky='w')
    Button(btn_f,cursor='hand2',text='Update Attendance',bg='cadetblue',state=NORMAL,command=attendance_upload,fg='white',pady=15,width=17,bd=2,font='arial 15 bold').grid(row=0,column=2,padx=5,pady=5)
    Button(btn_f,cursor='hand2',text='View Participants',bg='cadetblue',fg='white',state=NORMAL,command=view_part,pady=15,width=15,bd=2,font='arial 15 bold').grid(row=0,column=3,padx=5,pady=5)
    add_eventbtn=Button(btn_f,cursor='hand2',text='Add Event',bg='cadetblue',fg='white',pady=15,command=add_event,state=NORMAL,width=10,bd=2,font='arial 15 bold')
    add_eventbtn.grid(row=0,column=4,padx=5,pady=5)
    add_userbtn=Button(btn_f,cursor='hand2',text='Add User',bg='cadetblue',fg='white',pady=15,command=add_user,state=NORMAL,width=9,bd=2,font='arial 15 bold')
    add_userbtn.grid(row=0,column=5,padx=5,pady=5)
    mod_userbtn=Button(btn_f,cursor='hand2',text='Modify user role',bg='cadetblue',fg='white',command=mod_user,state=NORMAL,pady=15,width=14,bd=2,font='arial 15 bold')
    mod_userbtn.grid(row=0,column=6,padx=5,pady=5)
    add_partbtn=Button(btn_f,cursor='hand2',text='Add participants',bg='cadetblue',fg='white',command=add_part,state=NORMAL,pady=15,width=14,bd=2,font='arial 15 bold')
    add_partbtn.grid(row=0,column=7,padx=5,pady=5)

    if(admin!='y'):
        add_eventbtn.configure(state=DISABLED)
        add_userbtn.configure(state=DISABLED)
        mod_userbtn.configure(state=DISABLED)
        add_partbtn.configure(state=DISABLED)

    Button(btn_f,cursor='hand2',text='Logout',bg='cadetblue',fg='white',pady=15,width=8,state=NORMAL,bd=2,font='arial 15 bold',command=exit_app).grid(row=0,column=8,padx=5,pady=5)
    root.mainloop()
#-----------------------------------------------------

def main(id):
    global userID
    userID=id
    cnx()
    cursor.execute(f'select username, admin from user where userid = {id}');
    user=cursor.fetchall()
    print(user)
    eventide(user[0][0],user[0][1])

if __name__=='__main__':
    main('101')

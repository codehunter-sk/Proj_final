from tkinter import *
import tkinter as tk
from tkinter import messagebox as msgbox
from Attendance import myconn
from Dashboard import dashpage as dpg
bgcolour="#074463"

connection = myconn.myconn()
cursor = connection.cursor()
cursor.execute('use eventide04')

def clear():
    for item in root.winfo_children():
      item.destroy()

def update_admin(userid,status):

    cursor.execute('''update user set admin="{}" where userid={}'''.format(status,userid))
    msgbox.showinfo(title='Alert',message='Changes applied succesfully')
    if(int(userid)==int(org_userid)):
        window.destroy()
        return dpg.main(org_userid)

    clear()
    main(window,root,org_userid)

def fetch_data(userid):
    
    try:
        cursor.execute("Select * from user where userid={}".format(userid))
        user_det=cursor.fetchall()

    except:
        msgbox.showerror(title = 'Invalid UserID' , message = 'User ID doesnt exist')
        clear()
        main(window,root,org_userid)

    if(user_det==[]):
        msgbox.showerror(title = 'Invalid UserID' , message = 'User ID doesnt exist')
        clear()
        main(window,root,org_userid)

    if(int(userid)==int(org_userid)):

        ans=msgbox.askquestion("Same ID", "Are you sure you want to change your own admin status ")
        if ans=="no":
            clear()
            main(window,root,org_userid)
        else:
            cursor.execute('''select count(admin) from user where admin="y"''')
            if(cursor.fetchall()[0][0]==1):
                msgbox.showinfo("Last Admin", "Last admin!Pls make someone else admin")
                clear()
                main(window,root,org_userid)

    clear()
    

    userid_label = tk.Label(root,text="User ID ",font=('times new roman',20,'bold'),bg=bgcolour,fg="white")
    username_label = tk.Label(root,text="Username",font=('times new roman',20,'bold'),bg=bgcolour,fg="white")
    admin_label = tk.Label(root,text="Admin Status",font=('times new roman',20,'bold'),bg=bgcolour,fg="white")

    for i in [80,120,160]:
        tk.Label(root,text=":",font=('times new roman',20,'bold'),bg=bgcolour,fg="white").place(x=530,y=i)

    userid_value = tk.Label(root,text=user_det[0][1],font=('times new roman',20,'bold'),bg=bgcolour,fg="white")
    username_value = tk.Label(root,text=user_det[0][0],font=('times new roman',20,'bold'),bg=bgcolour,fg="white")

    admin_status = tk.StringVar()
    admin_status.set(user_det[0][2])
    admin_radiobutton = tk.Radiobutton(root, text="Admin", variable=admin_status, value="y",font=('times new roman',20,'bold'),bg=bgcolour,fg="white",selectcolor=bgcolour)
    nonadmin_radiobutton = tk.Radiobutton(root, text="Non-Admin", variable=admin_status, value="n",font=('times new roman',20,'bold'),bg=bgcolour,fg="white",selectcolor=bgcolour)

    userid_label.place(x=350,y=80)
    username_label.place(x=350,y=120)
    admin_label.place(x=350,y=160)
    userid_value.place(x=550,y=80)
    username_value.place(x=550,y=120)
    admin_radiobutton.place(x=550,y=160)
    nonadmin_radiobutton.place(x=670,y=160)

    modify_but=tk.Button(root,text='Apply Changes',bg='cadetblue',command=lambda:update_admin(user_det[0][1],admin_status.get()),fg='white',pady=10,state=NORMAL,width=12,bd=2,font='arial 12 bold').place(x=500,y=220)
    window.mainloop()


def main(mainwin,parent,uid):
    global root,window,org_userid
    root=parent
    window=mainwin
    org_userid=uid
    userid_label=tk.Label(root,text="User ID :",font=('times new roman',20,'bold'),bg=bgcolour,fg="white").place(x=400,y=80)
    userid_entry=tk.Entry(root,font=('times new roman',24,'bold'),width=10,relief=SUNKEN)
    userid_entry.place(x=520,y=80)

    modify_but=tk.Button(root,text='Modify User',bg='cadetblue',command=lambda:fetch_data(userid_entry.get()),fg='white',pady=10,state=NORMAL,width=10,bd=2,font='arial 12 bold').place(x=500,y=140)

    window.mainloop()

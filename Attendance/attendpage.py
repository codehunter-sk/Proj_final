from tkinter import *
from . import myconn
from Dashboard import dashpage
from mysql.connector import errors

bgcolour='#074463'
pagestate=1
currEvent=0

def cnx():
    global connection , cursor
    connection = myconn.myconn()
    cursor = connection.cursor()
    # cursor.execute("SET TRANSACTION ISOLATION LEVEL READ COMMITTED")
    cursor.execute('use eventide04')

def rootw():
    global root
    root = Tk()
    root.title('Eventide')
    root.geometry('1200x600')
    root.resizable(0,0)

def Delpage(content=''):
    global pagestate
    pagestate=3
    listbox.delete(0,END)
    delbutton.destroy()
    headlabel.configure(text='Remove participant')
    txtinput01.focus_set()

    cursor.execute(f"select pID, pname, college, city from participants where eventid = {currEvent} and attendance = '1' and pname like '%{content}%'")
    partList=cursor.fetchall()
    print('1',partList)
    partNumb=len(partList)

    partind=0
    for partind in range(partNumb):
        listbox.insert(END, ' '*5+str(partList[partind][0])+' :- '+myconn.addspace(partList[partind][1],25)+myconn.addspace(partList[partind][2],100)+myconn.addspace(partList[partind][3],30))
        if(partind%2):
            listbox.itemconfig(partind, bg='black')
    # print(partind)
    while(partind<12):
        listbox.insert(END, '')
        if(partind%2):
            listbox.itemconfig(partind, bg='black')
        partind+=1



def Atdpage(eid,content=''):
    global pagestate, currEvent, delbutton
    pagestate=2
    listbox.delete(0,END)
    headlabel.configure(text='Select participant')
    findlabel.configure(text='Find participant:')
    txtinput01.focus_set()

    # frame2.destroy()
    # Label(frame1, text = str(eid)+': '+ename, bg='white', fg='black').place(relx = 0.5, rely = 0.5, anchor = 'center')

    currEvent=eid

    cursor.execute(f"select pID, pname, college, city  from participants where eventid = {eid} and attendance = '0' and pname like '%{content}%'")
    partList=cursor.fetchall()
    print('he')
    print(partList)
    partNumb=len(partList)

    # try:

    # _=0
    # while(_<5):
    #     cursor.execute(f"select pID, pname, college, city  from participants where eventid = {eid} and attendance = '0'")
    #     partList=cursor.fetchall()
    #     _+=1

    # except errors.InternalError:
    #     partList=cursor.fetchall()
    # print(partList)
    # partNumb=len(partList)



    partind=0
    for partind in range(partNumb):
        listbox.insert(END, ' '*5+str(partList[partind][0])+' :- '+myconn.addspace(partList[partind][1],25)+myconn.addspace(partList[partind][2],100)+myconn.addspace(partList[partind][3],30))
        if(partind%2):
            listbox.itemconfig(partind, bg='black')
    # print(partind)
    while(partind<12):
        listbox.insert(END, '')
        if(partind%2):
            listbox.itemconfig(partind, bg='black')
        partind+=1


    delbutton=Button(frame1,cursor='hand2',text='Remove participant',bd=3, bg='cadetblue', fg='white', command=Delpage, font=('helvetica',12))
    delbutton.place(x=1020,y=25)



    # listbox.selection_clear(0,END)

def eveListPage(uid,content=''):

    try:
        delbutton.destroy()
        headlabel.configure(text='Select event')
    except:
        pass
    listbox.delete(0,END)
    findlabel.configure(text='Find event:')
    txtinput01.focus_set()

    cursor.execute(f"select c_v.eventid, eventname from c_v, events where userid = {uid} and c_v.eventid = events.eventID and eventname like '%{content}%'");
    eventList=cursor.fetchall()
    numbOfEvents=len(eventList)


    eveind=0
    for eveind in range(numbOfEvents):
        listbox.insert(END, ' '*5+str(eventList[eveind][0])+' :- '+myconn.addspace(eventList[eveind][1],50))
        if(eveind%2):
            listbox.itemconfig(eveind, bg='black')

    # print(eveind)
    while(eveind<12):
        listbox.insert(END, '')
        if(eveind%2):
            listbox.itemconfig(eveind, bg='black')
        eveind+=1


def wind1(uid):
    global frame1, frame2, frame15, listbox, backbutton, headlabel, findlabel, txtinput01

    frame1 = Frame(root, height=100, width=1200,bd=10,relief=GROOVE, bg=bgcolour)
    frame1.grid(row=1, column=0)
    # btn_f=Frame(root,bd=10,relief=GROOVE,bg=bgcolour)
    # btn_f.place(x=0,y=150,relwidth=1,height=100)

    Label(root,text='EVENTIDE',bg=bgcolour,fg='white',font=('times new roman',36,'bold')).place(x=450,y=20)

    frame15=Frame(root, height=80, width=1200,bd=10,relief=GROOVE, bg=bgcolour)
    frame15.grid(row=2, column=0)
    # frame15.grid_propagate(0)

    headlabel=Label(frame15, text='Select event', font=('consolas', 22,'underline'),bg=bgcolour,fg='white',bd=1)
    headlabel.place(x = 10, y = 10)

    findlabel=Label(frame15, text='Find event:',font=('consolas',18),bg=bgcolour,fg='white')
    findlabel.place(x = 520, y=14)

    txtinput01=Text(frame15, height = 1, width = 15, font=('consolas',18))
    txtinput01.place(x = 770, y = 15)
    # txtinput01.focus_set()

    def txtinp_dyna(event):
        content=txtinput01.get('1.0','end-1c')
        if(pagestate==1):
            eveListPage(uid,content)
        elif(pagestate==2):
            Atdpage(currEvent,content)
        elif(pagestate==3):
            Delpage(content)



    txtinput01.bind("<KeyRelease>",txtinp_dyna)

    frame2 = Frame(root, height=420, width=1200, bg=bgcolour)
    frame2.grid(row=3, column=0)
    frame2.grid_propagate(0)


    listbox = Listbox(frame2, font=('consolas', 22), bg = '#272821', fg = '#66d9ee', width = 73, height = 11, borderwidth = 6, cursor = 'hand2')
    # listbox.pack(side=LEFT, fill=BOTH)
    listbox.grid(row=0,column=0,)

    vscrollbar = Scrollbar(frame2)
    # vscrollbar.pack(side=RIGHT, fill=Y)
    vscrollbar.grid(row=0,column=1,sticky='ns')

    hscrollbar = Scrollbar(frame2, orient=HORIZONTAL)
    # hscrollbar.pack(side=BOTTOM, anchor='s', fill=X)
    hscrollbar.grid(row=1,column=0,sticky='ew')

    listbox.configure(yscrollcommand=vscrollbar.set, xscrollcommand=hscrollbar.set)
    vscrollbar.configure(command=listbox.yview)
    hscrollbar.configure(command=listbox.xview)

    def row_selected(event):
        eve = listbox.get(listbox.curselection()).strip().split(':-')
        if(eve[0]):
            txtinput01.delete('1.0',END)
            if(pagestate==1):
                Atdpage(int(eve[0]))#,eve[1])
            elif(pagestate==2):
                cursor.execute(f"update participants set attendance = 1 where eventid = {currEvent} and pID = {eve[0]}")
                # .flush()
                # connection.commit()
                # cursor.execute(f"select * from participants")
                Atdpage(currEvent)#,eve[1])
            elif(pagestate==3):
                cursor.execute(f"update participants set attendance = 0 where eventid = {currEvent} and pID = {eve[0]}")
                # connection.commit()
                Delpage()


    listbox.bind('<<ListboxSelect>>', row_selected)

    # listbox.bind()

    eveListPage(uid)


    # for eveind in range(40):
    #     listbox.insert(END, ' '*5+str(eveind)+' :- ')
    #     if(eveind%2):
    #         listbox.itemconfig(eveind, bg='black')

    def goback():
        global pagestate
        txtinput01.delete('1.0',END)
        listbox.delete(0,END)
        if(pagestate==1):
            root.destroy()
            dashpage.main(uid)
        elif(pagestate==2):
            pagestate=1
            eveListPage(uid)
        elif(pagestate==3):
            pagestate=2
            Atdpage(currEvent)

        # print('hee')
        # frame2.destroy()

    backbutton=Button(frame1,cursor='hand2',text='Back',bd=3, bg='cadetblue', fg='white',command=goback,font=('helvetica',12))
    backbutton.place(x=10,y=25)


        

    # for eid,ename in eventList:
    #     Button(frame2, cursor = 'hand2', text = ename+' '+str(eid), bd = 2, command = lambda : Atdpage(eid), background = 'lightblue', width = 24, height = 14).pack()



    root.mainloop()


def main(uid):
    rootw()
    cnx()
    wind1(uid)

if __name__ == '__main__':
    main(101)
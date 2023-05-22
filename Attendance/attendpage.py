from tkinter import *
from . import myconn
from Dashboard import dashpage

bgcolour='#074463'
pagestate=1
currEvent=0

def cnx():
    global connection , cursor
    connection = myconn.myconn()
    cursor = connection.cursor()
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

    currEvent=eid

    cursor.execute(f"select pID, pname, college, city  from participants where eventid = {eid} and attendance = '0' and pname like '%{content}%'")
    partList=cursor.fetchall()
    print('he')
    print(partList)
    partNumb=len(partList)

    partind=0
    for partind in range(partNumb):
        listbox.insert(END, ' '*5+str(partList[partind][0])+' :- '+myconn.addspace(partList[partind][1],25)+myconn.addspace(partList[partind][2],100)+myconn.addspace(partList[partind][3],30))
        if(partind%2):
            listbox.itemconfig(partind, bg='black')
    while(partind<12):
        listbox.insert(END, '')
        if(partind%2):
            listbox.itemconfig(partind, bg='black')
        partind+=1


    delbutton=Button(frame1,cursor='hand2',text='Remove participant',bd=3, bg='cadetblue', fg='white', command=Delpage, font=('helvetica',12))
    delbutton.place(x=1020,y=25)


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

    while(eveind<12):
        listbox.insert(END, '')
        if(eveind%2):
            listbox.itemconfig(eveind, bg='black')
        eveind+=1


def wind1(uid):
    global frame1, frame2, frame15, listbox, backbutton, headlabel, findlabel, txtinput01

    frame1 = Frame(root, height=100, width=1200,bd=10,relief=GROOVE, bg=bgcolour)
    frame1.grid(row=1, column=0)

    Label(root,text='EVENTIDE',bg=bgcolour,fg='white',font=('times new roman',36,'bold')).place(x=450,y=20)

    frame15=Frame(root, height=80, width=1200,bd=10,relief=GROOVE, bg=bgcolour)
    frame15.grid(row=2, column=0)

    headlabel=Label(frame15, text='Select event', font=('consolas', 22,'underline'),bg=bgcolour,fg='white',bd=1)
    headlabel.place(x = 10, y = 10)

    findlabel=Label(frame15, text='Find event:',font=('consolas',18),bg=bgcolour,fg='white')
    findlabel.place(x = 520, y=14)

    txtinput01=Text(frame15, height = 1, width = 15, font=('consolas',18))
    txtinput01.place(x = 770, y = 15)

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
    listbox.grid(row=0,column=0,)

    vscrollbar = Scrollbar(frame2)
    vscrollbar.grid(row=0,column=1,sticky='ns')

    hscrollbar = Scrollbar(frame2, orient=HORIZONTAL)
    hscrollbar.grid(row=1,column=0,sticky='ew')

    listbox.configure(yscrollcommand=vscrollbar.set, xscrollcommand=hscrollbar.set)
    vscrollbar.configure(command=listbox.yview)
    hscrollbar.configure(command=listbox.xview)

    def row_selected(event):
        eve = listbox.get(listbox.curselection()).strip().split(':-')
        if(eve[0]):
            txtinput01.delete('1.0',END)
            if(pagestate==1):
                Atdpage(int(eve[0]))
            elif(pagestate==2):
                cursor.execute(f"update participants set attendance = 1 where eventid = {currEvent} and pID = {eve[0]}")
                Atdpage(currEvent)
            elif(pagestate==3):
                cursor.execute(f"update participants set attendance = 0 where eventid = {currEvent} and pID = {eve[0]}")
                Delpage()
    listbox.bind('<<ListboxSelect>>', row_selected)

    eveListPage(uid)


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



    backbutton=Button(frame1,cursor='hand2',text='Back',bd=3, bg='cadetblue', fg='white',command=goback,font=('helvetica',12))
    backbutton.place(x=10,y=25)


    root.mainloop()


def main(uid):
    rootw()
    cnx()
    wind1(uid)

if __name__ == '__main__':
    main(101)
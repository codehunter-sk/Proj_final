from tkinter import *
from Attendance import myconn
from tkinter import ttk
from Dashboard import dashpage
import csv


def cnx():
    global connection, cursor, ds
    connection = myconn.myconn()
    cursor = connection.cursor()
    cursor.execute('use eventide04')
    ds = myconn.ds


def rootw():
    global root
    root = Tk()
    root.title('Eventide')
    root.geometry('1200x600')
    root.resizable(0,0)

def show_parts(name='',eid='',id='',city='',college=''):
    try:
        partWindow.delete('1.0',END)
    except:
        pass

    _1=myconn.addspace('NAME',30)
    _2=myconn.addspace('EMAIL',40)
    _3=myconn.addspace('MOBILE',10)
    _4=myconn.addspace('EVENT ID',30)
    _5=myconn.addspace('ID',10)
    _6=myconn.addspace('CITY',30)
    _7=myconn.addspace('COLLEGE',100)
    partWindow.insert(END,'|  '+_1+'| '+_2+'| '+_3+'| '+_4+'| '+_5+'| '+_6+'| '+_7+'|\n')
    partWindow.insert(END,('-'*264)+'\n')

    cursor.execute(f"select * from participants where pname like '%{name}%' and eventid like '%{eid}%' and pID like '%{id}%' and city like '%{city}%' and college like '%{college}%'")
    partis=cursor.fetchall()

    for parti in partis:
        _1=myconn.addspace(parti[0],30)
        _2=myconn.addspace(parti[1],40)
        _3=myconn.addspace(parti[2],10)
        _4=myconn.addspace(parti[3],30)
        _5=myconn.addspace(parti[4],10)
        _6=myconn.addspace(parti[5],30)
        _7=myconn.addspace(parti[6],100)
        partWindow.insert(END,'|  '+_1+'| '+_2+'| '+_3+'| '+_4+'| '+_5+'| '+_6+'| '+_7+'|\n')
        partWindow.insert(END,('-'*264)+'\n')



def wind1(uid):
    global frame1, frame2, partWindow

    C14=('consolas',14)

    frame1 = Frame(root, height=100, width=1200, bg='black')
    frame1.grid(row=1, column=0)

    Label(root,text='EVENTIDE',bg='black',fg='white',font=('times new roman',36,'bold')).place(x=450,y=20)

    frame2 = Frame(root, height=500, width=1200, bg='maroon')
    frame2.grid(row=3, column=0)

    partWindow = Text(frame2, bd=2, wrap='none', bg='#DCD094', fg='#000000', cursor='hand2', width='105', height='28',
                      font=('Courier', 10), insertbackground='#000000', insertborderwidth=10)
    partWindow.place(x=10, y=10)

    collWscrollbary = Scrollbar(frame2, orient="vertical", command=partWindow.yview)
    collWscrollbary.place(x=860, y=10, height=456)

    collWscrollbarx = Scrollbar(frame2, orient="horizontal", command=partWindow.xview)
    collWscrollbarx.place(x=10, y=470, width=847)
    partWindow.configure(yscrollcommand=collWscrollbary.set, xscrollcommand=collWscrollbarx.set)

    namelabel=Label(frame2,text='Name: ', font=C14, bg='#dcd094')
    namelabel.place(x = 900, y = 14)
    nameinput=Text(frame2, height = 1, width = 22, font=C14)
    nameinput.place(x = 900, y = 50)

    eidlabel=Label(frame2,text='Event ID: ', font=C14, bg='#dcd094')
    eidlabel.place(x = 900, y = 104)
    eidinput=Text(frame2, height = 1, width = 22, font=C14)
    eidinput.place(x = 900, y = 140)

    idlabel=Label(frame2,text='ID: ', font=C14, bg='#dcd094')
    idlabel.place(x = 900, y = 194)
    idinput=Text(frame2, height = 1, width = 22, font=C14)
    idinput.place(x = 900, y = 230)

    citylabel=Label(frame2,text='City: ', font=C14, bg='#dcd094')
    citylabel.place(x = 900, y = 284)

    cursor.execute('select distinct city from participants');
    cities=['']
    for i in cursor.fetchall():
        cities.append(i[0])

    selected_city=StringVar()
    city_combo=ttk.Combobox(frame2, textvariable=selected_city,state='readonly',values=cities,font=C14)
    city_combo.place(x = 900, y = 320)

    clglabel=Label(frame2,text='College: ', font=C14, bg='#dcd094')
    clglabel.place(x = 900, y = 374)

    cursor.execute('select distinct college from participants');
    clgs=['']
    for i in cursor.fetchall():
        clgs.append(i[0])

    selected_clg=StringVar()
    clg_combo=ttk.Combobox(frame2, textvariable=selected_clg,state='readonly',values=clgs,font=C14)
    clg_combo.place(x = 900, y = 410)

    def dyna(event):
        name=nameinput.get('1.0','end-1c')
        eid=eidinput.get('1.0','end-1c')
        id=idinput.get('1.0','end-1c')
        city=selected_city.get()
        clg=selected_clg.get()
        show_parts(name,eid,id,city,clg)

    nameinput.bind("<KeyRelease>",dyna)
    eidinput.bind("<KeyRelease>",dyna)
    idinput.bind("<KeyRelease>",dyna)
    city_combo.bind("<<ComboboxSelected>>",dyna)
    clg_combo.bind("<<ComboboxSelected>>",dyna)

    show_parts()


    def goback():
        root.destroy()
        dashpage.main(uid)


    backbutton=Button(frame1,cursor='hand2',text='Back',bd=3, bg='white', fg='black',command=goback,font=('helvetica',12))
    backbutton.place(x=10, y=35)

    root.mainloop()


def main(uid):
    rootw()
    cnx()
    wind1(uid)


if __name__ == '__main__':
    main(101)

from tkinter import *
from tkinter import filedialog as fd
from tkinter import messagebox as msgbox
import csv

def get_file_name():
    file_name = fd.askopenfilename(initialdir = "/", title = "Select file",filetypes = (("CSV Files","*.csv"),))
    entry_csv.delete(0,END)
    entry_csv.insert(0,file_name)


def upload_csvfile(ds,cursor,file_name = None):
    try:
        with open(file_name) as file:
            csv_reader=csv.reader(file, delimiter=',')
            line_count=0
            for row in csv_reader:
                try:
                    print(tuple(row))
                    if(line_count):
                        cursor.execute('insert into participants values (%s,%s,%s,%s,%s,%s,%s,%s)',tuple(row))
                    line_count+=1
                except ds.IntegrityError:
                    pass
        msgbox.showinfo(title = 'Alert!' , message = f'Processed {line_count-1} rows')
    except FileNotFoundError:
        pass
    entry_csv.delete(0,END)


def add_part_func(ds,root,cursor,bgcolor):
    global entry_csv


    entry_csv = Entry(root, width=50, bg = '#d9dbde')
    entry_csv.place(x = 470, y =370,height = 20)

    csv_selectlbl = Label(root, bg = '#ffffff' ,font = ('Arial',14), text="Select CSV")
    csv_selectlbl.place(x = 320,y = 367)

    csv_browsebtn = Button(root, text ="Browse...",  cursor = 'hand2',width=10, command = lambda: get_file_name())
    csv_browsebtn.place(x = 810,y = 367)

    csv_uploadbtn = Button(root, text ="Upload", cursor = 'hand2', command = lambda: upload_csvfile(ds,cursor,entry_csv.get()), width=10)
    csv_uploadbtn.place( x = 470, y = 420)

    csv_cancelbtn = Button(root, text ="Reset",  cursor = 'hand2', command = lambda: entry_csv.delete(0,END), width=10)
    csv_cancelbtn.place( x = 550, y = 420)


    root.mainloop()


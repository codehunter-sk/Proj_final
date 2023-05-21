from tkinter import *

def login(cursor,event_entry, users_entry,login_status_label):
    # Retrieve the entered username and password
    eventname = event_entry.get()
    inputs = users_entry.get().split(",")
    print(inputs)

    if(eventname and inputs[0]):
        cursor.execute("select eventname from events")
        events=cursor.fetchall()
        exists=0
        for event in events:
            if(eventname==event[0]):
                exists=1
                break
        if(not exists):
            try:
                # Execute the SQL query to check the credentials
                query = "INSERT INTO events (eventname) VALUES (%s)"
                cursor.execute(query, (eventname,))

                q1 = "select eventID from events where eventname =%s"
                cursor.execute(q1,(eventname,))

                result = cursor.fetchone()
                print(result)
                val = result[0]
                print(val)

                cursor.execute("select userID from user")
                users=cursor.fetchall()
                users=[user[0] for user in users]
                print(users,type(users))
                print('hi')

                for i in inputs:
                    if int(i) in users:
                        q2 = "insert into c_v(userid, eventid) values(%s,%s)"
                        cursor.execute(q2, (i,val))
                if True:
                    login_status_label.config(text="entered successful!", fg="green")
                else:
                    login_status_label.config(text="error occured", fg="red")

                event_entry.delete(0,END)
                users_entry.delete(0,END)

            except Exception as error:
                print("Error while connecting to the database:", error)
                login_status_label.config(text="Database error", fg="red")
        else:
            login_status_label.config(text="Event already exists!", fg="black", bg='lightblue')
    else:
        login_status_label.config(text="Fill empty fields!", fg="black", bg='lightblue')

def evefr(root,cursor,bgcolour):

    login_frame = Frame(root, width=600, height=700, bg=bgcolour)
    login_frame.place(x=100,y=300)

    event_label = Label(login_frame, text="EventName:", font=("Arial", 16),bg="white")
    event_label.grid(row=0, column=0, sticky="w", padx=20, pady=20)

    event_entry = Entry(login_frame, font=("Arial", 16))
    event_entry.grid(row=0, column=1, padx=20, pady=20)

    users_label = Label(login_frame, text="User ID", font=("Arial", 16),bg="white")
    users_label.grid(row=1, column=0, sticky="w", padx=20, pady=20)

    users_entry = Entry(login_frame, font=("Arial", 16))
    users_entry.grid(row=1, column=1, padx=20, pady=20)

    login_status_label = Label(root, text="", fg="black", font=("Arial", 14), bg=bgcolour)
    login_status_label.place(x=900,y=390)

    login_button = Button(root,cursor='hand2', text="Add Event", command=lambda:login(cursor,event_entry, users_entry,login_status_label), font=("Arial", 16),bg="light blue")
    login_button.place(x=700,y=385)


from tkinter import *


def login(cursor, username_entry, password_entry, admin_entry, login_status_label):
    username = username_entry.get()
    password = password_entry.get()
    admin = admin_entry.get()
    if username and password and admin:
        cursor.execute("select username from user")
        users = cursor.fetchall()
        exists = 0
        for user in users:
            if username == user[0]:
                exists = 1
                break
        if not exists:
            if admin == 'y' or admin == 'n':
                try:
                    query = "INSERT INTO user (username,admin, password) VALUES (%s,%s,%s)"

                    cursor.execute(query, (username, admin, password))

                    if True:
                        login_status_label.config(text="entered successful!", fg="green")
                        username_entry.delete(0, END)
                        password_entry.delete(0, END)
                        admin_entry.delete(0, END)
                    else:
                        login_status_label.config(text="error occured!", fg="red")

                except Exception as error:
                    print("Error while connecting to the database:", error)
                    login_status_label.config(text="Database error", fg="black", bg='lightblue')
            else:
                login_status_label.config(text="Admin should be y or n!", fg="black", bg='lightblue')
        else:
            login_status_label.config(text="Username already exists!", fg="black", bg='lightblue')
    else:
        login_status_label.config(text="Fill empty fields!", fg="black", bg='lightblue')


def loginfr(root, cursor, bgcolour):
    login_frame = Frame(root, width=600, height=700, bg=bgcolour)
    login_frame.place(x=100, y=300)

    username_label = Label(login_frame, text="Username:", font=("Arial", 16), bg="white")
    username_label.grid(row=0, column=0, sticky="w", padx=20, pady=20)

    username_entry = Entry(login_frame, font=("Arial", 16))
    username_entry.grid(row=0, column=1, padx=20, pady=20)

    password_label = Label(login_frame, text="Password:", font=("Arial", 16), bg="white")
    password_label.grid(row=1, column=0, sticky="w", padx=20, pady=20)

    password_entry = Entry(login_frame, show="*", font=("Arial", 16))
    password_entry.grid(row=1, column=1, padx=20, pady=20)

    admin_label = Label(login_frame, text="Admin: (y/n)", font=("Arial", 16), bg="white")
    admin_label.grid(row=2, column=0, sticky="w", padx=20, pady=20)

    admin_entry = Entry(login_frame, font=("Arial", 16))
    admin_entry.grid(row=2, column=1, padx=20, pady=20)

    login_status_label = Label(root, text="", fg="black", font=("Arial", 14), bg=bgcolour)
    login_status_label.place(x=900, y=390)

    login_button = Button(root, cursor='hand2', text="Add User",
                          command=lambda: login(cursor, username_entry, password_entry, admin_entry,
                                                login_status_label), font=("Arial", 16), bg="light blue")
    login_button.place(x=700, y=385)

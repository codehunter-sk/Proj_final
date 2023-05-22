from Attendance import myconn
import tkinter as tk
from tkinter import messagebox as msgbox
from PIL import Image, ImageTk

from Dashboard import dashpage as dpg

connection = myconn.myconn()
cursor = connection.cursor()
cursor.execute('use eventide04')


def main():
    global entry_username, entry_password, window
    window = tk.Tk()
    window.title('Eventide')
    window.geometry('1200x600')

    bg_img = ImageTk.PhotoImage(Image.open('images/bg_login.png'))
    tk.Label(window, image=bg_img, bd=0).place(x=0, y=0)

    tk.Label(window, text='   EVENTIDE   ', bd=12, relief=tk.GROOVE, bg='#074463', fg='white',
             font=('times new roman', 30, 'bold')).pack(padx=20, pady=20)

    frame = tk.Frame(window, bg='#074463')
    frame.pack(padx=20, pady=20)

    label_username = tk.Label(frame, text="Username:", bg='#074463', fg='white', font=("Arial", 14))
    label_username.pack(padx=10, pady=5)
    entry_username = tk.Entry(frame, font=("Arial", 14))
    entry_username.pack(padx=10, pady=5)

    label_password = tk.Label(frame, text="Password:", bg='#074463', fg='white', font=("Arial", 14))
    label_password.pack(padx=10, pady=5)
    entry_password = tk.Entry(frame, show="*", font=("Arial", 14))  # Show '*' instead of the actual password
    entry_password.pack(padx=10, pady=5)

    tk.Label(frame, text="", bg='#074463', fg='white', font=("Arial", 14)).pack(padx=10, pady=5)

    button_login = tk.Button(window, text="Login", command=login, font=("Arial", 14), bg='#074463', fg="white")
    button_login.pack(pady=10)

    window.mainloop()


def login():
    username = entry_username.get()
    password = entry_password.get()

    cursor.execute("Select username from user")
    user_arr = cursor.fetchall()
    cursor.execute("Select password from user")
    pwd_arr = cursor.fetchall()

    if (username,) in user_arr:
        if pwd_arr[user_arr.index((username,))] == (password,):
            window.destroy()
            cursor.execute(
                '''Select userid from user where username="{}"and password="{}"'''.format(username, password))
            userid = cursor.fetchall()
            return dpg.main(userid[0][0])
        else:
            msgbox.showerror(title='Invalid credentials', message='Invalid Password')
    else:
        msgbox.showerror(title='Invalid credentials', message='Invalid Username')


if __name__ == '__main__':
    main()

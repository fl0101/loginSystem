"""
Date: 02/18/2022
Author: Flaviane S. Nascimento
Desc.: Sistema de login com Tkinter
"""

from tkinter import *
from tkinter import ttk
from tkinter.messagebox import showinfo


def register():
    exec(open("Register.py").read())


def login():
    a = search_user(var1.get(), var2.get())
    if a is True:
        showinfo("Message", f"Successful login")

    elif len(var1.get()) == 0 or len(var2.get()) == 0:
        lb1["text"] = "Username*"
        lb2["text"] = "Password*"
        showinfo("Message", f"Required fields")

    else:
        showinfo("Message", f"Incorrect username or password")


def search_user(name, passwd):
    to_check = []

    try:
        with open('users.txt', 'r+', newline='') as arquivo:
            for separate in arquivo:
                separate = separate.strip()
                to_check.append(separate.split(","))

            for verify in to_check:
                verify_name = verify[0]
                verify_passwd = verify[1]
                if name == verify_name and passwd == verify_passwd:
                    return True

    except (Exception, ):
        pass


window = Tk()

# definindo o tamanho da janela
window.title("Login")
window.geometry("400x300+450+200")
window["bg"] = "white"

lb = Label(window, text="Login", bg="white", font=("Arial Bold", 20))
lb.place(x=160, y=15)

lb1 = Label(window, text="Username", bg="white", fg="gray", font=("Arial Bold", 15))
lb1.place(x=50, y=70)

# input Box
var1 = StringVar()
txt1 = Entry(window, width=20, textvariable=var1)
txt1.place(x=170, y=73)

lb2 = Label(window, text="Password", bg="white", fg="gray", font=("Arial Bold", 15))
lb2.place(x=50, y=120)

var2 = StringVar()
txt2 = Entry(window, width=20, textvariable=var2, show="*")
txt2.place(x=170, y=123)

btn1 = ttk.Button(window, text="Login", width=12, command=login)
btn1.place(x=80, y=175)

btn2 = ttk.Button(window, text="New user?", width=12, command=register)
btn2.place(x=200, y=175)

window.mainloop()

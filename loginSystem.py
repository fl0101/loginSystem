"""
Date: 02/18/2022
Author: Flaviane S. Nascimento
Desc.: Sistema de login com Tkinter
"""

from tkinter import *
from tkinter import ttk
from tkinter.messagebox import showinfo


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

    """ Verifica se o usuario e senha existe no arquivo users.txt e retorna true caso exista"""

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

window.title("Login")
window.geometry("400x300+450+200")
window["bg"] = "white"

# Label de título
lb = Label(window, text="Login", bg="white", font=("Arial Bold", 20))
lb.place(x=160, y=15)

# Label login
lb1 = Label(window, text="Username", bg="white", fg="gray", font=("Arial Bold", 15))
lb1.place(x=50, y=70)

# Entry do login
var1 = StringVar()
txt1 = Entry(window, width=20, textvariable=var1)
txt1.place(x=170, y=73)

# Label password
lb2 = Label(window, text="Password", bg="white", fg="gray", font=("Arial Bold", 15))
lb2.place(x=50, y=120)

# Entry do password
var2 = StringVar()
txt2 = Entry(window, width=20, textvariable=var2, show="*")
txt2.place(x=170, y=123)

# Button para logar
btn1 = ttk.Button(window, text="Login", width=12, command=login)
btn1.place(x=140, y=175)

window.mainloop()

"""
Date: 02/18/2022
Author: Flaviane S. Nascimento
Desc.: Sistema de login com Tkinter
"""

from tkinter import *
from tkinter import ttk
from tkinter.messagebox import showinfo


class Regist:

    """ Requisitos para cadastro """

    def __init__(self, name, passwd):
        self.dados_user = {}
        self.name = name
        self.passwd = passwd
        self.user = open("users.txt", 'a')
        self.dados_users = f'{name},{passwd}\n'
        self.user.write(self.dados_users)
        self.user.close()


register = Tk()


def registe():
    verify = check(var1.get(), var2.get(), var3.get())
    if verify is True:
        showinfo("Message", f"Username already in use")
    else:
        Regist(name=var1.get(), passwd=var2.get())
        showinfo("Message", f"Welcome :)")


def check(name, passwd, conf_pass):
    if name.upper() == passwd.upper():
        showinfo("Message", f"Password must be different from username")

    if passwd != conf_pass:
        showinfo("Message", f"Passwords don't match")

    if len(name) == 0 or len(passwd) == 0 or len(conf_pass) == 0:
        lb1["text"] = "User*"
        lb2["text"] = "Password*"
        lb3["text"] = "Confirm your\n password*"
        showinfo("Message", f"Required fields")

    if True:
        users = []

        try:
            with open('users.txt', 'r+') as archive:
                for line in archive:
                    line = line.strip()
                    users.append(line.split(","))

                for user in users[:]:
                    if name == user[0]:
                        return True

        except (Exception,):
            pass


register.title("Welcome")
register.geometry("600x400+350+150")
register["bg"] = "white"

lb = Label(register, text="WELCOME", bg="white", fg="black", font=("Ariel Bold", 13))
lb.place(x=252, y=10)

lb1 = Label(register, text="User", bg="white", fg="gray", font=("Arial Bold", 13))
lb1.place(x=179, y=70)

var1 = StringVar()
txt = Entry(register, width=20, textvariable=var1)
txt.place(x=270, y=70)

# dois
lb2 = Label(register, text="Password", bg="white", fg="gray", font=("Arial Bold", 13))
lb2.place(x=160, y=120)

var2 = StringVar()
txt = Entry(register, width=20, textvariable=var2)
txt.place(x=270, y=120)


lb3 = Label(register, text="Confirm your\n password", bg="white", fg="gray", font=("Arial Bold", 13))
lb3.place(x=145, y=165)

var3 = StringVar()
txt = Entry(register, width=20, textvariable=var3)
txt.place(x=270, y=180)

btn = ttk.Button(register, text="Register", width=12, command=registe)
btn.place(x=260, y=240)

register.mainloop()

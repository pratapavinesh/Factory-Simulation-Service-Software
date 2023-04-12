import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from head import head
from manager import manager
#FUNCTIONS
def on_enter_username(e):
    username.delete(0,"end")

def on_leave_username(e):
    name = username.get()
    if name == '':
        username.insert(0,'Username')

def on_enter_password(e):
    password.delete(0,"end")

def on_leave_password(e):
    name = password.get()
    if name == '':
        password.insert(0,'Password')


def auth():
    name = username.get()
    passwd = password.get()
    # print(f'{name = } & {passwd = }')
    # if name == 'Username' and passwd == 'Password':
    #     head()
    if name == 'head' and passwd == 'head':
        head()
    elif name == 'manager' and passwd == 'manager':
        manager()
    else:
        messagebox.showinfo("Alert", "Incorrect Username or password")

    

#MAIN WINDOW
root = tk.Tk()
root.title('Login')
root.geometry('600x600')

#HEADING
heading = ttk.Label(master = root,text = 'Sign in')
heading.pack()  

#INPUT
username = ttk.Entry(master = root)
username.insert(0, "Username")
username.pack()
username.bind("<FocusIn>", on_enter_username)
username.bind("<FocusOut>", on_leave_username)


password = ttk.Entry(master = root)
password.insert(0, "Password")
password.pack()
password.bind("<FocusIn>", on_enter_password)
password.bind("<FocusOut>", on_leave_password)

#BUTTON

signin_button = ttk.Button(master = root, text = 'Sign in', command = auth)
signin_button.pack()

#RUN
root.mainloop()
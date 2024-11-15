# this file contains all gui elements

from tkinter import *
from tkinter import ttk

import pass_ly as pass_wd 

def passwd_check(*args) :

    try :
        value = str(passwd.get())
        mssg.set(pass_wd._return_check(value))

    except ValueError :
        pass

root = Tk()
root.title("Anonym0us")
frm = ttk.Frame(root, padding="10")
frm.grid(row=0, column=0)

# root.columnconfigure(0, weight=1)
# root.rowconfigure(0, weight=1)

ttk.Label(frm, text="enter passwd : ", background="red").grid(column=0, row=1, stick='ns')

passwd = StringVar()
passwd_entry = ttk.Entry(frm, width=20, textvariable=passwd)
passwd_entry.grid(column=1,row=1)

ttk.Button(frm, text="Calculate", command=passwd_check).grid(column=2, row=1)

mssg = StringVar()
ttk.Label(frm, textvariable=mssg).grid(column=1, row=2)

for child in frm.winfo_children() :
    child.grid_configure(padx=10, pady=10)

root.bind('<Return>', passwd_check)

root.mainloop()

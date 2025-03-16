from tkinter import *
from tkinter import messagebox


def print_name(name):
    messagebox.showinfo('info', 'Hello {}!'.format(name))
    print("Hello {}! How are you?".format(name))


tk = Tk()
tk.geometry("500x450")
entry_name = Entry()
entry_name.place(x=150, y=150, width=200, height=50)
btn = Button(text="Enter your name?", command=(lambda: print_name(entry_name.get())))
btn.place(x=150, y=220, width=200, height=50)
tk.mainloop()

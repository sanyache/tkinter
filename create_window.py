from tkinter import *


def click_load():
    print("Loading .....")


tk = Tk()
tk.geometry("450x350")
btn = Button(text="Load", command=click_load)
btn.place(x=100, y=150, width=200, height=50)
tk.mainloop()

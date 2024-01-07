from tkinter import *
import time
import random


def handler():
    global run
    run = False


tk = Tk()
tk.title("Arkanoid")
# tk.config(relief=RAISED, bd=10)
tk.resizable(None, None)  # it doesn't allow to change the size of the window
tk.wm_attributes("-topmost", 1)  # always on top
canvas = Canvas(tk, width=500, height=600, bd=0, highlightthickness=0)
canvas.pack()
canvas.update()
tk.protocol("WM_DELETE_WINDOW", handler)
run = True
while run:
    tk.update_idletasks()
    tk.update()
    time.sleep(0.005)
tk.destroy()


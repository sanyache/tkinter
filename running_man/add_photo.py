import os
from tkinter import *
from PIL import Image, ImageTk
import time




def handler():
    global run
    run = False


tk = Tk()
tk.title("Running man")
tk.config(relief=RAISED, bd=10)
tk.resizable(None, None)  # it doesn't allow to change the size of the window
tk.wm_attributes("-topmost", 1)  # always on top
canvas = Canvas(tk, width=500, height=600, bd=0, highlightthickness=0)
canvas.pack()
bg_img = Image.open("man.png")
bg_img = ImageTk.PhotoImage(bg_img)
canvas.create_image(0, 0, image=bg_img, anchor="nw")

tk.protocol("WM_DELETE_WINDOW", handler)

tk.mainloop()
from tkinter import *
from tkinter import colorchooser


def choose_color(rectangle):
    color = colorchooser.askcolor()
    print(color)
    canvas.itemconfig(rectangle, fill=color[1])


tk = Tk()
canvas = Canvas(tk, width=500, height=500)
rec = canvas.create_rectangle(150, 150, 350, 350)
canvas.pack()
button = Button(tk, text="Choose color", command=lambda: choose_color(rec))
button.pack()
tk.mainloop()
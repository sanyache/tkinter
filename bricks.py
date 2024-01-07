from tkinter import *
import time
import random


def handler():
    global run
    run = False


class Brick:
    def __init__(self, canvas, width, color):
        self.canvas = canvas
        self.id = self.canvas.create_rectangle(0, 0, width, width/2, fill=color)

    def get_position(self):
        return self.canvas.coords(self.id)

    def delete(self):
        self.canvas.delete(self.id)


tk = Tk()
tk.title("Arkanoid")
# tk.config(relief=RAISED, bd=10)
tk.resizable(None, None)  # it doesn't allow to change the size of the window
tk.wm_attributes("-topmost", 1)  # always on top
canvas = Canvas(tk, width=500, height=600, bd=0, highlightthickness=0)
canvas.pack()
canvas.update()
brick_width = canvas.winfo_width()/10
color = "blue"
for i in range(10):
    for j in range(3):
        brick = Brick(canvas, brick_width, color)
        canvas.move(brick.id, brick_width*i, j * brick_width/2)
        canvas.update()

tk.protocol("WM_DELETE_WINDOW", handler)
run = True
while run:
    tk.update_idletasks()
    tk.update()
    time.sleep(0.005)
tk.destroy()


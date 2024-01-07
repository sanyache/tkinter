from tkinter import *
import time
import random


def handler():
    global run
    run = False


class Ball:
    def __init__(self, canvas, color):
        self.canvas = canvas
        self.id = self.canvas.create_oval(10, 10, 25, 25, fill=color)
        self.canvas.move(self.id, 250, 150)
        self.canvas_height = self.canvas.winfo_height()
        self.canvas_width = self.canvas.winfo_width()
        self.dx = 1
        self.dy = 0

    def get_position(self):
        return self.canvas.coords(self.id)

    def draw(self):
        self.canvas.move(self.id, self.dx, self.dy)
        pos = self.get_position()
        print(pos)
        if pos[0] < 0:
            self.dx = 1
        if pos[2] > self.canvas_width:
            self.dx = -1


tk = Tk()
tk.title("Arkanoid")
# tk.config(relief=RAISED, bd=10)
tk.resizable(None, None)  # it doesn't allow to change the size of the window
tk.wm_attributes("-topmost", 1)  # always on top
canvas = Canvas(tk, width=500, height=600, bd=0, highlightthickness=0)
canvas.pack()
canvas.update()
ball = Ball(canvas, "red")
tk.protocol("WM_DELETE_WINDOW", handler)
run = True
while run:
    ball.draw()
    tk.update_idletasks()
    tk.update()
    time.sleep(0.005)
tk.destroy()

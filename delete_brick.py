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


class Ball:
    def __init__(self, canvas, color):
        self.canvas = canvas
        self.id = self.canvas.create_oval(10, 10, 25, 25, fill=color)
        self.canvas.move(self.id, 250, 150)
        start = [-3, -2, -1, 1, 2, 3]
        random.shuffle(start)
        self.x = start[0]
        self.y = start[1]
        self.canvas.update()
        self.canvas_height = self.canvas.winfo_height()
        self.canvas_width = self.canvas.winfo_width()

    def draw(self):
        self.canvas.move(self.id, self.x, self.y)
        pos = self.get_position()
        if pos[1] <= 0:
            self.y = -self.y
        if pos[3] >= self.canvas_height:
            self.y = -self.y
        if pos[0] <= 0:
            self.x = -self.x
        if pos[2] >= self.canvas_width:
            self.x = -self.x

    def get_position(self):
        return self.canvas.coords(self.id)


def is_ball_hit_brick(ball, brick):
    pass

tk = Tk()
tk.title("Arkanoid")
# tk.config(relief=RAISED, bd=10)
tk.resizable(None, None)  # it doesn't allow to change the size of the window
tk.wm_attributes("-topmost", 1)  # always on top
canvas = Canvas(tk, width=500, height=600, bd=0, highlightthickness=0)
canvas.pack()
canvas.update()
brick_width = canvas.winfo_width()/10
color = "green"
ball = Ball(canvas, "red")
bricks = []
for i in range(3):
    for j in range(10):
        brick = Brick(canvas, brick_width, color)
        bricks.append(brick)
        canvas.move(brick.id, brick_width*j, i * brick_width/2)
        canvas.update()
tk.protocol("WM_DELETE_WINDOW", handler)
run = True
while run:
    ball.draw()
    for brick in bricks:
        if is_ball_hit_brick(ball, brick):
            brick.delete()
            bricks.remove(brick)
            ball.y = -ball.y
    tk.update_idletasks()
    tk.update()
    time.sleep(0.005)
tk.destroy()


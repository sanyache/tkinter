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
        """
        створюємо список для задання випадкового напрямку і випадкової швидкості
        руху кульки
        """
        start = [-3, -2, -1, 1, 2, 3]
        random.shuffle(start)
        self.dx = start[0]
        self.dy = start[1]
        self.canvas.update()
        self.canvas_height = self.canvas.winfo_height()
        self.canvas_width = self.canvas.winfo_width()

    def draw(self):
        self.canvas.move(self.id, self.dx, self.dy)
        pos = self.get_position()
        if pos[1] <= 0:
            self.dy = -self.dy
        if pos[3] >= self.canvas_height:
            self.dy = -self.dy
        if pos[0] <= 0:
            self.dx = -self.dx
        if pos[2] >= self.canvas_width:
            self.dx = -self.dx

    def get_position(self):
        return self.canvas.coords(self.id)


def is_ball_hit_brick(ball, brick):
    """
    функція, яка визначає чи була взаємодія кульки і цеглинки
    :param ball: кулька
    :param brick: цеглинка
    :return: True - якщо була взаємодія, False - якщо не було взаємодії.
    """
    ball_pos = ball.get_position()
    brick_pos = brick.get_position()
    if brick_pos[0] <= ball_pos[0] <= brick_pos[2] and brick_pos[1] <= ball_pos[1] <= brick_pos[3]:
        return True
    return False

tk = Tk()
tk.title("Arkanoid")
# tk.config(relief=RAISED, bd=10)
tk.resizable(None, None)  # it doesn't allow to change the size of the window
tk.wm_attributes("-topmost", 1)  # always on top
canvas = Canvas(tk, width=500, height=600, bd=0)
canvas.pack()
canvas.update()
brick_width = canvas.winfo_width()/10
color = "green"
ball = Ball(canvas, "red")
bricks = []  # створюємо пустий список, куди занесемо всі створені цеглинки
for i in range(3):
    for j in range(10):
        brick = Brick(canvas, brick_width, color)
        bricks.append(brick)  # додаємо цеглинку в список
        canvas.move(brick.id, brick_width*j, i * brick_width/2)
        canvas.update()
tk.protocol("WM_DELETE_WINDOW", handler)
run = True
while run:
    ball.draw()
    """
    перевіряємо чи була взаємодія з кожною цеглинкою,
    якщо так, то видаляємо її з Canvas і з списку bricks
    і змінюємо рух кульки на протилежний
    """
    for brick in bricks:
        if is_ball_hit_brick(ball, brick):
            brick.delete()
            bricks.remove(brick)
            ball.dy = -ball.dy
    tk.update_idletasks()
    tk.update()
    time.sleep(0.005)
tk.destroy()


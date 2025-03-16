from tkinter import *
import time
import random


def handler():
    global run
    run = False


class Brick:

    def __init__(self, canvas, width, color):
        """
        конструктор цеглинок, які реалізовані у вигляді зафорбованого прямокутника.
        :param canvas: полотно на якому розміщуємо цеглинку
        :param width: ширина цеглинки
        :param color: колір цеглинки
        """
        self.canvas = canvas   # в інших методах canvas будемо використовувати як власний атрибут
        self.id = self.canvas.create_rectangle(0, 0, width, width/2, fill=color)

    def get_position(self):
        """
        :return: повертає координати цеглинки self.id яка розташована на полотні canvas.
        """
        return self.canvas.coords(self.id)

    def delete(self):
        """
        знищує цеглинку self.id на полотні canvas.
        """
        self.canvas.delete(self.id)


tk = Tk()
tk.title("Arkanoid")
# tk.config(relief=RAISED, bd=10)
tk.resizable(None, None)  # it doesn't allow to change the size of the window
tk.wm_attributes("-topmost", 1)  # always on top
canvas = Canvas(tk, width=500, height=600, bd=0, highlightthickness=0)
canvas.pack()
canvas.update()
brick_width = canvas.winfo_width()/10  # обчислюємо ширину цеглинки.
color = 'blue'  # задаємо колір цеглинки
for i in range(3):
    for j in range(10):
        brick = Brick(canvas, brick_width, color)
        """
        рухаємо об'єкт на канвас, вказуємо який об'єкт та задаємо зміщення по x та y
        """
        canvas.move(brick.id, brick_width*j, brick_width/2*i)
        time.sleep(0.5)
        canvas.update()
tk.protocol("WM_DELETE_WINDOW", handler)
run = True
while run:
    tk.update_idletasks()
    tk.update()
    time.sleep(0.005)
tk.destroy()

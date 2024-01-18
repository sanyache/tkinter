from tkinter import *
import time
import random


def handler():
    global run
    run = False


class Ball:
    def __init__(self, canvas, color):
        """
        конструктор кульки
        :param canvas: полотно на якому створюємо гру
        :param color: колір кульки
        """
        self.canvas = canvas
        self.id = self.canvas.create_oval(10, 10, 25, 25, fill=color) # створюємо кульку
        self.canvas.move(self.id, 250, 150)  # переміщуємо в точку, з якої почнеться гра.
        self.canvas_width = self.canvas.winfo_width()  # визначаємо ширину вікна
        self.dx = 1
        self.dy = 0

    def get_position(self):
        return self.canvas.coords(self.id)

    def draw(self):
        """
        задаємо зміщення кульки на dx пікселів
        перевіряємо чи кулька не виходить за межі екрану
        якщо виходить, то змінюємо рух на протилежний
        """
        self.canvas.move(self.id, self.dx, 0)
        pos = self.get_position()
        print(pos) # друкуємо координати кульки, щоб зрозуміти параметри виходу за межі вікна
        if pos[2] > self.canvas_width:
            self.dx = - self.dx
        if pos[0] < 0:
            self.dx = - self.dx


tk = Tk()
tk.title("Arkanoid")
# tk.config(relief=RAISED, bd=10)
tk.resizable(None, None)  # it doesn't allow to change the size of the window
tk.wm_attributes("-topmost", 1)  # always on top
canvas = Canvas(tk, width=500, height=600, bd=0, highlightthickness=0)
canvas.pack()
canvas.update()
ball = Ball(canvas, 'red')
tk.protocol("WM_DELETE_WINDOW", handler)
run = True
while run:
    ball.draw()   # запускаємо рух кульки
    tk.update_idletasks()
    tk.update()
    time.sleep(0.005)
tk.destroy()


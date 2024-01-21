from tkinter import *
import time


class Board:
    def __init__(self, canvas, color):
        """
        конструктор платформи
        :param canvas:
        :param color:
        """
        self.canvas = canvas
        self.board_width = 150  # задаємо ширину платформи
        # створюємо платформу у верхньому лівому куті вікна
        self.id = self.canvas.create_rectangle(0, 0, 150, 10, fill=color)
        # оновлюємо полотно
        self.canvas.update()
        # визначаємо ширину і висоту полотна
        self.canvas_height = self.canvas.winfo_height()
        self.canvas_width = self.canvas.winfo_width()
        # переміщуємо платформу на вихідну позицію
        self.canvas.move(self.id,
                         self.canvas_width/2 - self.board_width/2,
                         self.canvas_height - 40)
        # задаємо зміщення платформи
        self.dx = 8

    # реалізуйте функції, які будуть переміщувати платформу вліво-вправо
    def move_right(self, event):
        # event - обов'язковий аргумент, який надає метод bind_all
        print("right", event)

    def move_left(self, event):
        print("left")

    def draw(self, dx):
        self.canvas.move(self.id, dx, 0)

    def get_position(self):
        return self.canvas.coords(self.id)


class Ball:
    def __init__(self, canvas, color):
        self.canvas = canvas
        self.id = self.canvas.create_oval(10, 10, 25, 25, fill=color)
        self.canvas.move(self.id, 250, 150)
        self.x = 1
        self.y = 2
        self.canvas.update()
        self.canvas_height = self.canvas.winfo_height()
        self.canvas_width = self.canvas.winfo_width()

    def draw(self):
        self.canvas.move(self.id, self.x, self.y)
        pos = self.get_position()
        if pos[1] <= 0:
            self.y = -self.y
        if pos[0] <= 0:
            self.x = -self.x
        if pos[2] >= self.canvas_width:
            self.x = -self.x

    def get_position(self):
        return self.canvas.coords(self.id)

    def delete(self):
        return self.canvas.delete(self.id)


def is_ball_hit_board(ball, board):
    """
    функція, яка визначає, чи є взаємодія кульки і платформи
    :param ball: кулька
    :param board: платформа
    :return: True - якщо була взаємодія, False - якщо ні.
    """
    ball_pos = ball.get_position()
    board_pos = board.get_position()
    if (board_pos[0] <= ball_pos[2] and board_pos[2] >= ball_pos[0]
            and board_pos[1] < ball_pos[3] and ball_pos[1] <= board_pos[3]):
        return True
    return False


def handler():
    global run
    run = False


tk = Tk()
tk.title("Arkanoid")
tk.resizable(None, None)  # it doesn't allow to change the size of the window
tk.wm_attributes("-topmost", 1)  # always on top
canvas = Canvas(tk, width=500, height=600, bd=0, highlightthickness=0)
canvas.pack()
board = Board(canvas, "blue")
ball = Ball(canvas, "red")

"""
bind_all - метод canvas, який зв'язує подію із її обробником
в даному випадку при натисненні клавіш "вліво" - "вправо" 
викликаються відповідні методи обробники подій
"""
canvas.bind_all("<KeyPress-Left>", board.move_left)
canvas.bind_all("<KeyPress-Right>", board.move_right)
tk.protocol("WM_DELETE_WINDOW", handler)
run = True
while run:
    ball.draw()
    if is_ball_hit_board(ball, board):
        ball.y = -ball.y
    tk.update_idletasks()
    tk.update()
    time.sleep(0.005)

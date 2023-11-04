from tkinter import *
import time
import random


class Board:
    def __init__(self, canvas, color):
        self.canvas = canvas
        self.board_width = 150
        self.id = self.canvas.create_rectangle(0, 0, 150, 10, fill=color)
        self.canvas.update()
        self.canvas_height = self.canvas.winfo_height()
        self.canvas_width = self.canvas.winfo_width()

        self.x = self.canvas_width/2 - self.board_width/2
        self.y = self.canvas_height - 40
        self.canvas.move(self.id, self.x, self.y)
        self.speed = 8

    def move_right(self, event):
        # print("right")
        # print(event)
        pos = self.get_position()
        self.x = self.speed
        if pos[2] + self.x <= self.canvas_width:
            self.draw()

    def move_left(self, event):
        pos = self.get_position()
        self.x = -self.speed
        if pos[0] - self.x >= 0:
            self.draw()

    def draw(self):
        self.canvas.move(self.id, self.x, 0)

    def get_position(self):
        return self.canvas.coords(self.id)


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
        # print(pos)
        if pos[1] <= 0:
            # self.y = 1
            self.y = -self.y
        if pos[3] >= self.canvas_height:
            # self.y = -1
            self.y = -self.y
        if pos[0] <= 0:
            # self.x = 1
            self.x = -self.x
        if pos[2] >= self.canvas_width:
            self.x = -self.x

    def get_position(self):
        return self.canvas.coords(self.id)


class Brick:
    def __init__(self, canvas, width, color):
        self.canvas = canvas
        self.id = self.canvas.create_rectangle(0, 0, width, width/2, fill=color)

    def get_position(self):
        return self.canvas.coords(self.id)

    def delete(self):
        self.canvas.delete(self.id)


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
board = Board(canvas, "blue")
ball = Ball(canvas, "red")
colors = ["black", "red", "green", "blue", "cyan", "yellow", "magenta", "azure", "brown",
          "coral", "grey", "khaki", "olive", "orange", "lavender", "ivory", "navy",
          "orchid", "plum"]
bricks = []
brick_width = canvas.winfo_width()/10
for i in range(10):
    for j in range(3):
        brick = Brick(canvas, brick_width, random.choice(colors))
        canvas.move(brick.id, i*brick_width, j*brick_width/2)
        bricks.append(brick)
        canvas.update()
canvas.bind_all("<KeyPress-Left>", board.move_left)
canvas.bind_all("<KeyPress-Right>", board.move_right)


def is_ball_hit_brick(ball, brick):
    ball_pos = ball.get_position()
    brick_pos = brick.get_position()
    if brick_pos[0] <= ball_pos[0] <= brick_pos[2] and brick_pos[1] <= ball_pos[1] <= brick_pos[3]:
        brick.delete()
        return True
    return False


def is_ball_hit_board(ball, board):
    ball_pos = ball.get_position()
    board_pos = board.get_position()
    if board_pos[0] <= ball_pos[0] <= board_pos[2] and board_pos[1] <= ball_pos[3]:
        return True
    return False


tk.protocol("WM_DELETE_WINDOW", handler)
run = True
while run:
    ball.draw()
    if is_ball_hit_board(ball, board):
        ball.y = -ball.y
    tk.update_idletasks()
    tk.update()
    for brick in bricks:
        if is_ball_hit_brick(ball, brick):
            bricks.remove(brick)
            ball.y = -ball.y
    time.sleep(0.005)
tk.destroy()
# tk.mainloop()

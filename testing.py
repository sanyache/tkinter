import os
from tkinter import *
from PIL import Image, ImageTk
import time


class Sprite:
    def __init__(self, image, ROW, COLUMN):
        self.sprites = []
        self.height_img, self.width_img = image.size
        self.height = self.height_img/COLUMN
        self.width = self.width_img/ROW
        for i in range(4):
            for j in range(12):
                img = image.crop((self.height*j, self.width*i, self.height+self.height*j,
                                 self.width+self.width*i))
                self.sprites.append(ImageTk.PhotoImage(img))

    def get_sprite_list(self):
        return self.sprites

    def get_forward_list(self):
        return self.sprites[:COLUMN]

    def get_left_list(self):
        return self.sprites[COLUMN:COLUMN*2]

    def get_right_list(self):
        return self.sprites[COLUMN*2:COLUMN*3]

    def get_back_list(self):
        return self.sprites[COLUMN*3:]


class Hero:
    def __init__(self, sprite, canvas):
        self.canvas = canvas
        self.canvas.update()
        self.canvas_width = canvas.winfo_width()
        self.canvas_height = canvas.winfo_height()
        self.sprite = sprite
        self.x = 200
        self.y = 100
        self.dx = 5
        self.dy = 5
        self.left_ind = 0
        self.right_ind = 0
        self.back_ind = 0
        self.forward_ind = 0
        self.hero_ava = sprite.get_forward_list()[0]
        self.hero_id = self.canvas.create_image(200, 100, anchor='nw', image=self.hero_ava)
        self.canvas.update()

    def get_avatar(self):
        return self.sprite.get_forward_list()[0]

    def handler(self, event):
        if event.keysym == "Left":
            self.move_left(event)
        if event.keysym == "Right":
            self.move_right(event)
        if event.keysym == "Up":
            self.move_back(event)
        if event.keysym == "Down":
            self.move_forward(event)

    def move_left(self, event):
        sprite = self.sprite.get_left_list()[self.left_ind]
        if self.x > 0:
            self.x -= self.dx
        self.left_ind = (self.left_ind + 1) % COLUMN
        self.move(sprite)

    def move_right(self, event):
        pos = self.get_position()
        sprite = self.sprite.get_right_list()[self.right_ind]
        if self.x + self.sprite.width <= (self.canvas_width+50):
            self.x += self.dx
        self.right_ind = (self.right_ind + 1) % COLUMN
        self.move(sprite)

    def move_back(self, event):
        sprite = self.sprite.get_back_list()[self.back_ind]
        if self.y > 0:
            self.y -= self.dy
        self.back_ind = (self.back_ind + 1) % COLUMN
        self.move(sprite)

    def move_forward(self, event):
        sprite = self.sprite.get_forward_list()[self.forward_ind]
        if self.y + self.sprite.height < self.canvas_height-60:
            self.y += self.dy
        self.forward_ind = (self.forward_ind + 1) % COLUMN
        self.move(sprite)

    def move(self, sprite):
        self.canvas.delete(self.hero_id)
        self.canvas.update()
        self.hero_id = self.canvas.create_image(self.x, self.y, anchor='nw', image=sprite)
        canvas.update()
        time.sleep(0.005)

    def get_position(self):
        return self.canvas.coords(self.hero_id)


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
# bg_img = Image.open("wall.png")
# bg_img = ImageTk.PhotoImage(bg_img)
# canvas.create_image(0, 0, image=bg_img, anchor="nw")

image = Image.open("pngwing.png")
print(image)
ROW = 4
COLUMN = 12
sprite = Sprite(image, ROW, COLUMN)
sprite_list = sprite.get_sprite_list()
hero = Hero(sprite, canvas)
canvas.bind_all("<KeyPress>", hero.handler)
tk.protocol("WM_DELETE_WINDOW", handler)
for step in sprite_list:
    hero.move(step)
run = True
while run:

    tk.update_idletasks()
    tk.update()
tk.destroy()

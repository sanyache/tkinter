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
        self.hero_ava = sprite.get_sprite_list()[0]
        self.hero_id = self.canvas.create_image(200, 100, anchor='nw', image=self.hero_ava)
        self.canvas.update()

    def get_avatar(self):
        return self.sprite.get_forward_list()[0]

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
tk.protocol("WM_DELETE_WINDOW", handler)
for step in sprite_list:
    hero.move(step)
    time.sleep(0.5)
run = True
while run:

    tk.update_idletasks()
    tk.update()
tk.destroy()

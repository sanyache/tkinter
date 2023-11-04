import random
from tkinter import *

tk = Tk()
canvas = Canvas(tk, width=500, height=500, bg="#808080")
colors = ["black", "red", "green", "blue", "cyan", "yellow", "magenta", "azure", "brown",
          "coral", "grey", "khaki", "olive", "orange", "lavender", "ivory", "navy", "orchid", "plum"]
for x in range(0, 500, 10):
    color = random.choice(colors)
    canvas.create_line(x, 0, x, 500, fill=color)
    canvas.create_line(0, x, 500, x, fill=color)

canvas.pack()
tk.mainloop()

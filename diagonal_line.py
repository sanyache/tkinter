import random
from tkinter import *

tk = Tk()
canvas = Canvas(tk, width=500, height=500)
colors = ["black", "red", "green", "blue", "cyan", "yellow", "magenta", "azure", "brown",
          "coral", "grey", "khaki", "olive", "orange", "lavender", "ivory", "navy", "orchid", "plum"]
for i in range(0, 1000, 10):
    canvas.create_line(0, 500 - i, i, 500, fill=random.choice(colors))
    canvas.create_line(500 - i, 500, 500, 500 - i, fill=random.choice(colors))
canvas.pack()
tk.mainloop()

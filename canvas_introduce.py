from tkinter import *

tk = Tk()
canvas = Canvas(tk, width=500, height=500)
canvas.create_line(0, 0, 500, 500, width=2, fill='green')
canvas.create_rectangle(50, 100, 350, 50, fill='blue', outline='red', width=3)
canvas.create_rectangle(50, 50, 350, 100)
canvas.create_polygon(100, 300, 100, 400, 200, 300, 200, 400)
canvas.create_oval(300, 150, 450, 450)
canvas.create_arc(10, 100, 200, 200, start=50, extent=180, style=ARC)
canvas.create_arc(10, 120, 200, 280, start=30, extent=300, style=PIESLICE, fill='yellow')
canvas.create_arc(400, 400, 500, 500)
canvas.pack()
tk.mainloop()
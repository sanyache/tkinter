from tkinter import *


def btn_click():
    for i in range(1, 10):
        print(i, end=' ')


button1 = Button(text="Click me", command=btn_click)
button1.pack()
mainloop()

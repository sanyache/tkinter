from tkinter import *

tk = Tk()
tk.title("Замовлення піци")

frame = Frame(tk)
frame.pack()

base_menu = LabelFrame(frame, text="Основне меню")
base_menu.grid(row=0, column=0, padx=10, pady=20, ipadx=20, ipady=10)

title_column = ["Найменування", "Ціна", "Кількість", "Вартість"]
for ind, title in enumerate(title_column):
    lb = Label(base_menu, text=title, font="Ariel 14 bold")
    lb.grid(row=0, column=ind, padx=20, pady=10)


def calculate_amount(event):
    val.delete(0, END)
    val.insert(END, str(int(event) * int(ent.get())))


title_product = ["Піца", "Морозиво", "Тістечка", "Сік"]

for index, title in enumerate(title_product):
    lb = Label(base_menu, text=title, font="Ariel, 16")
    ent = Entry(base_menu, justify="right", font=16)
    ent.insert(END, '0')
    scale = Scale(base_menu, orient=HORIZONTAL, command=calculate_amount)
    val = Entry(base_menu, justify="right", font=16)
    val.insert(END, '0')
    lb.grid(row=1 + index, column=0, padx=5, pady=5, sticky="ews")
    ent.grid(row=1 + index, column=1, padx=5, pady=5, sticky="ews", ipady=5)
    scale.grid(row=1 + index, column=2, padx=5, pady=5, sticky="ews")
    val.grid(row=1 + index, column=3, padx=5, pady=5, sticky="ews", ipady=5)

frame.mainloop()

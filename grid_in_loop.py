from tkinter import *


class ProductOrder:
    def __init__(self, title, index):
        self.lb = Label(base_menu, text=title, font="Ariel 16")
        self.ent = Entry(base_menu, font=16, justify="right")
        self.ent.insert(END, '0')
        self.val = Entry(base_menu, font=16, justify="right")
        self.val.insert(END, '0')
        self.scale = Scale(base_menu, orient=HORIZONTAL, font=16, command=self.calculate_amount)
        self.lb.grid(row=index + 1, column=0, sticky="ews", padx=5, pady=5)
        self.ent.grid(row=index + 1, column=1, sticky="ews", padx=5, pady=5)
        self.scale.grid(row=index + 1, column=2, sticky="ews", padx=5, pady=5)
        self.val.grid(row=index + 1, column=3, sticky="ews", padx=5, pady=5)

    def calculate_amount(self, event):
        self.val.delete(0, END)
        self.val.insert(END, str(int(event)*int(self.ent.get())))


tk = Tk()
tk.title("Замовлення піци")

frame = Frame(tk)
frame.pack()

base_menu = LabelFrame(frame, text="Основне меню", font=10)
base_menu.grid(row=0, column=0, padx=10, pady=20)

title_column = ["Найменування", "Ціна", "Кількість", "Вартість"]
for index, title in enumerate(title_column):
    lb = Label(base_menu, text=title,  font="Ariel, 14 bold")
    lb.grid(row=0, column=index, sticky=EW, pady=10, padx=20)

title_product = ["Піца", "Морозиво", "Тістечка", "Сік"]
products = []
for index, title in enumerate(title_product):
    product = ProductOrder(title, index)
    products.append(product)

frame.mainloop()
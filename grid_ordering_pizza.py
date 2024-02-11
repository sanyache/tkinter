from tkinter import *


class ProductOrder:
    def __init__(self, title, index):
        self.lb = Label(base_menu, text=title, font="Ariel 16")
        self.ent = Entry(base_menu, font=16)
        self.ent.insert(END, '0')
        self.val = Entry(base_menu, font=16)
        self.scale = Scale(base_menu, orient=HORIZONTAL, font=16, command=self.calculate_amount)
        self.lb.grid(row=index + 1, column=0, sticky="ews", padx=5, pady=5)
        self.ent.grid(row=index + 1, column=1, sticky="ews", padx=5, pady=5)
        self.scale.grid(row=index + 1, column=2, sticky="ews", padx=5, pady=5)
        self.val.grid(row=index + 1, column=3, sticky="ews", padx=5, pady=5)

    def calculate_amount(self, event):
        self.val.delete(0, END)
        self.val.insert(END, str(int(event)*int(self.ent.get())))


class AddProduct:
    def __init__(self, product, index):
        for key, val in product.items():
            self.val = val
            self.is_active = BooleanVar()
            self.check_button = Checkbutton(add_menu,
                                            variable=self.is_active,
                                            onvalue=True,
                                            offvalue=False,
                                            text=f'{key} {val}',
                                            font=16)
            self.check_button.grid(row=index + 1, column=0, sticky=W, pady=10, padx=10)


def total_amount():
    amount = 0
    for prod in products:
        amount += int(prod.val.get())
    for prod in add_products:
        if prod.is_active.get():
            amount += prod.val
    amount_total.delete(0, END)
    amount_total.insert(END, str(amount))


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

add_menu = LabelFrame(frame, text="Додаткове меню", font=10)
add_menu.grid(row=0, column=1, padx=10, pady=20, sticky="news")

add_label = Label(add_menu, text="Добавки до піци", font="Ariel 14")
add_label.grid(row=0, column=0, padx=10)

adding_product = [{"сир": 20}, {"гриби": 15}, {"бекон": 25}, {"ковбаски": 25}]
add_products = []
for index, product in enumerate(adding_product):
    add_product = AddProduct(product, index)
    add_products.append(add_product)

bottom_block = LabelFrame(frame, text="Обрахунок замовлення")
bottom_block.grid(row=1, column=0, columnspan=2, sticky=EW, padx=10, pady=20)
bottom_block.columnconfigure((0, 1, 2, 3, 4, 5), weight=1)
amount_label = Label(bottom_block, text="Сума", font="Ariel 14 bold")
amount_total = Entry(bottom_block, font=10)
amount_currency = Label(bottom_block, text="грн", font=10)
amount_btn = Button(bottom_block, text="Розрахувати", command=total_amount, font=10)

amount_label.grid(row=0, column=1, padx=20)
amount_total.grid(row=0, column=2, padx=20)
amount_currency.grid(row=0, column=3, padx=20)
amount_btn.grid(row=0, column=4, padx=20)

tk.mainloop()

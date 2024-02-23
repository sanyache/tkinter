from tkinter import *
from tkinter import ttk


window = Tk()
window.title("Data form")
frame = Frame(window)
frame.pack()

user_info_frame = LabelFrame(frame, text="Інформація про учня", font=10)
user_info_frame.columnconfigure((0, 1, 2), weight=1)
user_info_frame.grid(row=0, column=0, padx=20, pady=20, sticky="news")

first_name_label = Label(user_info_frame, text="Ім'я", font="Ariel, 14 bold")
first_name_entry = Entry(user_info_frame, font="Ariel 12")
first_name_label.grid(row=0, column=0)
first_name_entry.grid(row=1, column=0, ipady=5)

last_name_label = Label(user_info_frame, text="Прізвище", font="Ariel, 14 bold")
last_name_entry = Entry(user_info_frame, font="Ariel 12")
last_name_label.grid(row=0, column=1)
last_name_entry.grid(row=1, column=1, ipady=5)

gender_label = Label(user_info_frame, text="Стать", font="Ariel, 14 bold")
gender_combobox = ttk.Combobox(user_info_frame, values=["", "Чол", "Жін"], font="Ariel 12")
gender_label.grid(row=0, column=2)
gender_combobox.grid(row=1, column=2, ipady=5)

age_label = Label(user_info_frame, text="Вік", font="Ariel, 14 bold")
age_spinbox = Spinbox(user_info_frame, from_=10, to=17, font="Ariel 12")
age_label.grid(row=2, column=0, ipady=5)
age_spinbox.grid(row=3, column=0, ipady=5)

grade_label = Label(user_info_frame, text="Клас", font="Ariel, 14 bold")
grade_combobox = ttk.Combobox(user_info_frame, values=["8-а", "8-і", "8-б", "8-в"], font="Ariel 12")
grade_combobox.grid(row=3, column=1, ipady=5)
grade_label.grid(row=2, column=1, pady=5)
add_data_frame = LabelFrame(frame, text="Додаткова інформація", font=10)
add_data_frame.grid(row=1, column=0, padx=20, pady=10)

military_label = Label(add_data_frame, text="Військовий облік", font="Ariel, 14 bold")
military_var = BooleanVar()
military_check = Checkbutton(add_data_frame,
                             variable=military_var,
                             onvalue=True,
                             offvalue=False,
                             text="Чи стоїть на військовому обліку?",
                             font="Ariel 12")
military_label.grid(row=0, column=0, padx=10, pady=5)
military_check.grid(row=1, column=0, padx=10, pady=5, ipady=5)

id_label = Label(add_data_frame, text="ID учнівського квитка", font="Ariel, 14 bold")
id_spinbox = Spinbox(add_data_frame, from_=0, to="infinity", font="Ariel 12")
id_label.grid(row=0, column=1, padx=10, pady=5)
id_spinbox.grid(row=1, column=1, padx=10, pady=5, ipady=5)

subgroup_label = Label(add_data_frame, text="Підгрупа", font="Ariel, 14 bold")
subgroup_spinbox = Spinbox(add_data_frame, from_=1, to=2, font="Ariel 12")
subgroup_label.grid(row=0, column=2, padx=10, pady=5)
subgroup_spinbox.grid(row=1, column=2, padx=10, pady=5, ipady=5)

window.mainloop()

from tkinter import *
from tkinter import messagebox
from tkinter import ttk


def get_data():
    data = dict()
    if accept_var.get():
        data['first_name'] = first_name_entry.get()
        data['last_name'] = last_name_entry.get()
        data['gender'] = gender_combobox.get()
        data['military'] = military_var.get()
        data['student_id'] = id_spinbox.get()
        data['grade'] = grade_combobox.get()
        data['subgroup'] = subgroup_spinbox.get()
    else:
        messagebox.showwarning(title="Увага!", message="Не погоджено збір особистих даних")
    print(data)
    return data


window = Tk()
window.title("Data form")
frame = Frame(window)
frame.pack()

user_info_frame = LabelFrame(frame, text="Інформація про учня", font=10)
user_info_frame.grid(row=0, column=0, padx=20, pady=20, sticky="news")

first_name_label = Label(user_info_frame, text="Ім'я")
first_name_label.grid(row=0, column=0)
last_name_label = Label(user_info_frame, text="Прізвище")
last_name_label.grid(row=0, column=1)

first_name_entry = Entry(user_info_frame)
last_name_entry = Entry(user_info_frame)
first_name_entry.grid(row=1, column=0)
last_name_entry.grid(row=1, column=1)

gender_label = Label(user_info_frame, text="Пол")
gender_combobox = ttk.Combobox(user_info_frame, values=["", "Чол", "Жін"])
gender_label.grid(row=0, column=2)
gender_combobox.grid(row=1, column=2)

age_label = Label(user_info_frame, text="Вік")
age_spinbox = Spinbox(user_info_frame, from_=10, to=17)
age_label.grid(row=2, column=0)
age_spinbox.grid(row=3, column=0)

grade_label = Label(user_info_frame, text="Клас")
grade_combobox = ttk.Combobox(user_info_frame, values=["8-а", "8-і", "8-б", "8-в"])
grade_label.grid(row=2, column=1)
grade_combobox.grid(row=3, column=1)

add_data_frame = LabelFrame(frame, text="Додаткова інформація", font=10)
add_data_frame.grid(row=1, column=0, sticky="news", padx=20, pady=10)

military_label = Label(add_data_frame, text="Військовий облік")
military_var = BooleanVar()
military_check = Checkbutton(add_data_frame,
                             variable=military_var,
                             onvalue=True,
                             offvalue=False,
                             text="Чи стоїть на військовому обліці?")
military_label.grid(row=0, column=0)
military_check.grid(row=1, column=0)

id_label = Label(add_data_frame, text="ID учнівського квитка")
id_spinbox = Spinbox(add_data_frame, from_=0, to="infinity")
id_label.grid(row=0, column=1)
id_spinbox.grid(row=1, column=1)

subgroup_label = Label(add_data_frame, text="Підгрупа")
subgroup_spinbox = Spinbox(add_data_frame, from_=1, to=2)
subgroup_label.grid(row=0, column=2)
subgroup_spinbox.grid(row=1, column=2)

accept_frame = LabelFrame(frame, text="Збір особистих даних", font=10)
accept_frame.grid(row=2, column=0, sticky="news", padx=20, pady=10)
accept_var = BooleanVar()
accept_check = Checkbutton(accept_frame,
                           variable=accept_var,
                           onvalue=True,
                           offvalue=False,
                           text="Я погоджуюся на збір особистих даних",
                           font=10)
accept_check.grid(row=0, column=0, pady=10)

button = Button(frame, text="Відправити", command=get_data, font=12)
button.grid(row=3, column=0, sticky="news", pady=10, padx=20)
frames = [user_info_frame, add_data_frame, accept_frame]
for frame in frames:
    for widget in frame.winfo_children():
        widget.grid_configure(padx=10, pady=5)
        if widget.winfo_class() == "Label":
            widget.configure(font="Ariel, 14 bold")
        else:
            widget.configure(font="Ariel 12")

window.mainloop()

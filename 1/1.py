import tkinter as tk
from tkinter import messagebox
import random
import string
import math

def calculate_and_generate():
    try:
        length = int(length_entry.get())
        if length <= 0:
            raise ValueError
    except ValueError:
        messagebox.showerror("Ошибка", "Введите корректную длину пароля!")
        return

    alphabet = ""
    if var_digits.get():
        alphabet += string.digits
    if var_lower.get():
        alphabet += string.ascii_lowercase
    if var_upper.get():
        alphabet += string.ascii_uppercase
    if var_symbols.get():
        alphabet += "!@#$%^&*()-_=+[]{};:,.<>?/"

    if not alphabet:
        messagebox.showerror("Ошибка", "Выберите хотя бы один тип символов!")
        return

    alphabet_size = len(alphabet)
    total_passwords = alphabet_size ** length

    password = ''.join(random.choice(alphabet) for _ in range(length))

    result_label.config(
        text=f"Мощность алфавита: {alphabet_size}\n"
             f"Количество возможных паролей: {total_passwords:.3e}\n"
             f"(≈ 10^{math.log10(total_passwords):.2f})"
    )

    password_entry.config(state='normal')  
    password_entry.delete(0, tk.END)
    password_entry.insert(0, password)
    password_entry.config(state='readonly')  



root = tk.Tk()
root.title("Генератор паролей")
root.geometry("500x500")
root.resizable(False, False)

tk.Label(root, text="Длина пароля:", font=("Arial", 12)).pack(pady=5)
length_entry = tk.Entry(root, font=("Arial", 12), width=10, justify="center")
length_entry.insert(0, "8")
length_entry.pack(pady=5)

frame = tk.Frame(root)
frame.pack(pady=10)

var_digits = tk.BooleanVar(value=True)
var_lower = tk.BooleanVar(value=True)
var_upper = tk.BooleanVar(value=True)
var_symbols = tk.BooleanVar(value=False)

tk.Checkbutton(frame, text="Цифры (0-9)", variable=var_digits).grid(row=0, column=0, sticky="w")
tk.Checkbutton(frame, text="Строчные буквы (a-z)", variable=var_lower).grid(row=1, column=0, sticky="w")
tk.Checkbutton(frame, text="Заглавные буквы (A-Z)", variable=var_upper).grid(row=2, column=0, sticky="w")
tk.Checkbutton(frame, text="Спецсимволы (!@#$...)", variable=var_symbols).grid(row=3, column=0, sticky="w")

tk.Button(root, text="Сгенерировать пароль", font=("Arial", 12),
          command=calculate_and_generate).pack(pady=10)

result_label = tk.Label(root, text="Мощность алфавита: -\nКоличество паролей: -",
                        font=("Arial", 11))
result_label.pack(pady=10)

tk.Label(root, text="Случайный пароль:", font=("Arial", 12)).pack(pady=5)
password_entry = tk.Entry(root, font=("Arial", 14), width=30, justify="center")
password_entry.pack(pady=5)

root.mainloop()
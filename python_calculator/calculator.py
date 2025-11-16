import tkinter as tk
import re

# ввод цифр в строку калькулятора
def add_digit(digit):
    value = calc.get()
    if value == '0':
        value = digit
    else:
        value += digit
    calc.delete(0, tk.END) #функция delete очищает окно вывода нашего калькулятора calc (от 0 элемента строки, до последнего элемента строки)
    calc.insert(0, value) #функция insert добавляет в окно вывода нашего калькулятора calc (от 0 элемента строки, значение переменных value и operation)

# ввод операций в строку калькулятора
def add_operation(operation):
    value = calc.get()
    parts = re.split(r'[-+*/^]', value)
    if operation == '.':
        if '.' in parts[-1]:
            return
        else:
            calc.delete(0, tk.END)
            calc.insert(0, value + operation)
    else:
        if value and value[-1] in '-+*/^.':
            value = value[:-1]
        calc.delete(0, tk.END)
        calc.insert(0, value + operation)

#Считываем операцию вычисления из строки калькулятора
def calculate():
    value = calc.get()
    if value and value[-1] in '-+*/^.':
        value = value[:-1]
    calc.delete(0, tk.END)
    try:
        value = value.replace('^', '**')
        value = eval(value)
        calc.insert(0, "{:.4f}".format(value))
    except Exception as e:
        calc.insert(0, "Ошибка")

# макет кнопки под цифры
def make_digit_button(digit):
    return tk.Button(text=digit, bd=5, font=('Arial', 13), command=lambda: add_digit(digit))

# макет кнопки под перации
def make_operation_button(operation):
    return tk.Button(text=operation, bd=5, font=('Arial', 13), fg='red',
                     command=lambda: add_operation(operation))

# макет кнопки под знак =
def make_calc_button(operation):
    return tk.Button(text=operation, bd=5, font=('Arial', 13), fg='red',
                     command=calculate)

# макет кнопки отрицания
def make_min_button(operation):
    return tk.Button(text=operation, bd=5, font=('Arial', 13), fg='red',
                     command=add_min)

# функция очистки строки калькулятора
def clear():
    calc.delete(0, tk.END)
    calc.insert(0, '0')

# макет кнопки под очистку строки калькулятора
def make_clear_button(operation):
    return tk.Button(text=operation, bd=5, font=('Arial', 13), fg='red',
                     command=clear)

# функция ввода с клавиатуры
def press_key(event):
    # print(event)
    value = calc.get()
    if event.char.isdigit():
        if value == '0':
            value = event.char
        else:
              value += event.char
    elif  event.char in '.':
        parts = re.split(r'[-+*/^]',value)
        if '.' in parts[-1]:
            return
        else:
            value += event.char
        #     calc.delete(0, tk.END)
        #     calc.insert(0, value)
    elif event.char in '-+*/^.':
        if value and value[-1] in '-+*/^.':
            value = value[:-1] + event.char
        else:
            value += event.char
    calc.delete(0, tk.END)
    calc.insert(0, value)
    if event.keycode == 13:
        calculate()

# ввод точки кнопкой калькулятора
def add_fraction():
    value = calc.get()
    if '.' not in value:#[-1]:
        if value == '0':
            calc.delete(0, tk.END)
            calc.insert(0, '0.')
        else:
            add_digit('.')
# Ввод отрицания
def add_min():
    value = calc.get()
    calc.delete(0, tk.END)
    if value and value[0] == "-":
        value = value[1:]
        calc.insert(0, value)
    else:
        if "^" in value:
            value = value.replace("^","^-")
        else:
            value = "-" + value
        calc.insert(0, value)

# Создание графического интерфейса
win = tk.Tk()
win.geometry(f"305x270")
win.config(bg='#33ffe6')
win.title('Калькулятор')
win.bind('<Key>', press_key)

calc = tk.Entry(win, justify=tk.RIGHT, font=('Arial', 15), width=15)
calc.insert(0, '0')
calc.grid(row=0, column=0, columnspan=5, stick='we', padx=1)
# Расположение кнопок цифр
make_digit_button('1').grid(row=1, column=0, sticky='wens', padx=1, pady=5)
make_digit_button('2').grid(row=1, column=1, sticky='wens', padx=1, pady=5)
make_digit_button('3').grid(row=1, column=2, sticky='wens', padx=1, pady=5)
make_digit_button('4').grid(row=2, column=0, sticky='wens', padx=1, pady=5)
make_digit_button('5').grid(row=2, column=1, sticky='wens', padx=1, pady=5)
make_digit_button('6').grid(row=2, column=2, sticky='wens', padx=1, pady=5)
make_digit_button('7').grid(row=3, column=0, sticky='wens', padx=1, pady=5)
make_digit_button('8').grid(row=3, column=1, sticky='wens', padx=1, pady=5)
make_digit_button('9').grid(row=3, column=2, sticky='wens', padx=1, pady=5)
make_digit_button('0').grid(row=4, column=0, sticky='wens', padx=1, pady=5)
# Расположение кнопок операций
make_operation_button('+').grid(row=1, column=3, sticky='wens', padx=1, pady=5)
make_operation_button('-').grid(row=2, column=3, sticky='wens', padx=1, pady=5)
make_operation_button('/').grid(row=3, column=3, sticky='wens', padx=1, pady=5)
make_operation_button('*').grid(row=4, column=3, sticky='wens', padx=1, pady=5)
make_operation_button('^').grid(row=1, column=4, sticky='wens', padx=1, pady=5)

make_operation_button('.').grid(row=4, column=1, sticky='wens', padx=1, pady=5)
make_min_button('-/-').grid(row=2, column=4, sticky='wens', padx=1, pady=5)
make_calc_button('=').grid(row=4, column=2, sticky='wens', padx=1, pady=5)
make_clear_button('С').grid(row=3, column=4, sticky='wens', padx=1, pady=5, rowspan=2)
# Создание коркаса для графического интерфейса
win.grid_rowconfigure(1, minsize=60)
win.grid_rowconfigure(2, minsize=60)
win.grid_rowconfigure(3, minsize=60)
win.grid_rowconfigure(4, minsize=60)

win.grid_columnconfigure(0, minsize=60)
win.grid_columnconfigure(1, minsize=60)
win.grid_columnconfigure(2, minsize=60)
win.grid_columnconfigure(3, minsize=60)
win.grid_columnconfigure(4, minsize=60)
# Цикл завершения и активации
win.mainloop()
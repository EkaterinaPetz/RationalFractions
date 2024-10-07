"""
from math import gcd
import tkinter as tk
from tkinter import *
from tkinter import ttk

class RationalFraction:
    def __init__(self, num, denom=1):
        self.num = num
        if denom == 0:
            print("Деление на 0 невозможно! Знаминатель заменён на 1")
            self.denom = 1
        else:
            self.denom = denom
        self.simplify()

    def simplify(self):
        fr_gcd = gcd(self.num, self.denom)
        self.num //= fr_gcd
        self.denom //= fr_gcd
        if self.denom < 0:
            self.num = -self.num
            self.denom = -self.denom

    def add(self, other):
        new_num = self.num * other.denom + other.num * self.denom
        new_denom = self.denom * other.denom
        return RationalFraction(new_num, new_denom)

    def subtract(self, other):
        new_num = self.num * other.denom - other.num * self.denom
        new_denom = self.denom * other.denom
        return RationalFraction(new_num, new_denom)

    def multiply(self, other):
        new_num = self.num * other.num
        new_denom = self.denom * other.denom
        return RationalFraction(new_num, new_denom)

    def divide(self, other):
        if other.num == 0:
            raise ValueError("Деление на ноль невозможно.")
        new_num = self.num * other.denom
        new_denom = self.denom * other.num
        return RationalFraction(new_num, new_denom)

    def power(self, exponent):
        new_num = self.num ** exponent
        new_denom = self.denom ** exponent
        return RationalFraction(new_num, new_denom)

    def __str__(self):
        return f"{self.num}/{self.denom}"

    def add_integer(self, integ):
        fr2 = RationalFraction(integ, 1)
        return self.add(fr2)


def calculate_fraction_operation():
    num1 = int(entry_num1_1.get())
    den1 = int(entry_den1.get())
    num2 = int(entry_num2_1.get())
    den2 = int(entry_den2.get())
    operation = combo_operation.get()

    try:
        frac1 = RationalFraction(num1, den1)
        frac2 = RationalFraction(num2, den2)

        if operation == "Сложение":
            result = frac1.add(frac2)
        elif operation == "Вычитание":
            result = frac1.subtract(frac2)
        elif operation == "Умножение":
            result = frac1.multiply(frac2)
        elif operation == "Деление":
            result = frac1.divide(frac2)
        else:
            result = "Ошибка"

        label_result_1.config(text=str(result))
    except Exception as e:
        label_result_1.config(text=f"Ошибка: {e}")


def calculate_power():
    num = int(entry_power_num.get())
    denom = int(entry_power_den.get())
    degree = int(entry_power_degree.get())

    try:
        frac = RationalFraction(num, denom)
        result = frac.power(degree)
        label_result_2.config(text=str(result))
    except Exception as e:
        label_result_2.config(text=f"Ошибка: {e}")


def calculate_integer_addition():
    num = int(entry_integer_num.get())
    denom = int(entry_integer_denom.get())
    integ = int(entry_integer_value.get())
    try:
        frac = RationalFraction(num, denom)
        result = frac.add_integer(integ)
        label_result_3.config(text=str(result))
    except Exception as e:
        label_result_3.config(text=f"Ошибка: {e}")


root = Tk()

root.title("Калькулятор рациональных дробей")
root.geometry("300x400+250+50")

# Раздел 1: Операции с 2 дробями
frame1 = tk.Frame(root)
frame1.pack(pady=10)

# Первая дробь
tk.Label(frame1, text="Первая дробь:").grid(row=0, column=0, columnspan=3)
entry_num1_1 = tk.Entry(frame1, width=5)
entry_num1_1.grid(row=1, column=0)
tk.Label(frame1, text="/").grid(row=1, column=1)
entry_den1 = tk.Entry(frame1, width=5)
entry_den1.grid(row=1, column=2)

# Операция

combo_operation = ttk.Combobox(frame1,width=11, values=["Сложение", "Вычитание", "Умножение", "Деление"], state="readonly")
combo_operation.grid(row=1, column=3)
combo_operation.current(0)

# Вторая дробь
tk.Label(frame1, text="Вторая дробь:").grid(row=2, column=0, columnspan=3)
entry_num2_1 = tk.Entry(frame1, width=5)
entry_num2_1.grid(row=3, column=0)
tk.Label(frame1, text="/").grid(row=3, column=1)
entry_den2 = tk.Entry(frame1, width=5)
entry_den2.grid(row=3, column=2)

# Знак равно и результат
tk.Button(frame1, text="=", command=calculate_fraction_operation).grid(row=4, column=0)
label_result_1 = tk.Label(frame1, text="")
label_result_1.grid(row=4, column=1, columnspan=3)

# Раздел 2: Возведение в степень
frame2 = tk.Frame(root)
frame2.pack(pady=10)

# Дробь
tk.Label(frame2, text="Дробь:").grid(row=0, column=0, columnspan=3)
entry_power_num = tk.Entry(frame2, width=5)
entry_power_num.grid(row=1, column=0)
tk.Label(frame2, text="/").grid(row=1, column=1)
entry_power_den = tk.Entry(frame2, width=5)
entry_power_den.grid(row=1, column=2)

# Показатель степени
tk.Label(frame2, text="Cтепень:").grid(row=2, column=0)
entry_power_degree = tk.Entry(frame2, width=5)
entry_power_degree.grid(row=2, column=1)

# Знак равно и результат
tk.Button(frame2, text="=", command=calculate_power).grid(row=3, column=0)
label_result_2 = tk.Label(frame2, text="")
label_result_2.grid(row=3, column=1, columnspan=3)

# Раздел 3: Сложение дроби с целым числом
frame3 = tk.Frame(root)
frame3.pack(pady=30)

# Дробь
tk.Label(frame3, text="Дробь:").grid(row=0, column=0)
entry_integer_num = tk.Entry(frame3, width=5)
entry_integer_num.grid(row=0, column=1)
tk.Label(frame3, text="/").grid(row=0, column=2)
entry_integer_denom = tk.Entry(frame3, width=5)
entry_integer_denom.grid(row=0, column=3)
tk.Label(frame3, text="+").grid(row=0, column=4)

# Второе слагаемое - целое число
tk.Label(frame3, text="Число(int):").grid(row=1, column=0)
entry_integer_value = tk.Entry(frame3, width=5)
entry_integer_value.grid(row=1, column=1)

# Знак равно и результат
tk.Button(frame3, text="=", command=calculate_integer_addition).grid(row=2, column=0)
label_result_3 = tk.Label(frame3, text="")
label_result_3.grid(row=2, column=1, columnspan=3)


root.mainloop()
"""

"""
from math import gcd
import tkinter as tk
from tkinter import *
from tkinter import ttk

class RationalFraction:
    def __init__(self, num, denom=1):
        self.num = num
        if denom == 0:
            print("Деление на 0 невозможно! Знаминатель заменён на 1")
            self.denom = 1
        else:
            self.denom = denom
        self.simplify()

    def simplify(self):
        fr_gcd = gcd(self.num, self.denom)
        self.num //= fr_gcd
        self.denom //= fr_gcd
        if self.denom < 0:
            self.num = -self.num
            self.denom = -self.denom

    def __add__(self, other):
        new_num = self.num * other.denom + other.num * self.denom
        new_denom = self.denom * other.denom
        return RationalFraction(new_num, new_denom)

    def __sub__(self, other):
        new_num = self.num * other.denom - other.num * self.denom
        new_denom = self.denom * other.denom
        return RationalFraction(new_num, new_denom)

    def __mul__(self, other):
        new_num = self.num * other.num
        new_denom = self.denom * other.denom
        return RationalFraction(new_num, new_denom)

    def __truediv__(self, other):
        if other.num == 0:
            raise ValueError("Деление на ноль невозможно.")
        new_num = self.num * other.denom
        new_denom = self.denom * other.num
        return RationalFraction(new_num, new_denom)

    def __pow__(self, exponent):
        new_num = self.num ** exponent
        new_denom = self.denom ** exponent
        return RationalFraction(new_num, new_denom)

    def __str__(self):
        return f"{self.num}/{self.denom}"

    def fr_add_int(self, integ):
        fr2 = RationalFraction(integ, 1)
        return self.__add__(fr2)


def calculate_fraction_operation():
    num1 = int(entry_num1_1.get())
    den1 = int(entry_den1.get())
    num2 = int(entry_num2_1.get())
    den2 = int(entry_den2.get())
    operation = combo_operation.get()

    try:
        frac1 = RationalFraction(num1, den1)
        frac2 = RationalFraction(num2, den2)

        if operation == "Сложение":
            result = frac1.__add__(frac2)
        elif operation == "Вычитание":
            result = frac1.__sub__(frac2)
        elif operation == "Умножение":
            result = frac1.__mul__(frac2)
        elif operation == "Деление":
            result = frac1.__truediv__(frac2)
        else:
            result = "Ошибка"

        label_result_1.config(text=str(result))
    except Exception as e:
        label_result_1.config(text=f"Ошибка: {e}")


def calculate_power():
    num = int(entry_power_num.get())
    denom = int(entry_power_den.get())
    degree = int(entry_power_degree.get())

    try:
        frac = RationalFraction(num, denom)
        result = frac.__pow__(degree)
        label_result_2.config(text=str(result))
    except Exception as e:
        label_result_2.config(text=f"Ошибка: {e}")


def calculate_integer_addition():
    num = int(entry_integer_num.get())
    denom = int(entry_integer_denom.get())
    integ = int(entry_integer_value.get())
    try:
        frac = RationalFraction(num, denom)
        result = frac.fr_add_int(integ)
        label_result_3.config(text=str(result))
    except Exception as e:
        label_result_3.config(text=f"Ошибка: {e}")


root = Tk()

root.title("Калькулятор рациональных дробей")
root.geometry("300x400+250+50")

# Раздел 1: Операции с 2 дробями
frame1 = tk.Frame(root)
frame1.pack(pady=10)

# Первая дробь
tk.Label(frame1, text="Первая дробь:").grid(row=0, column=0, columnspan=3)
entry_num1_1 = tk.Entry(frame1, width=5)
entry_num1_1.grid(row=1, column=0)
tk.Label(frame1, text="/").grid(row=1, column=1)
entry_den1 = tk.Entry(frame1, width=5)
entry_den1.grid(row=1, column=2)

# Операция

combo_operation = ttk.Combobox(frame1,width=11, values=["Сложение", "Вычитание", "Умножение", "Деление"], state="readonly")
combo_operation.grid(row=1, column=3)
combo_operation.current(0)

# Вторая дробь
tk.Label(frame1, text="Вторая дробь:").grid(row=2, column=0, columnspan=3)
entry_num2_1 = tk.Entry(frame1, width=5)
entry_num2_1.grid(row=3, column=0)
tk.Label(frame1, text="/").grid(row=3, column=1)
entry_den2 = tk.Entry(frame1, width=5)
entry_den2.grid(row=3, column=2)

# Знак равно и результат
tk.Button(frame1, text="=", command=calculate_fraction_operation).grid(row=4, column=0)
label_result_1 = tk.Label(frame1, text="")
label_result_1.grid(row=4, column=1, columnspan=3)

# Раздел 2: Возведение в степень
frame2 = tk.Frame(root)
frame2.pack(pady=10)

# Дробь
tk.Label(frame2, text="Дробь:").grid(row=0, column=0, columnspan=3)
entry_power_num = tk.Entry(frame2, width=5)
entry_power_num.grid(row=1, column=0)
tk.Label(frame2, text="/").grid(row=1, column=1)
entry_power_den = tk.Entry(frame2, width=5)
entry_power_den.grid(row=1, column=2)

# Показатель степени
tk.Label(frame2, text="Cтепень:").grid(row=2, column=0)
entry_power_degree = tk.Entry(frame2, width=5)
entry_power_degree.grid(row=2, column=1)

# Знак равно и результат
tk.Button(frame2, text="=", command=calculate_power).grid(row=3, column=0)
label_result_2 = tk.Label(frame2, text="")
label_result_2.grid(row=3, column=1, columnspan=3)

# Раздел 3: Сложение дроби с целым числом
frame3 = tk.Frame(root)
frame3.pack(pady=30)

# Дробь
tk.Label(frame3, text="Дробь:").grid(row=0, column=0)
entry_integer_num = tk.Entry(frame3, width=5)
entry_integer_num.grid(row=0, column=1)
tk.Label(frame3, text="/").grid(row=0, column=2)
entry_integer_denom = tk.Entry(frame3, width=5)
entry_integer_denom.grid(row=0, column=3)
tk.Label(frame3, text="+").grid(row=0, column=4)

# Второе слагаемое - целое число
tk.Label(frame3, text="Число(int):").grid(row=1, column=0)
entry_integer_value = tk.Entry(frame3, width=5)
entry_integer_value.grid(row=1, column=1)

# Знак равно и результат
tk.Button(frame3, text="=", command=calculate_integer_addition).grid(row=2, column=0)
label_result_3 = tk.Label(frame3, text="")
label_result_3.grid(row=2, column=1, columnspan=3)


root.mainloop()
"""
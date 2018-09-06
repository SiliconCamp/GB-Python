__author__ = 'Тинкчян Феликс'

# Для задания №1
import random
# Для задания №3
import math

# Задача-1: Дано произвольное целое число, вывести самую большую цифру этого числа.
# Например, дается x = 58375.
# Нужно вывести максимальную цифру в данном числе, т.е. 8.
# Подразумевается, что мы не знаем это число заранее.
# Число приходит в виде целого беззнакового.
# Подсказки:
# * постарайтесь решить задачу с применением арифметики и цикла while;
# * при желании и понимании решите задачу с применением цикла for.

print("GeekBrains: Lesson 1 HomeWork")
print("_________________")
print("Task #1 -- started")

x = random.randint(1,99999)
takenumber = 0  # Берет последнюю цифру числа
max_take = 0  # Контроль максимального take

print("Source =", x)

while x != 0:

    take = x % 10
    if take > max_take:
        max_take = take

    x = x // 10

print("Max =", max_take)

print("Task #1 -- finished")

# Задача-2: Исходные значения двух переменных запросить у пользователя.
# Поменять значения переменных местами. Вывести новые значения на экран.
# Решите задачу, используя только две переменные.
# Подсказки:
# * постарайтесь сделать решение через действия над числами;
# * при желании и понимании воспользуйтесь синтаксисом кортежей Python.

print("_________________")
print("Task #2 -- started")

a = int(input("Number 1:"))
b = int(input("Number 2:"))

a = a + b
b = a - b
a = a - b

# a = a + (b / 10)
# b = int(a)
# a = a % 1
# a = int(a * 10)

print(a, b)
print("Task #2 -- finished")

# Задача-3: Напишите программу, вычисляющую корни квадратного уравнения вида
# ax² + bx + c = 0.
# Коэффициенты уравнения вводятся пользователем.
# Для вычисления квадратного корня воспользуйтесь функцией sqrt() модуля math:
# import math
# math.sqrt(4) - вычисляет корень числа 4

print("_________________")
print("Task #3 -- started")
print("Введите коэффициенты уравнения (ax² + bx + c = 0):")
a = float(input("a = "))
b = float(input("b = "))
c = float(input("c = "))

discr = b ** 2 - 4 * a * c;
print("Дискриминант D = ", discr)
if discr > 0:
    x1 = (-b + math.sqrt(discr)) / (2 * a)
    x2 = (-b - math.sqrt(discr)) / (2 * a)
    print("x1 =", x1, "x2 =", x2)
elif discr == 0:
    x = -b / (2 * a)
    print("x =", x)
else:
    print("Корней нет")
print("Task #3 -- finished")
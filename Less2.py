__author__ = 'Тинкчян Феликс'
# Репозиторий https://github.com/SiliconCamp/GB-Python
# DISCLAIMER!
# в решении я намеренно не использую принцип DRY, так как хочу сохранить возможность
# копипастить и запустить каждый кусок кода изолированно. В "боевом" проекте я бы использовал
# отдельную функцияю для генерации случайных списков.

import random
import datetime
import math

# Задача-1:
# Дан список, заполненный произвольными целыми числами, получите новый список,
# элементами которого будут квадратные корни элементов исходного списка,
# но только если результаты извлечения корня не имеют десятичной части и
# если такой корень вообще можно извлечь
# Пример: Дано: [2, -5, 8, 9, -25, 25, 4]   Результат: [3, 5, 2]

# Генерация списка

print("_____________________________")
print("Task #1")
print("Generating the list ...")
RandListLenght = random.randint(10, 50) # Определяем количество элементов в списке от 10 до 50 элементов
print("List lenght (elements):", RandListLenght)

RandList = []

while len(RandList) != RandListLenght:
    num = random.randint(-100,100) # Генерируем элемент от -100 до 100
    RandList.append(num)

print("Random list: ", RandList)

i = 0
RandSqrtList = []
for i in RandList:
    if i > 0:
        Sqrt = math.sqrt(i)
        if Sqrt == int(Sqrt):
            RandSqrtList.append(int(Sqrt))

print("Sqrted list: ", RandSqrtList)




# Задача-2: Дана дата в формате dd.mm.yyyy, например: 02.11.2013.
# Ваша задача вывести дату в текстовом виде, например: второе ноября 2013 года.
# Склонением пренебречь (2000 года, 2010 года)
print("_____________________________")
print("Task #2")
print("Generating the date ...")

RandDate = random.randint(500000,800000)
RandDate = datetime.datetime.fromordinal(RandDate)

RandDate = datetime.datetime.strptime(str(RandDate), '%Y-%m-%d %H:%M:%S').strftime('%d.%m.%Y')

print("Random date =", RandDate)




# Задача-3: Напишите алгоритм, заполняющий список произвольными целыми числами
# в диапазоне от -100 до 100. В списке должно быть n - элементов.
# Подсказка:
# для получения случайного числа используйте функцию randint() модуля random

print("_____________________________")
print("Task #3")
print("Generating the list ..")
n = random.randint(1, 50) # Определяем количество элементов в списке от 1 до 50 элементов, либо задать принудительно
print("List lenght n =", n)

RandList = []

while len(RandList) != n:
    num = random.randint(-100,100) # Генерируем элемент от -100 до 100
    RandList.append(num)

print("Random list: ", RandList)


# Задача-4: Дан список, заполненный произвольными целыми числами.
# Получите новый список, элементами которого будут:
# а) неповторяющиеся элементы исходного списка:
# например, lst = [1, 2, 4, 5, 6, 2, 5, 2], нужно получить lst2 = [1, 2, 4, 5, 6]
# б) элементы исходного списка, которые не имеют повторений:
# например, lst = [1 , 2, 4, 5, 6, 2, 5, 2], нужно получить lst2 = [1, 4, 6]

print("_____________________________")
print("Task #4")
print("Generating the list ..")
RandListLenght = random.randint(1, 50) # Определяем количество элементов в списке от 1 до 50 элементов
print("List lenght (elements):", RandListLenght)

RandList = []

while len(RandList) != RandListLenght:
    num = random.randint(-100,100) # Генерируем элемент от -100 до 100
    RandList.append(num)

print("Random list: ", RandList)
import random

# Задание-1:
# Напишите функцию, возвращающую ряд Фибоначчи с n-элемента до m-элемента.
# Первыми элементами ряда считать цифры 1 1
# РЕШЕНИЕ:
# Генерируем ряд Фиббоначи с самого начала. По достижении начального элемента ряда (n), начинаяем добавлять
# значения i-того элемента в результирующий массив. И так до тех пор, пока не достигнем конечного элемента (m)
print("_____________________________")
print("Task #1 - OK")


def fibonacci(n, m):
    fib1 = 1
    fib2 = 1
    fibarray = []


    i = 2
    while i < m:
        fib_sum = fib2 + fib1
        fib1 = fib2
        fib2 = fib_sum
        if i >= n-1:
            fibarray.append(fib2)
        i += 1

    return fibarray


fibo_start = random.randint(1, 40)
fibo_finish = random.randint(fibo_start, 40)
print("Fibonacci: from", fibo_start, "to", fibo_finish, "=", fibonacci(fibo_start, fibo_finish))

# Задача-2:
# Напишите функцию, сортирующую принимаемый список по возрастанию.
# Для сортировки используйте любой алгоритм (например пузырьковый).
# Для решения данной задачи нельзя использовать встроенную функцию и метод sort()
# РЕШЕНИЕ:
# Мы воспользуемся гномьим алгоритмом сортировки. Данный алгоритм очень прост и задействует только один цикл:
# "Это метод, которым садовый гном сортирует линию цветочных горшков. По существу он смотрит на текущий и предыдущий
# садовые горшки: если они в правильном порядке, он шагает на один горшок вперёд, иначе он меняет их местами и шагает
# на один горшок назад. Граничные условия: если нет предыдущего горшка, он шагает вперёд; если нет следующего горшка,
# он закончил."
# Дик Грун http://kvodo.ru/gnome-sorting.html


print("_____________________________")
print("Task #2 - OK")
print("Generating the list ...")
rand_list_len = random.randint(10, 50) # Определяем количество элементов в списке от 10 до 50 элементов
print("List len (elements):", rand_list_len)

rand_list = []

while len(rand_list) != rand_list_len:
    num = random.randint(-100,100) # Генерируем элемент от -100 до 100
    rand_list.append(num)

print("Random list: ",rand_list)


def sort_to_max(arr):
    i = 1
    while i < len(arr):
        if not i or arr[i - 1] <= arr[i]:
            i+=1
        else:
            arr[i], arr[i - 1] = arr[i - 1], arr[i]
            i-=1
    return arr


print("Gnome sorted list:", sort_to_max(rand_list))

# Задача-3:
# Напишите собственную реализацию стандартной функции filter.
# Разумеется, внутри нельзя использовать саму функцию filter.


# Задача-4:
# Даны четыре точки А1(х1, у1), А2(x2 ,у2), А3(x3 , у3), А4(х4, у4).
# Определить, будут ли они вершинами параллелограмма.

# coding: utf-8

import os
import sys
import psutil

# Комментарий

print("Great Python Program!")
print("Привет, программист!")

name = input("Ваше имя: ")
print(name, ", добро пожаловать в мир Python!")

#PEP-8
answer = ""

while answer != "Q":
    answer = input("Давайте поработаем? (Y/N/Q)")
    if answer == "Y":
        print("[1] - выведу список файлов")
        print("[2] - выведу информацию о системе")
        print("[3] - выведу список процессов")
        print("[4]")
        print("[5]")
        print("[6]")
        print("[7]")
        print("[8]")
        print("[9]")
        act = int(input("Выберите действие(1-9): "))

        if act == 1:
            print(os.listdir())
        elif act == 2:
            print("Вот что я знаю о системе:")
            print("Количество процессоров: ", psutil.cpu_count())
            print("Платформа: ", sys.platform)
            print("Кодировка файловой системы: ", sys.getfilesystemencoding())
            print("Текущая директория: ", os.getcwd())
            print("Текущий пользователь: ", os.getlogin())
        elif act == 3:
            print(psutil.pids())
        else:
            pass

    elif answer == "N":
        print("До свидания!")
    else:
        print("Неизвестный выбор")
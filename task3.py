# Задайте список из вещественных чисел. Напишите программу, которая найдёт разницу между максимальным 
# и минимальным значением дробной части элементов.

# Пример:
# - [1.1, 1.2, 3.1, 5, 10.01] => 0.19
import os
from random import uniform

def cls():
    os.system('cls' if os.name=='nt' else 'clear')

def GetNumber(message):
    isCorrect = False
    while isCorrect == False:
        try:
            number = int(input(message))
            isCorrect = True
        except ValueError:
            print("Введено не число. Повторите ввод ")
    return number

def InitList(number):
    my_list = []
    for i in range (number):
        my_list.append(round(uniform(0, 10), 2))
    return my_list

def TakeDifference(my_list):
    dif = 0
    dif_list = []
    for i in range(len(my_list)):
        dif_list.append(round(my_list[i]%1, 2))
        if i == 0:
            max = dif_list[i]
            min = dif_list[i]
        else:
            if dif_list[i]>max:
                max = dif_list[i]
            if dif_list[i] < min:
                min = dif_list[i]
    print(f'Дробная часть списка: {dif_list}')
    dif = round(max-min, 2)
    return dif

        
cls()
numb = GetNumber('Введите количество элементов списка ')
my_list = InitList(numb)
print(f'Список:               {my_list}')
diff = TakeDifference(my_list)
print(f'Разница между максимальным и минимальным значением дробной части {diff}')


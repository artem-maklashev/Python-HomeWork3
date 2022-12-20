# Задайте список из вещественных чисел. Напишите программу, которая найдёт разницу между максимальным 
# и минимальным значением дробной части элементов.

# Пример:
# - [1.1, 1.2, 3.1, 5, 10.01] => 0.19
import os
from random import uniform, randint

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
    index = randint(0,4)
    for i in range (number):
        my_list.append(round(uniform(0, 10), index))
    return my_list

def TakeDifference(my_list):
    dif = 0
    dif_list = []
    for i in range(len(my_list)):
        if my_list[i]%1 > 0:
            dif_list.append(round(my_list[i]%1,3))
    for j in range(len(dif_list)):        
            if j == 0:
                max = dif_list[j]
                min = dif_list[j]
            else:
                if dif_list[j]>max:
                    max = dif_list[j]
                if dif_list[j] < min:
                    min = dif_list[j]
    print(f'Дробная часть списка: {dif_list}')
    dif = round(max-min, 3)
    return dif

        
cls()
numb = GetNumber('Введите количество элементов списка ')
my_list = InitList(numb)
print(f'Список:               {my_list}')
diff = TakeDifference(my_list)
print(f'Разница между максимальным и минимальным значением дробной части {diff}')


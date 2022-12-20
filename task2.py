# Напишите программу, которая найдёт произведение пар чисел списка. Парой считаем первый и последний элемент, 
# второй и предпоследний и т.д.

# Пример:
# - [2, 3, 4, 5, 6] => [12, 15, 16];
# - [2, 3, 5, 6] => [12, 15]

from random import randint
import math

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
    for i in range(number):
        my_list.append(randint(0,10))
    return my_list

def MultiplyList(my_list):
    new_list = []
    for i in range(math.ceil(len(my_list)/2)):
        new_list.append(my_list[i]*my_list[len(my_list)-i-1])
    return new_list

numb = GetNumber('Введите количество элементов списка ')
first_list = InitList(numb)
second_list = MultiplyList(first_list)
print(f'{first_list} => {second_list}')


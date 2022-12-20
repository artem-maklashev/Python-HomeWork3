# Задайте список из нескольких чисел. Напишите программу, которая найдёт сумму элементов списка, стоящих на нечётной позиции.

# Пример:
# - [2, 3, 5, 9, 3] -> на нечётных позициях элементы 3 и 9, ответ: 12

from random import randint

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

def SumNotEven(my_list):
    sum = 0
    for i in range(1,len(my_list),2):
        sum+=my_list[i]
    return sum

numb = GetNumber("Введите количество элементов списка ")
new_list = InitList(numb)
sum = SumNotEven(new_list)
print(f'В списке {new_list} сумма нечетных элементов составляет {sum}')

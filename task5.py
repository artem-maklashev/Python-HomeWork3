# Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.

# Пример:
# - для k = 8 список будет выглядеть так: [-21 ,13, -8, 5, −3, 2, −1, 1, 0, 1, 1, 2, 3, 5, 8, 13, 21] 

import os

def cls():
    os.system('cls' if os.name=='nt' else 'clear')

def GetNumber(message):
    isCorrect = False
    while isCorrect == False:
        try:
            number = int(input(message))
            isCorrect = True
        except ValueError:
            print("Введено не целое число. Повторите ввод ")
    return number

def Fibo(number):
        if number == 0 or number == 1:
            return number
        elif number == -1:
            return 1
        elif number == -2:
            return -1
        elif number > 0:
            return Fibo(number-1)+Fibo(number-2)
        else:
            return int((-1)**(number+1)*Fibo(-number))
    
def InitList(number):
    fibo_list = []
    k = int(number/abs(number))
    for i in range (-number,number + k, k):
        fibo_list.append(Fibo(i))
    return fibo_list

cls()
numb = GetNumber('Введите число k: ')
my_list = InitList(numb)
print(f'Для k = {numb} последовательность выглядит -> {my_list}')
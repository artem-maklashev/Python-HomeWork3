# Напишите программу, которая будет преобразовывать десятичное число в двоичное.

# Пример:
# 45 -> 101101
# 3 -> 11
#- 2 -> 10
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

def DecToBin(number):
    my_list = ""
    while True:
        if int(number//2) == 0:
            my_list+='1'
            break
        else:
            my_list+=str(int(number%2))
            number/=2
    return my_list

cls()
numb = GetNumber('Input: ')
m_list = DecToBin(numb)
print(f'{numb} -> {m_list[::-1]}')
print(f'{numb:b}')
# 4) Задайте список из N элементов, заполненных числами из промежутка [-N, N]. 
# Найдите произведение элементов на указанных позициях. 
# Позиции вводятся с клавиатуры .

n = input('Введите N: ')

def is_int(k):
    try:
        int(k)
    except:
        print('Введено не корректное число.')
        quit()

is_int(n)
n = int(n)
new_list = []

import random
for i in range(0,n):
    a = random.randint(-n,n)
    new_list.append(a)
print(new_list)

print('Произведение скольких чисел, будем искать?')
z = input(f'Число  "от 2 до {len(new_list)}": ')
is_int(z)
z = int(z)


if z>len(new_list) or z<2:
    
    print('не корректное число')
    quit()

e = 1
resalt = 1

for i in range(0,z):
    d = input(f'Введите позицию числа {e}  "от 0 до {len(new_list)-1}": ')
    is_int(d)
    d = int(d)
    e+=1
    if d>len(new_list)-1 or d<0:
        print('Не корректное число.')
        quit()
    
    resalt *= new_list[d]

print(f'Произведение чисел равно: {resalt}')
# 1) Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.

# *Пример:*
# - 6782 -> 23
# - 0,56 -> 11

x = input('Введите число: ')

try:
    float(x)
except:
    print('Введено не корректное число.')
    quit()

new_list = list(x)
summ = 0
for i in range(len(new_list)):
    if new_list[i] == '.' or new_list[i] == '-' or new_list[i] == '+':
        new_list[i] = 0
    else:
        new_list[i] = int(new_list[i])
        summ += new_list[i] 

print(f'Cумма цифр в числе = {summ}')


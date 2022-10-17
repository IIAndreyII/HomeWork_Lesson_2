# 3) Задайте список из n чисел последовательности (1 + 1/n)^n и выведите на экран их сумму.

# *Пример:*
#     Для n=4 {1: 2, 2: 2.25, 3: 2.37, 4: 2.44}
#     Сумма 9.06

n = input('Введите n: ')

try:
    int(n)
except:
    print('Введено не корректное число.')
    quit()

n = int(n)
one_dic = {}
y = 1
summ = 0

for i in range(1,n+1):
    one_dic[y] = round(pow((1 + 1 / i),i),2)
    summ += one_dic[y]
    y += 1

print(one_dic)
print(summ)
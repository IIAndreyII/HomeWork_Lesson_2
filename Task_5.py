# 5) Реализуйте алгоритм перемешивания списка.

new_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print(new_list)

import random
for i in range(len(new_list)-1):
    z = random.randint(0, len(new_list)-1)
    temp = new_list[i]
    new_list[i] = new_list[z]
    new_list[z] = temp

print(new_list)
# Задача 22: Даны два неупорядоченных набора целых чисел (может быть, с
# повторениями). Выдать без повторений в порядке возрастания все те числа, которые
# встречаются в обоих наборах.
# Пользователь вводит 2 числа. n - кол-во элементов первого множества. m - кол-во
# элементов второго множества. Затем пользователь вводит сами элементы множеств.
# Например:
# 11 6
# 2 4 6 8 10 12 10 8 6 4 2
# 3 6 9 12 15 18
# 6 12
import random

n = int(input("Кол-во элементов первого множества: "))
m = int(input("Кол-во элементов второго множества: "))

import collections
a = []
for i in range(n):
    a.append(random.randint(1, 20))
print(a)

b = []
for i in range(m):
    b.append(random.randint(1, 10))
print(b)

print("1-й набор: " , [item for item, count in collections.Counter(a).items() if count > 1])
print("2-й набор: " , [item for item, count in collections.Counter(b).items() if count > 1])
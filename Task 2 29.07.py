# Во втором массиве сохранить индексы четных элементов первого массива.
import random


first_arr = []
second_arr = []
for n in range(8):
    first_arr.append(random.randint(1, 51))
print(first_arr)  # элементы первого массива
for i in first_arr:
    if i % 2 == 0:
        second_arr.append(i)
print(second_arr)  # элементы второго массива

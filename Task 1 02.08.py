# Task 2 29.07
# Во втором массиве сохранить индексы четных элементов первого массива.
import random


first_arr = []                                      # O(1)
second_arr = []                                     # O(1)
for n in range(8):
    first_arr.append(random.randint(1, 51))         # O(1)
print(first_arr)  # элементы первого массива
for i in first_arr:                                 # O(N)
    if i % 2 == 0:
        second_arr.append(i)                        # O(1)
print(second_arr)  # элементы второго массива

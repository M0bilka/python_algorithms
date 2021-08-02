# В одномерном массиве целых чисел определить два наименьших элемента.
import random

c = 0
arr = []
for n in range(8):
    arr.append(random.randint(1, 51))
print(arr)  # элементы массива
a = max(arr)
b = min(arr)
c = max(arr)
for n in arr:
    if arr.count(b) > 1:
        if c > n >= b:
            c = n
    else:
        if c > n > b:
            c = n
print(f'Два наименьших элемента: {b} и {c}')

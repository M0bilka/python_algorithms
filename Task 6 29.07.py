# В одномерном массиве найти сумму элементов, находящихся между минимальным и максимальным элементами.
import random

c = 0
arr = []
for n in range(8):
    arr.append(random.randint(1, 51))
print(arr)  # элементы массива
a = arr.index(max(arr))  # поиск индексов максимального и минимального значения
b = arr.index(min(arr))
if a < b:
    for n in range(a + 1, b):
        c += arr[n]
else:
    for n in range(b + 1, a):
        c += arr[n]
print(f"Сумма элементов между минимальными и максимальными элементами = {c}")

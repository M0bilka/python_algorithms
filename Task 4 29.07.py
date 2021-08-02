# Определить, какое число в массиве встречается чаще всего
import random

count = 0
arr = []
for n in range(8):
    arr.append(random.randint(1, 51))
print(arr)  # элементы массива
for n in arr:
    k = arr.count(n)
    if k > count:
        count = k
        num = n
if k == 1:
    print("Все элементы встречаются только 1 раз")
else:
    print(f"Элемент {num} появился {k} раз")

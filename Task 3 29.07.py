#  В массиве случайных целых чисел поменять местами минимальный и максимальный элементы.
import random


arr = []
for n in range(8):
    arr.append(random.randint(1, 51))
print(arr)  # элементы массива
a = arr.index(max(arr))  # поиск индексов максимального и минимального значения
b = arr.index(min(arr))
maksTemp = max(arr)
minTemp = min(arr)
arr[a] = minTemp
arr[b] = maksTemp
print(arr)  # элементы конечного массива

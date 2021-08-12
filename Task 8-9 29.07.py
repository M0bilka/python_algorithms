# Task 1 09.08: Подсчитать, сколько было выделено памяти под переменные в ранее разработанных программах в рамках первых
# трех уроков. Проанализировать результат и определить программы с наиболее эффективным использованием памяти.
import sys
# Task 8
# Матрица 5x4 заполняется вводом с клавиатуры кроме последних элементов строк.


matrix = []
for n in range(4):
    internal = []
    for j in range(4):
        internal.append(int(input(f"{j + 1} элемент {n + 1} строки: ")))    # Каждый ввод сразу попадает внутрь списка
    matrix.append(internal)                                                 # и потому не занимает память

print('\nМатрица:')
summary = []

# print(f"{sys.getsizeof(matrix) = }")    # Матрица 4х4 = 88 байт (Список с кол-вом элементов до 5 имеет размер 88 байт)

for n in range(len(matrix)):
    summary.append(sum(matrix[n]))
matrix.append(summary)
for n in range(len(matrix)):
    print(*matrix[n])

print(f"{sys.getsizeof(matrix) = }")    # Матрица 5х4 = 120 байт (Список на 5 элементов)

print('\n')

# Task 9
# Найти максимальный элемент среди минимальных элементов столбцов матрицы

mx = -1
for j in range(4):
    mn = max(max(matrix))
    for i in range(5):
        if matrix[i][j] < mn:
            mn = matrix[i][j]
    if mn > mx:
        mx = mn
print(f"Максимальный среди минимальных: {mx}")

print(f"{sys.getsizeof(mn) = }")    # Обе переменные весят 28 байт
# print(f"{sys.getsizeof(mx) = }")

# Суммарный объем памяти = 120 + (5 * 88) + (28 * 2) = 616 байт

# Система 64 бита, Python 3.9

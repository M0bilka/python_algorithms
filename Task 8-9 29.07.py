# Task 8
# Матрица 5x4 заполняется вводом с клавиатуры кроме последних элементов строк.


matrix = []
for n in range(4):
    internal = []
    for j in range(4):
        internal.append(int(input(f"{j + 1} элемент {n + 1} строки: ")))
    matrix.append(internal)

print('\nМатрица:')
summary = []
for n in range(len(matrix)):
    summary.append(sum(matrix[n]))
matrix.append(summary)
for n in range(len(matrix)):
    print(*matrix[n])
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

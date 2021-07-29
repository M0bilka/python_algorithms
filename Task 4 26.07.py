# Найти сумму n элементов следующего ряда чисел: 1 -0.5 0.25 -0.125

n = int(input("Введите кол-во элементов ряда: "))
summary = 0
num = 1
for i in range(1, n + 1):
    sum += num
    num = num / -2
print(summary)

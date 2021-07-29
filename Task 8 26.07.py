# Посчитать, сколько раз встречается определенная цифра в введенной последовательности чисел.
target = int(input("Введите число, которое необходимо найти: "))
num1 = int(input("Введите первое число: "))
num2 = int(input("Введите второе число: "))
num3 = int(input("Введите третье число: "))
summary = 0
while num1 > 0:
    if num1 % 10 == target:
        summary += 1
    num1 //= 10
while num2 > 0:
    if num2 % 10 == target:
        summary += 1
    num2 //= 10
while num3 > 0:
    if num3 % 10 == target:
        summary += 1
    num3 //= 10
print(f"Кол-во чисел {target} в трех введенных числах = {summary}")

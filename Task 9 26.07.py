# Среди натуральных чисел, которые были введены, найти наибольшее по сумме цифр.

num1 = int(input("Введите первое число: "))
num2 = int(input("Введите второе число: "))
num3 = int(input("Введите третье число: "))
temp1 = num1
temp2 = num2
temp3 = num3
s1 = 0
s2 = 0
s3 = 0
while num1 > 0:
    s1 = s1 + num1 % 10
    num1 //= 10
while num2 > 0:
    s2 = s2 + num2 % 10
    num2 //= 10
while num3 > 0:
    s3 = s3 + num3 % 10
    num3 //= 10
if s3 > s1 and s2 != s1:
    print(f"Число {temp3} имеет наибольшую сумму цифр: {s3}")
elif s2 > s3 and s3 != s1:
    print(f"Число {temp2} имеет наибольшую сумму цифр: {s2}")
elif s1 > s2 and s2 != s3:
    print(f"Число {temp1} имеет наибольшую сумму цифр: {s1}")

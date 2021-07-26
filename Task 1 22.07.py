num = int(input("Введите трехзначное число:"))
if (num // 100 == 0) or (num // 100 > 9):
    print("Неподходящее число")
else:
    first = num % 10
    num = num // 10
    sec = num % 10
    num = num // 10
    third = num % 10
print(f"Сумма - {third + sec + first}, произведение - {third * sec * first}")

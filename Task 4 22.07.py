import random


print('''
1 - случайное целое число
2 - случайное вещественное число
3 - случайный символ
''')
choice = int(input("Выбор действия: "))
if choice == 1:
    a = int(input("Введите меньшее число диапозона: "))
    b = int(input("Введите большее число диапозона: "))
    print(random.randint(a, b))
elif choice == 2:
    a = float(input("Введите меньшее число диапозона: "))
    b = float(input("Введите большее число диапозона: "))
    print(random.uniform(a, b))
elif choice == 3:
    a = ord(input("Введите меньшее значение диапозона: "))
    b = ord(input("Введите большее значение диапозона: "))
    print(chr(random.randint(a, b)))
else:
    print("Число выбора неверное")

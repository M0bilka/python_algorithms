#  Написать программу, которая будет складывать, вычитать, умножать или делить два числа.

choice = input("Введите символ операции (0 - для выхода): ")
while choice != "0":
    if choice == '+' or choice == '-' or choice == '*' or choice == '/':
        first = int(input("Введите первое число: "))
        second = int(input("Введите второе число: "))
        if choice == '+':
            print(f"Результат сложения = {first + second}")
            choice = input("Введите символ операции (0 - для выхода): ")
        elif choice == '-':
            print(f"Результат вычитания = {first - second}")
            choice = input("Введите символ операции (0 - для выхода): ")
        elif choice == '*':
            print(f"Результат умножения = {first * second}")
            choice = input("Введите символ операции (0 - для выхода): ")
        elif choice == '/':
            if first == 0:
                print('Деление на 0 невозможно')
            else:
                print(f"Результат деления = {first / second}")
            choice = input("Введите символ операции (0 - для выхода): ")
    else:
        print("Вы ввели неверный символ")
        choice = input("Введите символ операции (0 - для выхода): ")

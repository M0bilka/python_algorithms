# В программе генерируется случайное целое число от 0 до 100. Пользователь должен его отгадать не более чем за 10 попыток.
import random

chance = 10
target = random.randint(0, 100)
hit = int(input("Угадайте число от 0 до 100: "))
while chance != 0:
    if hit < target:
        chance -= 1
        print(f"Вы выбрали число меньше, чем загадано")
        hit = int(input(f"У вас есть еще {chance} попыток. Попробуйте еще: "))
    elif hit > target:
        chance -= 1
        print(f"Вы выбрали число больше, чем загадано")
        hit = int(input(f"У вас есть еще {chance} попыток. Попробуйте еще: "))
    elif hit == target and chance > 0:
        print(f"Поздравляю! Вы угадали число {target}, у вас осталось еще {chance} попыток")
        break

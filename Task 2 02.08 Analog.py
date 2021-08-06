# Написать два алгоритма нахождения i-го по счёту простого числа без использования «Решета Эратосфена»
# import time
# import cProfile


def calculate(maks_num):
    arr = []                                                                            # O(1)
    for num in range(2, maks_num):                                                      # O(N)
        if num == 2 or num == 3 or num == 5 or num == 7:
            arr.append(num)                                                             # O(1)
        elif (num % 2 != 0) and (num % 3 != 0) and (num % 5 != 0) and (num % 7 != 0):
            arr.append(num)                                                             # O(1)
    return arr


# start_time = time.time()

maks_number = int(input("До какого числа найти простые числа: "))
print(calculate(maks_number))

# print(cProfile.run('calculate(maks_num)'))
# print(time.time() - start_time)  # 5 запусков (для точности) со значением 57 дали результат по времени 1.698

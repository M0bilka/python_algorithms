x1 = int(input("Перый Х: "))
y1 = int(input("Первый У: "))
x2 = int(input("Второй Х: "))
y2 = int(input("Второй У: "))
k = (y1 - y2) / (x1 - x2)
b = y2 - k * x2
print(f"y = {k}*x + {b}")

var = float(input("Введите значение переменной x: "))
start = int(input("Введите начальное значение n: "))
stop = int(input("Введите конечное значение n: "))
step = int(input("Введите шаг функции: "))
precision = int(input("Введите точность вычислений: "))

print("Таблица вычислений функции")
cell = stop // 10 + 5
print()
result = 0
counter = 1
while start <= stop:
    power = 2 * start + 1
    result += 1 / (power * pow(var, power))

    print(f"{start:<{cell}d} {result:^0.{precision}f} {counter:>{cell}d}")
    start += step
    counter += 1

try:
    var = float(input("Введите значение переменной x: "))
    if abs(var) <= 1:
        print("Значение переменной по модулю должно быть больше 1")
        exit()
    # start = int(input("Введите начальное значение числового ряда: "))
    stop = int(input("Введите конечное значение числового ряда: "))
    step = int(input("Введите шаг функции: "))
    precision = int(input("Введите точность вычислений: "))

    cell = 20
    print("{:^{width}}".format("Таблица вычислений функции", width=cell*3))
    print("{:^{width}}{:^{width}}{:^{width}}"
          .format("Значение аргумента", "Значение функции", "Количество рядов", width=cell))
    result = 0
    counter = 1
    start = 0
    while start < stop:
        power = 2 * start + 1
        result += 1 / (power * pow(var, power))

        print(f"{start:^{cell}d}{result:^{cell}.{precision}f}{counter:^{cell}d}")
        start += step
        counter += 1
    print(f"{'Значение аргумента':^{cell}}{'Значение функции':^{cell}}{'Количество рядов':^{cell}}")

except ValueError:
    print("Ошибка. Вы можете вводить только числа, состоящие из цифр, а не текст!!!")

""" Найти косинус минимального из 4 заданных чисел"""

from math import radians, cos

try:
    a, b, c, d = map(float, input("Введите 4 значения угла в градусах через пробел:\n").split(maxsplit=3))
    a = cos(radians(a))
    b = cos(radians(b))
    c = cos(radians(c))
    d = cos(radians(d))
    if a == b == c == d:
        print(f"Все числа равны. Минимальное: {cos(radians(a)):.4f}")
    elif a <= b and a <= c and a <= d:
        print(f"Минимальное значение cos: {a:.4f}")
    elif b <= c and b <= d:
        print(f"Минимальное значение cos: {b:.4f}")
    elif c <= d:
        print(f"Минимальное значение cos: {c:.4f}")
    else:
        print(f"Минимальное значение cos: {d:.4f}")
except ValueError:
    print("Ошибка. Нужно ввести через пробел только 4 числа, состоящие из цифр и не текст!!!")

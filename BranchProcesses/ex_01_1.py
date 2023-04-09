""" Найти косинус минимального из 4 заданных чисел"""

from math import radians, cos

try:
    num_list =\
        list(radians(float(num)) for num in
             input("Введите 4 значения угла в градусах через запятую:\n").split(sep=',', maxsplit=3))
    # print("Список углов в радианах:\n{}\nПроверка типа {}".format(num_list, type(num_list)))
    print("Список углов в радианах:\n", *num_list, f"\nТип: {type(num_list)}")
    min_num = 2
    for num in num_list:
        num = cos(num)
        if num < min_num:
            min_num = num

    print(f"Минимальное значение cos: {min_num:.2f}")
except ValueError:
    print("Ошибка. Нужно ввести через запятую только 4 числа, состоящие из цифр и не текст!!!")

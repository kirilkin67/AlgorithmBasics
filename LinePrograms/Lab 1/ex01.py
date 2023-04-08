from math import radians, sin, tan

try:
    alpha = float(input("Введите значение угла в градусах: "))
    alpha_radians = radians(alpha)
    result_1 = (1 - 2 * sin(alpha_radians) ** 2) / (1 + sin(2 * alpha_radians))
    result_2 = (1 - tan(alpha_radians)) / (1 + tan(alpha_radians))
except ValueError:
    print("Ошибка. Вы можете вводить только числа, состоящие из цифр, а не текст!!!")
except ZeroDivisionError:
    print("Ошибка. При данном значении происходит деление на ноль.")
else:
    print(f"Первая формула:\nвведённое значение - {alpha} градусов, результат вычисления: {result_1:.4f}")
    print(f"Вторая формула:\nвведённое значение - {alpha} градусов, результат вычисления: {result_2:.4f}")

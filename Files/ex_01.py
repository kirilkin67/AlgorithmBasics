from math import sqrt, pow, e, cos, sin

TASK = '''
Лабораторная работа №7
1. Записать в файл цикл расчета значений функции.
Файл должен быть создан во время выполнения программы.
2. Записать в файл свои ФИО и группу.
3. Дать возможность пользователю, по желанию, считать из файла
рассчитанные значения и вывести на экран.
'''


def calculate_function(x, y, z):
    first = pow(y, pow(abs(x), 1/3))
    second = abs(x - y) * (1 + pow(sin(z), 2) / sqrt(x + y))
    third = pow(e, abs(x - y)) + y / 2
    return first + pow(cos(y), 3) * second / third


file_name = "lab_07.txt"
try:
    with open(file_name, 'w', encoding="utf-8") as fd:
        fd.write("Лабораторная работа №7. Вариант 11\n")
        fd.write("Кирилкин Михаил Альбертович\n")
        fd.write('Группа ИСП11оз-122ИП\n')


except (OSError, FileNotFoundError, IOError):
    print("File cannot be opened", file_name)

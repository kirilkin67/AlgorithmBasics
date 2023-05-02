from math import sqrt, pow, e, cos, sin

TASK = '''
Лабораторная работа №7
1. Записать в файл цикл расчета значений функции.
Файл должен быть создан во время выполнения программы.
2. Записать в файл свои ФИО и группу.
3. Дать возможность пользователю, по желанию, считать из файла
рассчитанные значения и вывести на экран.
'''
MENU = '''
0 - выйти из программы
1 - вывести результаты на экран'''
FILE_NAME = "lab_07.txt"


def input_data():
    try:
        var1 = float(input("Введите начальное значение переменной X: "))
        var2 = float(input("Введите конечное значение переменной X: "))
        var3 = abs(float(input("Введите шаг функции: ")))
        var4 = float(input("Введите значение переменной Y: "))
        var5 = float(input("Введите значение переменной Z: "))
        if var1 > var2:
            var1, var2 = var2, var3
        return var1, var2, var3, var4, var5
    except ValueError:
        print("Ошибка. Вы можете вводить только числа, состоящие из цифр, а не текст!!!")


def calculate_function(x, y, z):
    try:
        first = pow(y, pow(abs(x), 1/3))
        second = abs(x - y) * (1 + pow(sin(z), 2) / sqrt(x + y))
        third = pow(e, abs(x - y)) + y / 2
        return first + pow(cos(y), 3) * second / third
    except ZeroDivisionError:
        print("При данных значениях происходит деление на ноль.")
    except ValueError:
        print("При данных значениях происходит извлечение отрицательного квадратного корня.")


def write_result(var_x, stop, step, var_y, var_z):
    precision = 4
    cell = 20
    try:
        with open(FILE_NAME, 'w', encoding="utf-8") as fd:
            fd.write("Лабораторная работа №7. Вариант 11\n")
            fd.write("Кирилкин Михаил Альбертович\n")
            fd.write('Группа ИСП11оз-122ИП\n\n')
            fd.write("{:^{width}}\n".format("Таблица вычислений функции", width=cell * 2))
            fd.write("-" * (cell * 2) + "\n")
            fd.write(f"{'Значение Y':^{cell}}{'Значение Z':^{cell}}\n")
            fd.write(f"{var_y:^{cell}.{precision}f}${var_z:^{cell}.{precision}f}\n")
            fd.write(f"{'Значение X':^{cell}}{'Значение функции':^{cell}}\n")
            while var_x <= stop:
                result = calculate_function(var_x, var_y, var_z)
                fd.write(f"{var_x:^{cell}.{precision}f}${result:^{cell}.{precision}f}\n")
                var_x += step
    except (OSError, FileNotFoundError, IOError):
        print("File cannot be opened", FILE_NAME)
    except TypeError:
        print("Ошибка вычислений")


def read_file():
    choice = None
    count = 0
    while choice != '0' and count < 5:
        print(MENU)
        choice = input("Ваш выбор: ")
        if choice == '0':
            print("До свидания")
        elif choice == '1':
            try:
                with open(FILE_NAME, 'r', encoding="utf-8") as fdr:
                    print(fdr.read())
            except (OSError, FileNotFoundError, IOError):
                print("Ошибка чтения файла", FILE_NAME)
            finally:
                choice = '0'
        else:
            print("Вы ошиблись.")
        count += 1


x_min, x_max, x_step, y, z = input_data()
write_result(x_min, x_max, x_step, y, z)
read_file()

from random import randint

TASK = '''
Лабораторная работа №5
2. Найти самое маленькое по величине четное значение не кратное С,
расположенных после К-го индекса.
'''


def input_data():
    count = 1
    while True:
        try:
            value = int(input("Введите количество элементов массива, значение должно быть больше 1: "))
            value = -value if value < 0 else value
            value = 1 if value == 0 else value

            value1 = int(input("Введите кратность числа: "))
            value1 = -value1 if value1 < 0 else value1

            value2 = int(input("Введите индекс массива: "))
            value2 = -value2 if value2 < 0 else value2
            value2 = check_index(value2, value)
            return value, value1, value2
        except ValueError:
            print("Ошибка. Вы можете вводить только числа, состоящие из цифр, а не текст!!!"
                  "\nПопробуйте ещё раз.")
        finally:
            if count == 3:
                print("Извините, но количество попыток закончилось")
                exit()
        count += 1


def check_index(var_index, size):
    if (var_index + 1) >= size:
        print(f"Значение индекса должно быть меньше - {size - 1}")
        var_index = size - 2
    return var_index


def create_array(size: int, minimum: int, maximum: int):
    """
    Генерация массива случайными числами, int
    :param size: размер массива
    :param minimum: минимальное значение массива
    :param maximum: максимальное значение массива
    :return: сгенерированный массив
    """
    if minimum > maximum:
        minimum, maximum = maximum, minimum
    return [randint(minimum, maximum) for _ in range(size)]


def find_element_by_condition(source: list, mod: int, start=-1):
    new_list = list()
    for k in range(start + 1, array_size):
        if source[k] % 2 == 0 and source[k] % mod != 0:
            new_list.append(source[k])
    print(f"Массив чётных элементов не кратных {mod}: ", *new_list)
    validate_array(new_list)


def validate_array(source: list):
    if len(source) == 0:
        print(f"Нет элементов удовлетворяющих условию - чётные и не кратны {multiple}")
    else:
        print(f"Минимальный чётный элемент не кратный {multiple} - {sorted(source)[0]}")


print(TASK)
array_size, multiple, start_index = input_data()
generated_array = create_array(array_size, 101, 999)
print("Сгенерированный массив: ", *generated_array)

find_element_by_condition(generated_array, multiple, start_index)

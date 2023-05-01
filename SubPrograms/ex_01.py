from random import randint

TASK = '''
1. Заполните массив случайными числами.
- заменить значение элемента массива с минимальным произведением цифр,
на его индекс, за исключением первой цифры элемента.
'''


def input_data():
    count = 1
    while True:
        value = input("Введите количество элементов массива, значение должно быть больше 1: ")
        if value.isdigit():
            value = int(value)
            if value > 0:
                return value
            else:
                print("Количество элементов массива должно быть больше 1\nПопробуйте ещё раз.")
        else:
            print("Ошибка. Вы можете вводить только числа, состоящие из цифр, а не текст!!!"
                  "\nПопробуйте ещё раз.")
        if count == 3:
            print("Извините, но количество попыток закончилось")
            exit()
        count += 1


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


def multiply_digit(num: int, lim=0):
    """
    Нахождение произведения цифр числа, до определённой цифры
    :param num: число
    :param lim: до какой цифры ищем, если 0 все цифры числа
    :return: произведение цифр
    """
    multiply = 1
    lim = 10 ** lim if lim > 0 else 0
    while num > lim:
        num, mod = divmod(num, 10)
        # print(f"number - {num}, mod - {mod}")
        multiply *= mod
    return multiply


def find_index_min_element(sours: list):
    """
    Нахождение индекса минимального элемента массива
    :param sours: массив элементов int
    :return: индекс минимального элемента
    """
    index = 0
    min_num = sours[0]
    for k in range(1, len(sours)):
        if sours[k] < min_num:
            min_num = sours[k]
            index = k
    return index


def create_array_by_condition(source: list, mod: int, start=-1):
    new_list = list()
    for k in range(start + 1, array_size):
        if source[k] % 2 == 0 and source[k] % mod != 0:
            new_list.append(source[k])
    return new_list


print(TASK)
array_size = input_data()
generated_array = create_array(array_size, 1001, 9999)
print("Сгенерированный массив: ", *generated_array)

multi_array = [multiply_digit(el, lim=1) for el in generated_array]
print("Массив произведений цифр элементов: ", *multi_array)

min_index = find_index_min_element(multi_array)
print(f"Индекс элемента с min произведением цифр - {min_index}\n"
      f"Значение элемента с min произведением цифр - {multi_array[min_index]}")

modify_array = [el for el in generated_array]
modify_array[min_index] = min_index
print("Модифицированный массив: ", *modify_array)

from random import randint

TASK = '''
В массиве хранится информация о количестве людей, живущих на каждом из N этажей дома.
Определить два этажа, на которых проживает меньше всего людей.
Отсортировать массив по возрастанию
'''


def input_data():
    count = 1
    while True:
        floors = input("Введите количество этажей в доме, значение должно быть от 2 до 100: ")
        if floors.isdigit():
            if 1 < int(floors) < 101:
                return int(floors)
            else:
                print("Количество этажей должно быть от 2 до 100\nПопробуйте ещё раз.")
        else:
            print("Ошибка. Вы можете вводить только числа, состоящие из цифр, а не текст!!!"
                  "\nПопробуйте ещё раз.")
        if count == 3:
            print("Извините, но количество попыток закончилось")
            exit()
        count += 1


def bubble_sort(sours: list):
    """
    Сортировка массива по возрастанию методом пузырька
    :param sours: неотсортированный массив типа int
    :return: отсортированный массив по возрастанию
    """
    len_list = len(sours)
    for pos in range(1, len_list):
        for k in range(0, len_list - pos):
            if sours[k] > sours[k + 1]:
                sours[k], sours[k + 1] = sours[k + 1], sours[k]
    return sours


def get_index_minimum_values(sours_list: list):
    """
    Функция нахождения индексов двух минимальных значений в списке
    :param sours_list: список значений
    :return: индексы минимальных значений
    """
    # min1 = 0
    # min2 = 1
    # if sours_list[0] > sours_list[1]:
    #     min1 = 1
    #     min2 = 0

    min1, min2 = (0, 1) if sours_list[0] < sours_list[1] else (1, 0)
    for index in range(2, len(sours_list)):
        if sours_list[index] < sours_list[min1]:
            min2 = min1
            min1 = index
        elif sours_list[index] < sours_list[min2]:
            min2 = index
    return min1, min2


print(TASK)
number_floors = input_data()
residents_on_floor = list(randint(10, 50) for floor in range(number_floors))
print("Количество жильцов по этажам: ", *residents_on_floor)

min_resident_floor1, min_resident_floor2 = get_index_minimum_values(residents_on_floor)
print("Первый этаж на котором проживает меньше всего людей - ", min_resident_floor1 + 1)
print("Второй этаж на котором проживает меньше всего людей - ", min_resident_floor2 + 1)

bubble_sort(residents_on_floor)
print("Отсортированный массив: ", *residents_on_floor)

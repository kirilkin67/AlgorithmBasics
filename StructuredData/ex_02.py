from random import randint

TASK = '''
Лабораторная работа №4
Даны два массива из N однозначных чисел. В первом из них записано
количество мячей, забитых футбольной командой в игре, во втором -
количество пропущенных мячей в этой же игре.
Определить количество выигрышей данной команды.
Создать массив с данными содержащие соотношение количество забитых и пропущенных мячей.
'''


def input_data():
    count = 1
    while True:
        value = input("Введите количество игр сыгранной командой, значение должно быть больше 1: ")
        if value.isdigit():
            value = int(value)
            if value > 0:
                return value
            else:
                print("Количество игр должно быть больше 1\nПопробуйте ещё раз.")
        else:
            print("Ошибка. Вы можете вводить только числа, состоящие из цифр, а не текст!!!"
                  "\nПопробуйте ещё раз.")
        if count == 3:
            print("Извините, но количество попыток закончилось")
            exit()
        count += 1


def get_count_max_values(sours1: list, sours2: list):
    """
    Функция сравнения значений двух списков, если значение 1 списка больше 2
    :param sours1: первый список int
    :param sours2: второй список int
    :return: количество значений
    """
    count = 0
    for k in range(len(sours1)):
        if sours1[k] > sours2[k]:
            count += 1
    return count


def create_union_list(sours1: list, sours2: list):
    # union_list = list()
    # for k in range(len(sours1)):
    #     union_list.append([sours1[k], sours2[k]])
    # return union_list
    return [[sours1[k], sours2[k]] for k in range(len(sours1))]


print(TASK)
games = input_data()
scored_goals = list(randint(0, 8) for _ in range(games))
conceded_goals = list(randint(0, 8) for _ in range(games))
print("Забитые мячи: ", scored_goals)
print("Пропущенные мячи: ", conceded_goals)
print("Количество выигрышей команды - ", get_count_max_values(scored_goals, conceded_goals))
print("Соотношение количества забитых и пропущенных мячей\n", *create_union_list(scored_goals, conceded_goals))

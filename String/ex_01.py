TASK = '''
Лабораторная работа №6
Дан текст. Подсчитать самую длинную последовательность подряд идущих
букв Х(вводится с клавиатуры).
Преобразовать её, заменив точками все восклицательные знаки.
'''


def max_sequence_letter(source: str, ch: str):
    """
    Функция поиска максимальной последовательности подряд идущих букв
    :param source: искомый текст
    :param ch: искомая буква
    :return: 0 или максимальная последовательность
    """
    count = 0
    max_count = 0
    for letter in source:
        if letter == ch:
            count += 1
            if count > max_count:
                max_count = count
        else:
            count = 0
    print(f"Максимальная последовательность подряд идущих букв '{ch}' - {max_count}")
    return max_count


print(TASK)
text = input("Введите текст: ")
char = input("Введите букву: ")
max_sequence_letter(text, char)
print("Преобразованный текст:\n", text.replace('!', '.'))

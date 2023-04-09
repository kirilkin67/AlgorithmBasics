try:
    integer = int(input("Введите трёхзначное положительное число:\n"))
    if 99 < integer < 1000:
        NUMBER = integer
        first_num, integer = divmod(integer, 100)
        second_num, third_num = divmod(integer, 10)
        if first_num == third_num:
            print(f"Результат преобразования числа:\n{NUMBER}")
        elif third_num == 0:
            integer = second_num * 10 + first_num
            print(f"Результат преобразования числа:\n{integer}")
        else:
            integer = third_num * 100 + second_num * 10 + first_num
            print(f"Результат преобразования числа:\n{integer}")
    elif integer < 0:
        print("Ошибка. Вы ввели отрицательное число")
        exit()
    else:
        print("Ошибка. Вы ввели не трёхзначное число")
        exit()
except ValueError:
    print("Ошибка. Вы можете вводить только числа, состоящие из цифр, а не текст!!!")
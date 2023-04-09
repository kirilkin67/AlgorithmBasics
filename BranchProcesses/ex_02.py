try:
    integer = int(input("Введите трёхзначное положительное число:\n"))
    sign = 1
    if integer < 0:
        sign = -1
        integer = -integer
    if 99 < integer < 1000:
        NUMBER = integer
        first_num, integer = divmod(integer, 100)
        second_num, third_num = divmod(integer, 10)
        if first_num == third_num:
            print(f"Результат преобразования числа:\n{sign * NUMBER}")
        elif third_num == 0:
            integer = second_num * 10 + first_num
            print(f"Результат преобразования числа:\n{sign * integer}")
        else:
            integer = third_num * 100 + second_num * 10 + first_num
            print(f"Результат преобразования числа:\n{sign * integer}")
    else:
        print("Ошибка. Вы ввели не трёхзначное число")
except ValueError:
    print("Ошибка. Вы можете вводить только числа, состоящие из цифр, а не текст!!!")

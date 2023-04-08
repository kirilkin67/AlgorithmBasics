try:
    integer = int(input("Введите трёхзначное число:\n"))
    if 99 < integer < 1000:
        first_num, integer = divmod(integer, 100)
        second_num, third_num = divmod(integer, 10)
        integer = (second_num * 100 + first_num * 10 + third_num) * 2
        print(f"Результат преобразования числа:\n{integer}")
    else:
        print("Ошибка. Вы ввели не трёхзначное число")
        exit()
except ValueError:
    print("Ошибка. Вы можете вводить только числа, состоящие из цифр, а не текст!!!")

try:
    year = int(input("Введите номер года:\n"))
    if year >= 0:
        if year == 0:
            print("В этом году 365 дней")
        elif year % 400 == 0 or (year % 4 == 0 and year % 100 != 0):
            print("В этом году 366 дней")
        # elif year % 4 == 0 and year % 100 != 0:
        #     print("В этом году 366 дней")
        else:
            print("В этом году 365 дней")
    else:
        print("Ошибка. Год не может быть отрицательным числом")
except ValueError:
    print("Ошибка. Вы можете вводить только числа, состоящие из цифр, а не текст!!!")

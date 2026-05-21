def digit_sum(number):  # вычисляем и возвращаем сумму чисел
    digits_list = [int(n) for n in str(number)]
    return sum(digits_list)


def digit_root(num):  # рекурентно вычисляем сумму чисел пока не получим цифровой корень

    dig_root = digit_sum(num)
    while True:
        dig_root = digit_sum(num)
        if 1 <= dig_root <= 9:
            return dig_root
            break
        else:
            num = dig_root

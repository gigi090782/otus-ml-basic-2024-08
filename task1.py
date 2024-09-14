def get_digit_of_number(num: int):
    result = 0
    while num > 0:
        result+= num % 10
        num = num // 10
    if result > 9:
        return get_digit_of_number(result)
    return result

num_string = input("Введите число для преобразования: ")
if (not(num_string.isnumeric()) or (num_string.find('.') != -1)):
    print("Ошибка! Введено не целое число!")
else:
    print(f"Преобразованное число: {get_digit_of_number(int(num_string))}")

assert get_digit_of_number(545) == 5, "Неверное преобразование"
assert get_digit_of_number(12345) == 6, "Неверное преобразование"

input_string = input("Введите число для преобразования в римскую систему: ")

if (not(input_string.isnumeric())):
    print("Ошибка! Введено не число!")
else:
    roman_nums = [(1000, 'M'), (900, 'CM'), (500, 'D'), (400, 'CD'), (100, 'C'), (90, 'XC'), (50, "L"), (40, 'XL'),
                  (10, 'X'), (9, 'IX'), (5, 'V'), (4, 'IV'), (1, 'I')]
    num_to_convert = int(input_string)
    converted_num = ''

    while num_to_convert > 0:
        for num_roman, symbols_roman in roman_nums:
            while num_to_convert >= num_roman:
                converted_num += symbols_roman
                num_to_convert -= num_roman

    print(f"Полученное число в римской системе: {converted_num}")

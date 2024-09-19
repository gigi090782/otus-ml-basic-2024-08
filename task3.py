def is_simple_number(number : int)-> bool:
    if number == 1 or number == 2:
        return True
    for i in range(2,number):
        if number%i == 0:
            return False
    return True

assert is_simple_number(1) == True, "Неверная проверка"
assert is_simple_number(2) == True, "Неверная проверка"
assert is_simple_number(17) == True, "Неверная проверка"
assert is_simple_number(20) == False, "Неверная проверка"
assert is_simple_number(23) == True, "Неверная проверка"

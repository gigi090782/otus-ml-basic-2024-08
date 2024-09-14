
def encrypt_string(input_string: str, offset: int):
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    result_string = ""
    for symbol in input_string:
        if symbol == " ":
            result_string += " "
            continue
        if alphabet.find(symbol.lower()) == -1:
            raise Exception("Недопустимый символ!")
        result_symbol =  alphabet[(alphabet.index(symbol.lower()) + offset) % len(alphabet)]
        if (symbol.isupper()):
            result_string += result_symbol.upper()
        else:
            result_string += result_symbol
    return result_string

input_string = input("Введите строку для преобразования: ")
offset_string = input("Введите сдвиг: ")
if (len(input_string) == 0 or (not offset_string.isnumeric())):
    print("Введены невалидные данные!")
else:
    print(f"Преобразованная строка: {encrypt_string(input_string, int(offset_string))}")

    assert encrypt_string("Dog", 2) == "Fqi", "Неверное шифрование"
    assert encrypt_string("Zak zak", 3) == "Cdn cdn", "Неверное шифрование"
    assert encrypt_string("Python is the BEST", 5) == "Udymts nx ymj GJXY", "Неверное шифрование"
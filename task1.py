from enum import Enum

class Code_style(Enum):
    CAMEL = 1
    SNAKE = 2
    UNDEFINED = 3

def check_upper_case (input_string: str) -> bool:
    """
    Функция для проверки наличия букв в верхнем регистре
    :param input_string: входная строка
    :return: True/False
    """
    for symbol in input_string:
        if symbol.isupper():
            return True
    return False

def get_code_style(input_string: str) -> Code_style:
    """
    Функция для определения стиля кода
    :param input_string: входная строка
    :return: стиль кода
    """
    if input_string.find("_") != -1:
        return Code_style.SNAKE
    elif check_upper_case (input_string):
        return Code_style.CAMEL
    return Code_style.UNDEFINED

def convert_to_snake_case (input_string: str) -> str:
    """
    Функция для преобразования входной строки к стилю snake_case
    :param input_string: входная строка
    :return: преобразованная строка
    """
    result_string = input_string[0].lower()
    index = 1
    while index < len(input_string):
        if str(input_string[index]).isupper():
            result_string += "_"
        result_string+=input_string[index].lower()
        index += 1
    return result_string


def convert_to_camel_case (input_string: str) -> str:
    """
    Функция для преобразования входной строки к стилю camel_case
    :param input_string: входная строка
    :return: преобразованная строка
    """
    result_string = input_string[0].upper()
    index = 1
    while index < len(input_string):
        if input_string[index] != "_":
            result_string += input_string[index]
        else:
            index +=1
            result_string+=input_string[index].upper()
        index += 1
    return result_string

def change_code_style(input_string: str, need_revert: bool = True, code_style: Code_style = Code_style.CAMEL) -> str:
    """
    Функция изменяющая стиль кода для введенной строки
    :param input_string: входная строка
    :param need_revert: необходимость конвертировать snake_case->camel_case и camel_case->snake_case
    :param code_style: если задано need_revert = False, то учитывается параметр code_style для принудительного преобразования в выбранный стиль
    :return: преобразованная строка
    """
    input_string_code_style = get_code_style(input_string)
    if not need_revert:
        if code_style == input_string_code_style:
            return input_string
        elif code_style == Code_style.CAMEL:
            return convert_to_camel_case(input_string)
        elif code_style == Code_style.SNAKE:
            return convert_to_snake_case(input_string)
        else:
            raise Exception("Неверные данные!")
    else:
        if input_string_code_style == Code_style.CAMEL:
            return convert_to_snake_case(input_string)
        elif input_string_code_style == Code_style.SNAKE:
            return convert_to_camel_case(input_string)
        else:
            raise Exception("Неверные данные!")

assert change_code_style("otus_course", True) == "OtusCourse", "Неверное преобразование"
assert change_code_style("PythonIsTheBest", True) == "python_is_the_best", "Неверное преобразование"
assert change_code_style("otus_course", False, Code_style.CAMEL) == "OtusCourse", "Неверное преобразование"
assert change_code_style("otus_course", False, Code_style.SNAKE) == "otus_course", "Неверное преобразование"
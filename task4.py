result_dict = dict()
right_symbols_for_name = 'abcdefghijklmnopqrstuvwxyzабвгдеёжзийклмнопрстуфхцчшщьъэюя -'

def get_correct_name(input_name:str)->str:
    while input_name.find("  ")!=-1:
        input_name = input_name.replace("  "," ")
    while input_name.find("--") != -1:
        input_name = input_name.replace("--", "-")
    while input_name.find("- ") != -1:
        input_name = input_name.replace("- ", "-")
    while input_name.find(" -") != -1:
        input_name = input_name.replace(" -", "-")
    result_string = input_name[0].upper()
    if len(input_name) > 1:
        index = 1
        while index < len(input_name):
            if ((input_name[index] != " " and input_name[index-1] == " ") or
                (input_name[index] != "-" and input_name[index-1] == "-")):
                result_string += input_name[index].upper()
            else:
                result_string += input_name[index]
            index += 1
    return result_string

def validate_name(input_text:str, input_text_name:str):
    if len(input_text) == 0:
        raise Exception(f"Отсутствует значение для {input_text_name}!")
    for symbol in input_text:
        if right_symbols_for_name.find(symbol.lower()) == -1:
            raise Exception(f"Введен недопустимый символ {symbol} в {input_text_name}!")

def validate_input_data(input_list):
    if len(input_list) != 4:
        raise Exception("Введено недостаточное количество значений!")
    validating_user_id = str(input_list[3]).strip()
    if not validating_user_id.isnumeric() or validating_user_id.find(".") != -1 or len(validating_user_id) > 8:
        raise Exception("Неверно введен ID пользователя")
    age = str(input_list[2]).strip()
    if not age.isnumeric() or age.find(".") != -1:
        raise Exception("Неверно введен возраст пользователя: должен быть целым числом")
    if int(age)<18 or int(age)>60:
        raise Exception("Возраст пользователя должен быть от 18 до 60")
    validate_name(input_list[0].strip(), "имени")
    validate_name(input_list[1].strip(), "фамилии")

def get_correct_user_id(input_user_id:str)->str:
    if len(input_user_id)==8:
        return user_id
    return "0"*(8-len(input_user_id))+input_user_id

def get_value_for_print(value:str, count_symbols:int)->str:
    if len(value)==count_symbols:
        return value
    return value+" "* (count_symbols-len(value))

def get_max_size_field(field_index:int)->int:
    max_size_field = -1
    for key, value in result_dict.items():
        if len(str(value[field_index]))>max_size_field:
            max_size_field=len(str(value[field_index]))
    return max_size_field

def print_result_dict():
    if len(result_dict) == 0:
        raise Exception("Отсутствуют данные для печати!")
    max_size_name = get_max_size_field(0)
    max_size_surname = get_max_size_field(1)
    common_len_table = 20+max_size_name+max_size_surname
    print("-"*common_len_table)
    print("|ID      |"+get_value_for_print("Имя",max_size_name)+"|"+get_value_for_print("Фамилия",max_size_surname)
          +"|Возраст|")
    for key, value in sorted(result_dict.items()):
        print("|"+key+"|"+get_value_for_print(str(value[0]), max_size_name)+"|"
              +get_value_for_print(str(value[1]), max_size_surname)+"|"
              +str(value[2])+" "*5+"|")
    print("-"*common_len_table)

print("Введите данные пользователя через запятую: имя, фамилия, возраст и ID")
while True:
    input_string = input()
    if len(input_string) == 0:
        break
    split_string = input_string.strip().split(",")
    validate_input_data(split_string)
    user_id = get_correct_user_id(split_string[3].strip())
    name = get_correct_name(split_string[0].strip())
    surname = get_correct_name(split_string[1].strip())
    if result_dict.get(user_id) is not None:
        raise Exception("Введено неуникальное значение ID!")
    result_dict.update({user_id:(name, surname, int(split_string[2].strip()))})
print_result_dict()
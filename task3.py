
def get_string_in_rle_algorithm(input_string: str):
    if (len(input_string) == 1):
        return f"1{input_string}"
    result_string = ""
    symbol = input_string[0]
    count_symbol = 1
    for i in range(1, len(input_string)):
        if input_string[i] == symbol:
            count_symbol+=1
        else:
            result_string+=f"{count_symbol}{symbol}"
            count_symbol = 1
            symbol = input_string[i]
    return result_string+f"{count_symbol}{symbol}"


input_string = input("Введите строку для преобразования: ")
if (len(input_string) == 0):
    print("Строка не введена!")
else:
    print(f"Преобразованная строка: {get_string_in_rle_algorithm(input_string)}")


assert get_string_in_rle_algorithm("aaabbbbccccc") == "3a4b5c", "Неверное преобразование"
assert get_string_in_rle_algorithm("asssdddsssddd") == "1a3s3d3s3d", "Неверное преобразование"
assert get_string_in_rle_algorithm("abcba") == "1a1b1c1b1a", "Неверное преобразование"
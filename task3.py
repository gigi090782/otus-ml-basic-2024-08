input_string = input("Введите длину, ширину плитки шоколада и размер куска, который хотите отломить через запятую: ")
input_list = input_string.split(",")

if (len(input_list)<3):
    raise Exception("Недостаточно данных!")

length_string = input_list[0]
width_string = input_list[1]
size_string = input_list[2]

if ((not(length_string.isnumeric())) or
        (not(width_string.isnumeric())) or
        (not(size_string.isnumeric()))):
    print("Ошибка! Введено не число!")
else:
    length_num = int(length_string)
    width_num = int(width_string)
    size_num = int(size_string)

    if(((size_num % length_num == 0) and (size_num // length_num<=width_num)) or
            ((size_num % width_num == 0) and (size_num // width_num <= width_num))):
        print("True")
    else:
        print("False")

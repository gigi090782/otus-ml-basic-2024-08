num_string = input("Введите пятизначное число:")
if((not(num_string.isnumeric())) or (len(num_string)!=5)):
    print("Ошибка! Введено не пятизначное число!")
else:
    list_string = list(num_string)
    list_string[1],list_string[3]=list_string[3],list_string[1]
    new_string = ''.join(list_string)
    print(f"Новое число, где заркально отражены центральные три цифры: {new_string}")

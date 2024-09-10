input_string = input("Введите число для проверки: ")
index = 0
dot_index = -1
for symbol in input_string:
    if (index == 0):
        if (not(symbol == '.' or symbol == '-' or symbol.isnumeric())):
            print('False')
            exit()
        else:
            if(symbol == '.'):
                dot_index = index
    else:
        if (not(symbol == '.' or symbol.isnumeric())):
            print('False')
            exit()
        else:
            if(symbol == '.'):
                if (dot_index > -1):
                    print('False')
                    exit()
    index += 1

if (dot_index == index):
    print('False')
else:
    print('True')
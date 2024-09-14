
def get_available_row_of_cinema(rows_of_cinema, count_of_tickets):
    str_result = "Доступный ряд для покупки билетов: "
    for i in range (len(rows_of_cinema)):
        count_available_sits = 0
        for j in range (len(rows_of_cinema[i])):
            if (rows_of_cinema[i][j] == 0):
                count_available_sits += 1
                if (count_available_sits == count_of_tickets):
                    return str_result+ str(i)
            else:
                count_available_sits = 0
    return  str_result+"False"


count_of_tickets_string = input("Введите число билетов: ")
if (not(count_of_tickets_string.isnumeric())):
    print("Ошибка! Введено не число!")
else:
    count_of_tickets = int(count_of_tickets_string)
    print("Кинотеатр 1: "+ get_available_row_of_cinema([[0,1,1,0], [1, 0, 0, 0], [0,1,0,0]],count_of_tickets ))
    print("Кинотеатр 2: "+ get_available_row_of_cinema([[0,1,1,0], [1, 0, 1, 0], [1,1,0,1]],count_of_tickets ))
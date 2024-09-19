

list_month_days = [31,28,31,30,31,30,31,31,30,31,30,31]

def validate_is_date_format_string(input_date_string:str) -> bool:
    index = 0
    input_date_string = input_date_string.strip()
    while index<len(input_date_string):
        if index==2 or index == 5:
            if input_date_string[index]!=".":
                return False
        else:
            if not input_date_string[index].isnumeric():
                return False
        index += 1
    return True

def is_leap_year(day: int, month: int, year: int)-> bool:
    if month == 2:
       if year%400 == 0:
           return True
       elif year % 100 == 0:
           return day <= False
       elif year % 4 == 0:
            return day <= True
    return False

def validate_date(input_date_string:str) ->bool:
    if not validate_is_date_format_string(input_date_string):
        return False
    date_list = input_date_string.strip().split(".")
    day = int(date_list[0])
    month = int(date_list[1])
    year = int(date_list[2])
    if is_leap_year(day,month,year):
       return day <= list_month_days[month - 1] + 1
    return day <= list_month_days[month - 1]

assert validate_date("29.02.2000") == True, "Неверная проверка"
assert validate_date("29.02.2001") == False, "Неверная проверка"
assert validate_date("31.04.1962") == False, "Неверная проверка"
assert validate_date("3в.04.1962") == False, "Неверная проверка"



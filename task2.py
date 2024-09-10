days_to_holiday_string = input("Введите количество дней до отпуска: ")
if (not(days_to_holiday_string.isnumeric())):
    print("Ошибка! Введено не число!")
else:
    days_to_holiday = int(days_to_holiday_string)
    count_weekends_days = (days_to_holiday//7)*2
    if (((days_to_holiday%7)-5)>0):
        count_weekends_days+=(days_to_holiday%7)-5
    print(f"Количество выходных дней до отпуска: {count_weekends_days}")


result_dict = dict()
print("Введите название предмета, фамилию ученика и оценку через запятую: ")
while True:
    input_string = input()
    if len(input_string) == 0:
        break
    split_string = input_string.strip().split(" ")
    if len(split_string) != 3:
        raise Exception("Введено недопустимой значение!")
    dict_surnames = result_dict.get(split_string[0]);
    if (dict_surnames == None):
        result_dict.update({split_string[0]: {split_string[1]: list(split_string[2])}})
    else:
        marks = dict_surnames.get(split_string[1])
        if (marks==None):
            dict_surnames.update({split_string[1]: list(split_string[2])})
        else:
           marks.append(split_string[2])

print("Результаты:")
for key_subject, value_subject in result_dict.items():
    print(key_subject)
    for key_surname, value_surname in result_dict.get(key_subject).items():
        print(key_surname+" "+  ','.join(value_surname))

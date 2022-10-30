# Ваша задача: починить адресную книгу, используя регулярные выражения.
# Структура данных будет всегда:
# lastname,firstname,surname,organization,position,phone,email
# Предполагается, что телефон и e-mail у человека может быть только один.
# Необходимо:
# (1) поместить Фамилию, Имя и Отчество человека в поля lastname, firstname и surname соответственно. - DONE
# (1)В записной книжке изначально может быть Ф + ИО, ФИО, а может быть сразу правильно: Ф+И+О;
# (2) привести все телефоны в формат +7(999)999-99-99. Если есть добавочный номер, формат будет такой:
# (2) +7(999)999-99-99 доб.9999;
# (3) объединить все дублирующиеся записи о человеке в одну.

import re
from pprint import pprint
import csv


def open_phonebook_raw():
    # читаем адресную книгу в формате CSV в список contacts_list
    with open("phonebook_raw.csv") as f:
        rows = csv.reader(f, delimiter=",")
        contacts_list = list(rows)
    return contacts_list

def name_split1(contacts_list):
    for i,val in enumerate(contacts_list):
        if i > 0:
            result_ = val[0]
            result = re.split('\s', result_)
            # print(result)
            for x,val_result in enumerate(result):
                name_split = result[x]
                contacts_list[i][x] = name_split
    return contacts_list

def name_split2(contacts_list1):
    for i, val in enumerate(contacts_list1):
        if i > 0:
            result_ = val[1]
            result = re.split('\s', result_)
            # print(result)
            for x, val_result in enumerate(result):
                name_split = result[x]
                contacts_list1[i][x+1] = name_split
    return contacts_list1

    # TODO 2: сохраните получившиеся данные в другой файл
    # код для записи файла в формате CSV
    # with open("phonebook.csv", "w") as f:
    #     datawriter = csv.writer(f, delimiter=',')
    #     # Вместо contacts_list подставьте свой список
    #     datawriter.writerows(contacts_list)

if __name__ == '__main__':
    contacts_list = open_phonebook_raw()
    pprint(contacts_list)
    print('')
    print('Name split 1st iteration')
    print('')
    contacts_list1 = name_split1(contacts_list)
    pprint(contacts_list1)
    print('')
    print('Name split 2nd iteration')
    print('')
    contacts_list2 = name_split2(contacts_list1)
    pprint(contacts_list2)

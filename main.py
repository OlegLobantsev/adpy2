from pprint import pprint
# читаем адресную книгу в формате CSV в список contacts_list
import csv
import re

with open("phonebook_raw.csv") as f:
    rows = csv.reader(f, delimiter=",")
    contacts_list = list(rows)
pprint(contacts_list)


# TODO 1: выполните пункты 1-3 ДЗ

def reformat_number(phonebook):
    for el in phonebook:
        name = ' '.join(el[:3])
        sep_name = name.split(' ')
        result = [sep_name[0], sep_name[1], sep_name[2],
                  el[3], el[4],
                  re.sub(r"(\+7|8)?\s?\(?(\d{3})\)?[-|\s]*(\d{3})[-]*(\d{2})[-]*(\d{2})\s*\(?(\w*\.)?\s?(\d*)\)?",
                         r"+7(\2)\3-\4-\5 \6\7", el[5]),
                  el[6]]
        new_contacts_list.append(result)


def remove_duplicates(phonebook):
    for el in phonebook:
        surname = el[0]
        name = el[1]
        for el_2 in phonebook:
            new_surname = el_2[0]
            new_name = el_2[1]
            if surname == new_surname and name == new_name:
                index = 2
                while index <= 6:
                    if el[index] == '':
                        el[index] = el_2[index]
                    index += 1
    for element in phonebook:
        if element not in normal_list:
            normal_list.append(element)


if __name__ == '__main__':
    new_contacts_list = []
    normal_list = []
    reformat_number(contacts_list)
    remove_duplicates(new_contacts_list)

# TODO 2: сохраните получившиеся данные в другой файл
# код для записи файла в формате CSV

    with open("phonebook.csv", "w") as f:
        datawriter = csv.writer(f, delimiter=',')
        datawriter.writerows(normal_list)
    pprint(normal_list)

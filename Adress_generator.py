import random
import json
import re

"""Функция для считывания данных из json файла и проверки их на корректность.
Названия улиц должны быть строкой, в ней допускаются прописные и строчные буквы, цифры, дефисы и точки.
В файле данные записаны в виде словаря, значания двух первых полей - названия страны и города,
третьего - список улиц"""
def load_data(file_name):
    with open(file_name, "rt", encoding="UTF8") as f:
        new_str = f.read()
    g = json.loads(new_str)
    return g

def check_data(ll):
    for i in ll:
        if not isinstance(i, str):
            raise TypeError(f"Ошибка в строке {i} - неправильный тип данных")
        if not re.fullmatch(r"[A-ZА-Яa-zа-яё\-\d' '.]+", i):
            raise ValueError(f"Ошибка в строке {i} - название некорректно")



"""Декоратор для условного выполнения функции.
Если в аргументах, поданных в основную функцию, есть соответствие параметру декоратора,
то функция не запускается, вместо этого выводится строка 'test is here'"""


def decorator_maker(c):
    def check_dec(f):
        def inner(*ar):
            if c in ar[0] or c in ar[1] or c in ar[2]:
                print("test is here")
                return
            result = f(*ar)
            return result
        return inner
    return check_dec


"""Генератор случайных адресов.
Возвращает словарь, значения которого преобразуются в строку с адресом.
Названия страны, города и улиц считываются из внешнего файла, проверяются на корректрность.
Номера дома, корпуса (не обязательная позиция) и квартры генерируются с помощью модуля random.
В случае, если в адресе нет корпуса, для поля генерируется значение None, которое удаляется при выводе адреса в консоль"""


@decorator_maker("test")
def address_gen(countries_list, cities_list, streets_list):
    while True:
        some_address = {"country": countries_list[0], "city": cities_list[1],
                       "street": random.choice(streets_list), "num_build": random.randint(1, 200),
                       "corp": random.randint(1, 6) if random.randint(1, 100) % 5 == 0 else None,
                       "num_flat": random.randint(1, 500)}
        yield some_address

def main():
    res = load_data("_Adr.json")
    check_data(res["countries"])
    check_data(res["cities"])
    check_data(res["streets"])
    f = address_gen(res["countries"], res["cities"], res["streets"])
    if f:

        for i in range(5):
            a = next(f)
            print(a)

#v = list(next(f).values())
    # if None in v:
    #     v.remove(None)
    # a = ", ".join(map(str, v))

if __name__ == '__main__':
    main()


# import json
# adr = {"country": "Россия", "city": "Санкт-Петербург",
#        "street": ["test", "улица Пионерская","улица Лодейнопольская", "улица Гатчинаская",
#                  "улица Ораниенбаумская", "Большой проспект П.С.", "проспект Славы", "улица Турку", "улица Луначарского",
#                  "Поэтический бульвар", "пропект Юрия Гагарина", "улица Некрасова", "Литейный проспект", "улица Эриванская"]}
# adr_str = json.dumps(adr)
# with open(r"_Adr.py", "wt", encoding="UTF8") as f:
#     f.write(adr_str)
#_Adr.json
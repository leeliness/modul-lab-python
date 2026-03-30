import os
from functions import process_numbers, compare_positive, translate

FILE_NAME = "MyData.txt"

def read_data():
    try:
        with open(FILE_NAME, "r") as f:
            lines = f.readlines()
            a, b, c = map(int, lines[0].split())
            lang = lines[1].strip()
            return a, b, c, lang
    except:
        return None


def write_data(a, b, c, lang):
    with open(FILE_NAME, "w") as f:
        f.write(f"{a} {b} {c}\n")
        f.write(lang)


data = read_data()

if data is None:
    a, b, c = map(int, input("Введіть три числа a, b, c: ").split())
    lang = input("Введіть мову інтерфейсу: ")

    write_data(a, b, c, lang)
    print(f"Дані збережено в файл {FILE_NAME}")

else:
    a, b, c, lang = data

    print(translate("language", lang))
    print(f"{translate('input', lang)} {a} {b} {c}")
    print(translate("task", lang))

    x, y, z = process_numbers(a, b, c)
    print(x, y, z)

    print(compare_positive(a, b, c))
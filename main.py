import json
from functions import process_numbers, compare_positive, translate_text

FILE_NAME = "MyData.json"


def read_data():
    try:
        with open(FILE_NAME, "r") as f:
            data = json.load(f)
            return data["a"], data["b"], data["c"], data["lang"]
    except:
        return None


def write_data(a, b, c, lang):
    data = {"a": a, "b": b, "c": c, "lang": lang}
    with open(FILE_NAME, "w") as f:
        json.dump(data, f)


data = read_data()

if data is None:
    a, b, c = map(int, input("Введіть три числа a, b, c: ").split())
    lang = input("Введіть мову інтерфейсу (en/uk): ")

    write_data(a, b, c, lang)
    print(f"Дані збережено в файл {FILE_NAME}")

else:
    a, b, c, lang = data

    print(translate_text("Language:", lang))
    print(translate_text("Three numbers a, b, c:", lang), a, b, c)
    print(translate_text("Processing numbers...", lang))

    x, y, z = process_numbers(a, b, c)
    print(x, y, z)

    print(compare_positive(a, b, c))
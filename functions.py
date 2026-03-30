def process_numbers(a, b, c):
    def transform(x):
        if x > 0:
            return x ** 3
        else:
            return 0

    return transform(a), transform(b), transform(c)


def compare_positive(a, b, c):
    positives = [x for x in [a, b, c] if x > 0]

    if len(positives) < 2:
        return "Недостатньо додатних чисел"

    positives.sort()
    return f"{positives[0] ** 3} < {positives[1] ** 3}"


def translate(text, lang):
    translations = {
        "uk": {
            "language": "Мова: Українська",
            "input": "Три числа a, b, c:",
            "task": "Додатні возвести в куб, а від’ємні замінити на 0, порівняти додатні числа:"
        },
        "en": {
            "language": "Language: English",
            "input": "Three numbers a, b, c:",
            "task": "Positive numbers cubed, negative replaced with 0:"
        }
    }

    if lang not in translations:
        lang = "uk"

    return translations[lang][text]
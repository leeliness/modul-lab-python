from translate import Translator


def process_numbers(a, b, c):
    def transform(x):
        if x > 0:
            return x ** 3
        return 0

    return transform(a), transform(b), transform(c)


def compare_positive(a, b, c):
    positives = [x for x in [a, b, c] if x > 0]

    if len(positives) < 2:
        return "Недостатньо додатних чисел"

    positives.sort()
    return f"{positives[0] ** 3} < {positives[1] ** 3}"


def translate_text(text, lang):
    try:
        translator = Translator(to_lang=lang)
        return translator.translate(text)
    except:
        return text
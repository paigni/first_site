import re


def regular_strings(regular, text):
    try:
        if re.compile(regular):
            match = re.search(rf'{regular}', rf'{text}')
            if match:
                return print('Совпадения найдены')
            if not match:
                return print('Совпадения не найдены')
    except:
        print('Регулярное выражение не верно')
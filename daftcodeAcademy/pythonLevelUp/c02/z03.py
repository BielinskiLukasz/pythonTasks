# Napisz dekorator @add_date,  który opakowuje funkcję zwracającą słownik. Dekorator ma dodać aktualną datę do zwracanego przez dekorowaną funkcję słownika w formacie podanym jako argument dekoratora.
#
# Użyj modułu datetime korzystając z datetime.datetime.now() do pobrania aktualnej daty. Więcej informacji o formatowaniu znajdziesz tutaj:
# https://docs.python.org/3/library/datetime.html#strftime-and-strptime-behavior
#
# Przykład:
#
# @add_date('%A %d. %B %Y')
# def get_data():
#     return {1: 2, 'name': 'Jan'}
#
#
# assert get_data() == {
#     1: 2, 'name': 'Jan', 'date': 'Sunday 17. March 2019'
# }
#
# Dodatkowo sprawdź czy możesz użyć dwóch dekoratorów: @add_date oraz @is_correct z poprzedniego zadania oraz zastanów się w jakiej kolejności zostaną wywołane oraz czy wynik będzie poprawny.
#
# Przykład:
#
# @is_correct('date')
# @add_date('%A %d. %B %Y')
# def get_data():
#     return {1: 2, 'name': 'Jan'}
#
#
# @add_date('%A %d. %B %Y')
# @is_correct('date')
# def get_data():
#     return {1: 2, 'name': 'Jan'}


import datetime  # do not change this import, use datetime.datetime.now() to get date


def add_date(format):
    def real_decorator(func):
        def wrapper(*args):
            result = func(*args)
            today = datetime.datetime.now()
            result['date'] = today.strftime(format)
            return result

        return wrapper

    return real_decorator

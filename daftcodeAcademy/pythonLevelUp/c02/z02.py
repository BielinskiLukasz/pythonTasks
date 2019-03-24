# Napisz dekorator @is_correct,  który opakowuje funkcję zwracającą słownik. Dekorator ma sprawdzić czy w słowniku znajdują się klucze zawarte w argumentach dekoratora. Jeśli tak niech zwróci ten słownik, jeśli nie, niech zwraca wartość None.
#
# Przykład:
#
# @is_correct('first_name', 'last_name')
# def get_data():
#     return {
#         'first_name': 'Jan',
#         'last_name': 'Kowalski',
#         'email': 'jan@kowalski.com'
#     }
#
#
# @is_correct('first_name', 'last_name', 'email')
# def get_other_data():
#     return {
#         'first_name': 'Jan',
#         'email': 'jan@kowalski.com'
#     }
#
#
# assert get_data() == {
#         'first_name': 'Jan',
#         'last_name': 'Kowalski',
#         'email': 'jan@kowalski.com'
#     }
#
#
# assert get_other_data() is None


def is_correct(*args):
    def real_decorator(to_be_decorated):
        def wrapper(*args_to_be_decorated, **kwargs):
            result = to_be_decorated(*args_to_be_decorated, **kwargs)
            is_in = True
            for x in args:
                if x in result.keys():
                    is_in = is_in and True
                else:
                    is_in = is_in and False
            if is_in:
                return result
            return None

        return wrapper

    return real_decorator

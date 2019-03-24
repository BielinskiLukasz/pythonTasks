# Napisz dekorator @to_list,  który opakowuje funkcję zwracającą tekst (iterable) oraz zwraca jej znaki (elementy) w postaci jednowymiarowej listy.
#
# Przykład:
#
# @to_list
# def say_python():
#     return 'Python'
#
#
# assert say_python() == ['P', 'y', 't', 'h', 'o', 'n']


def to_list(func):
    def inner():
        return list(func())

    return inner


@to_list
def say_python():
    return 'Python'

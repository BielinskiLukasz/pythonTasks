# Zadanie 3
# Napisz funkcję char_frequency, która przyjmuje jako argument string.
# Dla podanego stringa funkcja musi zliczyć ile razy wystąpiła każda litera.
# Zwróc wynik jako słownik wartości ile razy wystąpił każdy znak, gdzie klucz to występujący znak a wartścią
# jest liczba wystąpień tego znaku.


def char_frequency(string=""):
    result = {}
    for x in string:
        if x in result.keys():
            result[x] += 1
        else:
            result[x] = 1
    return result


assert char_frequency("576") == {'5': 1, '6': 1, '7': 1}
assert char_frequency() == {}
assert char_frequency('Ala ma kota, a kot kocha ale') == \
       {'e': 1, 'm': 1, 'a': 6, 'o': 3, 'k': 3, 'A': 1, 't': 2,
        ',': 1, ' ': 6, 'l': 2, 'c': 1, 'h': 1}

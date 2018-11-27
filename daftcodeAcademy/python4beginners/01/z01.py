# Wykład 1 - Zadanie 1
# Stwórz listę liczb od 0 do 999.

# Liczby podzielne przez 3 zastąp słowem 'Daftcode.
# Liczby podzielne przez 5 zastąp słowem 'Loves'.
# Liczby podzielne przez 7 zastąp słowem 'Python.
# Liczby podzielne jednocześnie przez 3 i 5 zastąp słowem 'DaftcodeLoves'
# Liczby podzielne jednocześnie przez 5 i 7 zastąp słowem 'LovesPython'.
# Liczby podzielne jednocześnie przez 3 i 7 zastąp słowem 'DaftcodePython'.
# Liczby podzielne jednocześnie przez 3, 5 i 7 zastąp słowem 'DaftcodeLovesPython'.

# Wynikową listę przypisz zmiennej result.

result = [x for x in range(1000)]
for x in result:
    if not x % (3 * 5 * 7):
        result[x] = 'DaftcodeLovesPython'
    elif not x % (3 * 7):
        result[x] = 'DaftcodePython'
    elif not x % (5 * 7):
        result[x] = 'LovesPython'
    elif not x % (3 * 5):
        result[x] = 'DaftcodeLoves'
    elif not x % (7):
        result[x] = 'Python'
    elif not x % (5):
        result[x] = 'Loves'
    elif not x % (3):
        result[x] = 'Daftcode'

assert result[2] == 2
assert result[3] == 'Daftcode'
assert result[5] == 'Loves'
assert result[7] == 'Python'
assert result[3 * 5] == 'DaftcodeLoves'
assert result[5 * 7] == 'LovesPython'
assert result[3 * 7] == 'DaftcodePython'
assert result[3 * 5 * 7] == 'DaftcodeLovesPython'

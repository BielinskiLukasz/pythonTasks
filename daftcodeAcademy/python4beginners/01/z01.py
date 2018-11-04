# zadanie 1

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

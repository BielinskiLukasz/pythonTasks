# zadanie 3

days = {
    1: 'Poniedziałek',
    2: 'Wtorek',
    3: 'Środa',
    4: 'Czwartek',
    5: 'Piątek',
    6: 'Sobota',
    7: 'Niedziela'
}

result = dict()
for n, d in days.items():
    result[d] = n

assert 'Poniedziałek' in result

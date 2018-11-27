# Wykład 1 - Zadanie 3
# Napisz kod transformujący podany słownik:

# {
#     1: "Poniedziałek',
#     2: 'Wtorek',
#     3: 'Środa',
#     4: 'Czwartek',
#     5: 'Piątek',
#     6: 'Sobota',
#     7: 'Niedziela',
# }

# do postaci (zamiana klucza z wartością):

# {
#     'Poniedziałek': 1,
#     'Wtorek': 2,
#     'Środa': 3,
#     'Czwartek': 4,
#     'Piątek': 5,
#     'Sobota': 6,
#     'Niedziela': 7,
# }

# Wynik przypisz do zmiennej result.

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

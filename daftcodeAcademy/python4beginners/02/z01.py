# Zadanie 1
# Napisz funkcję power, która dla danego n i p zwraca w wyniku n podniesione do potęgi p.
# Domyślna wartość argumentu p to 2.
# Załóż, że n i p będą liczbami całkowitymi >= 0.


def power(n, p=2):
    return n ** p if p > 0 else 1


assert power(5) == 25
assert power(5, 3) == 125

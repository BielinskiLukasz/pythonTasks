# zadanie 1

def power(n, p=2):
    return n ** p if p > 0 else 1


assert power(5) == 25
assert power(5, 3) == 125

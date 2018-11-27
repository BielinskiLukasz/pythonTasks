# Wykład 1 - Zadanie 4
# Napisz program tworzący ze zbioru U = {'👻', '🕵', '🔺', '🐉', '🐍', '🦂', '🔥', '🌻', '🐙', '🌌'} zbiór zawierający wszystkie podzbiory U (włącznie z pustym i U).

# UWAGA: w Pythonie zbiory (set) nie mogą być elementami innych zbiorów, proszę użyć frozenset jako zbiorów wewnętrznych.

# Wynik przypisz do zmienej result.

U = {'👻', '🕵', '🔺', '🐉', '🐍', '🦂', '🔥', '🌻', '🐙', '🌌'}

def powset(inputSet):
    powerset = set()
    powerset.add(frozenset())
    for x in list(inputSet):
        for n in list(powerset):
            temp = set(n)
            temp.add(x)
            powerset.add(frozenset(temp))
    return powerset

# shorthand
# result = {frozenset()}
# for x in U:
#     result |= {y | frozenset({x}) for y in result}

result = powset(U)

assert frozenset(('👻', '🕵', '🔺', '🐉', '🐍', '🦂', '🔥', '🌻', '🐙', '🌌')) in result

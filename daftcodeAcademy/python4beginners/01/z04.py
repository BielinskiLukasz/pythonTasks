# zadanie 4

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


result = powset(U)

assert frozenset(('👻', '🕵', '🔺', '🐉', '🐍', '🦂', '🔥', '🌻', '🐙', '🌌')) in result

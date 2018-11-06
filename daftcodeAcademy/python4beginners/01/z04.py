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


# shorthand
# result = {frozenset()}
# for x in U:
#     result |= {y | frozenset({x}) for y in result}

result = powset(U)

assert frozenset(('👻', '🕵', '🔺', '🐉', '🐍', '🦂', '🔥', '🌻', '🐙', '🌌')) in result

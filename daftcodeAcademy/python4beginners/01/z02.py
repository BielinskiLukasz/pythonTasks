# Wykład 1 - Zadanie 2
# Napisać kod tworzący listę list kolejnych elementów nieparzystych < 100 według schematu: [[1], [3], ... , [99]].

# Wynikową listę przypisz do zmiennej result.

result = [[x] for x in range(100) if x % 2]

assert result[1] == [3]

# Zadanie 5
# Napisz 2 funkcje:

# Jedna o nazwie prime ma sprawdzić czy zadana liczba n jest liczbą pierwszą, zwracając True/False.

# Druga funkcja twins ma sprawdzić czy dane liczby n, k są liczbami bliźniaczymi.
# Funkcja może przyjmować też jeden parametr - jeśli podana liczba jest liczbą bliźniaczą zwróć jej bliźniaka, jeśli nie jest bliźniacza to zwróć False.

# Obie funkcje mają przyjmować liczby naturalne. Podanie innej liczby niż naturalna w wymaganym parametrze ma skutkować zwróceniem None.

# Definicja 1: Liczba pierwsza to liczba naturalna większa od 1, która ma dokładnie dwa dzielniki naturalne: jedynkę i siebie samą.
# Definicja 2: Liczby bliźniacze to takie dwie liczby pierwsze, których różnica wynosi 2.

# Przydatne linki:
# https://stackoverflow.com/questions/18833759/python-prime-number-checker

def prime(n):
    if type(n) == int:
        if n < 2:
            return False
        elif n == 2:
            return True
        elif not n & 1:
            return False
        for x in range(3, int(n ** 0.5) + 1, 2):
            if n % x == 0:
                return False
        return True


def twins(n, *args):
    if args.__len__() == 0:
        if prime(n):
            if prime(n + 2):
                return n + 2
            elif prime(n - 2):
                return n - 2
            else:
                return False
        else:
            return False
    elif (type(n) == int) and (type(args[0]) == int) and abs(n - args[0]) == 2:
        return prime(n) and prime(args[0])


assert prime(101) == True
assert prime("22") is None

assert twins(101) == 103
assert twins(79) == False
assert twins(5, 7) == True

# zadanie 5

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

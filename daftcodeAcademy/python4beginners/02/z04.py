# Zadanie 4
# Napisz funkcję fibonacci_list, która dla zadanego n obliczy n liczb ciągu Fibonacciego, zwracając listę liczb z zadanego ciągu.

def fibonacci_list(n):
    if n == 0:
        return []
    elif n == 1:
        return [1]
    elif n == 2:
        return [1, 1]
    elif n > 2:
        result = [1, 1]
        counter = 2
        while n > counter:
            result.append(result[counter - 1] + result[counter - 2])
            counter += 1
        return result

assert fibonacci_list(7) == [1, 1, 2, 3, 5, 8, 13]

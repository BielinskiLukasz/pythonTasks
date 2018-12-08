# ZADANIE 3: czyszczenie id_number i liczenie unikalnych id_number po czyszczeniu
# Napisz funkcję count_unique_id_numbers_after_clean, która przyjmie nazwę pliku csv (str), a zwróci inta, którego
# wartością będzie liczba unikalnych id_number w przekazanym pliku csv. Ma być to wartość po czyszczeniu pliku csv.
# Do testów używamy pliku personal_data_homework.csv (tego samego, co w zadaniu 1).
#
# Uwagi:
# Funkcję czyszczącą trzeba napisać samemu i wywołać ją w count_unique_id_numbers_after_clean. Mogą przydać się
# materiały z wykładu.
# W przekazanym pliku nie będzie wartości id_number, której nie da się oczyścić (np. z brakującymi danymi).
# W przekazanym pliku nie będzie pustych id_number.
# (Podpowiedź: po oczyszczeniu wszystkich id_number funkcja validate_id_number z poprzedniego zadania powinna zwrócić
# True dla wszystkich tych oczyszczonych wartości. validate_id_number musi być oczywiście poprawnie napisana;)
#
# Przykład:
# Dla wyjściowych danych (ignoruję tu inne kolumny, w pliku będą wszystkie, co na zajęciach):
#
# 1. "KA/123456/2005"
# 2. "IT/111111/2001"
# 3. "IT/111111/2001"
# 4. "IT/111111/   2001"
#
# Unikalnych wartości, po czyszczeniu, id_number jest 2 (dwie):
# - "KA/123456/2005" (1.)
# - "IT/111111/2001" (2., 3., 4.)
# Jest tak, bo po czyszczeniu "IT/111111/   2001" staje się "IT/111111/2001", czyli tym samym, co pozycje 2. oraz 3.


def count_unique_id_numbers_after_clean(filename):
    personal_data = read_data(filename)
    id_numbers = set(personal_data['id_number'])
    unique_id_numbers = list()
    for id_number in id_numbers:
        if not validate_id_number(id_number):
            id_number = id_number.replace('.', '/').replace('_', '/').replace('-', '/')
            code, number, year = id_number.split('/')
            code = code.strip()
            code = code.upper()
            number = number.strip()
            year = year.strip()
            unique_id_numbers.append(code + '/' + number + '/' + year)
        else:
            unique_id_numbers.append(id_number)
    return len(set(unique_id_numbers))


def read_data(filename):
    rows = list()
    data = dict()
    with open(filename, "r") as f:
        headers = f.readline().strip('\n').split(",")
        for line in f:
            rows.append(line.strip('\n').split(","))
        for i in range(0, len(headers)):
            data[headers[i]] = list(filter(lambda g: len(g), [y[i] for y in rows]))
    return data


def validate_id_number(id_number):
    valid_code = {'ZA', 'IT', 'KS', 'KA', 'LO', 'SP', 'MA', 'CZ', 'OC'}
    data = id_number.split('/')
    if len(data) != 3:
        return False
    code, number, year = data
    return (len(code) == 2 and code in valid_code
            and len(number) == 6 and number.isdigit()
            and len(year) == 4 and 1900 <= int(year) <= 2018)


assert count_unique_id_numbers_after_clean('personal_data_homework.csv') == 1533

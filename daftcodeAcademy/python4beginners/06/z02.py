# ZADANIE 2: walidacja wartości id_number
# Napisz funkcję validate_id_number, która przyjmuje id_number (str) oraz zwraca wartość typu bool:
# True, jeśli id_number jest zgodny ze specyfikacją opisaną w zadaniu 1
# False, jeśli nie jest zgodny
#
# Uwagi:
# Funkcja ma sprawdzać wyłącznie poprawność przekazanej wartości, nie ma robić nic więcej (jak na przykład sprawdzanie
# unikalności).
# Funkcja ma być przygotowana, by poprawnie walidować wszystkie wartości id_number z pliku personal_data_homework.csv.
# Dodatkowo ma sobie radzić z wartościami zepsutymi na wiele innych sposobów, w tym takich, które nie nadają się
# do oczyszczenia (np. z brakującymi danymi).


def validate_id_number(id_number):
    valid_code = {'ZA', 'IT', 'KS', 'KA', 'LO', 'SP', 'MA', 'CZ', 'OC'}
    data = id_number.split('/')
    if len(data) != 3:
        return False
    code, number, year = data
    return (len(code) == 2 and code in valid_code
            and len(number) == 6 and number.isdigit()
            and len(year) == 4 and 1900 <= int(year) <= 2018)


assert validate_id_number("SP/987543/2000") is True
assert validate_id_number("ZA/434503/2005") is True
assert validate_id_number("ZA/434503/2005 ") is False
assert validate_id_number("ble ble") is False
assert validate_id_number("ZA/43450/2005") is False
assert validate_id_number("XX/987654/2011") is False
assert validate_id_number("IT/34343/1800") is False

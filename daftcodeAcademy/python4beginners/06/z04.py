# ZADANIE 4: wyznaczanie mediany monthly_salary pięciu najkosztowniejszych pracowników w danym dziale
# Napisz funkcję median_of_top_five, która przyjmuje:
# filename – nazwę pliku CSV, w którym mamy dane (struktura pliku będzie taka sama jak na zajęciach),
# department_name – dwuliterowy skrót nazwy działu firmy, pisany wielkimi literami.
#
# Funkcja ma zwracać wartość `Decimal` z medianą wynagrodzeń pięciu najlepiej zarabiających pracowników firmy
# w danym dziale.
#
# UPDATE: działu szukamy w kolumnie `department_name`, a nie wyciągamy go z `id_number`. Zatem jeśli brakuje wartości
# pod `department_name`, to ignorujemy ten wiersz.
#
# UPDATE 2: zadaniem tej funkcji nie jest radzenie sobie z duplikatami. Zatem nie usuwamy duplikatów. Jeśli wiersz
# powtórzony, to traktujemy je jako dwa różne wiersze.
#
# Uwagi:
# Dane walutowe w pliku (kolumna monthly_salary) są do oczyszczenia. Niestety będą miały dodatkowe “brudy” względem tych
# pokazanych na zajęciach. Brudy te trzeba zaleźć i usunąć. Będą również puste wartości, należy je zignorować (nie mają
# wartości zero!). W trakcie czyszczenia dane mają być zaokrąglane do dwóch miejsc po przecinku, tak jak na zajęciach.

import csv
from decimal import Decimal
from statistics import median


def median_of_top_five(filename, department):
    people = get_csv_lines(filename)
    salary = list(
        Decimal(person['monthly_salary'].strip().upper().replace('ZŁOTYCH', '').replace('ZŁ', '').replace('PLN', '')
                .replace(',', '.').replace(' ', '')).quantize(Decimal('0.01'))
        for person in people
        if person['department'][:2] == department
    )
    salary.sort(reverse=True)
    return median(salary[:5]).quantize(Decimal('0.01'))


def get_csv_lines(in_filename):
    with open(in_filename, encoding='utf8') as csv_file:
        reader = csv.DictReader(csv_file, delimiter=',')
        for row in reader:
            yield row


assert median_of_top_five('personal_data_homework.csv', 'IT') == Decimal("9160.25")
assert median_of_top_five('personal_data_homework.csv', 'ZA') == Decimal("90640.00")
assert median_of_top_five('personal_data_homework.csv', 'LO') == Decimal("5104.84")

# Pamiętasz firmę ConfWord dla której sprawdzałeś statystyki kilka tygodni temu?
# Okazało się że firmowa baza danych klientów wyciekła do internetu.

# By firma ConfWorld dalej funkcjonowała musisz przekazać klientom
# informacje na temat wycieku, ale nie chcesz siać paniki.
# W pierwszej kolejności należy zresetować hasła klientom którzy nie zmieniali hasła od czasu ataku

# Napisz program by znaleźć takie osoby. Wyciek danych nastąpił 10.11.2017 w samo południe
# Twoja baza danych jest aktualna (załóżmy dzień 20.11.2018 00:00)

# Na domiar złego okazało się że Twoi klienci używali bardzo słabych haseł.
# By w przyszłości nikt nie łamał haseł Twoich klientów,
# wykożystując listę dancyh najczęściej używanych haseł w internecie,
# napisz kolejną część programu który w 2-giej kolejności:
#     znajdzie wszystkich użytkowników którzy mają hasło figurujące na tej liście
#     znajdzie top 10 występujących haseł w serwisie figurujących na liście top500 w PLAIN TEXT
#     znajdzie wszystkich bezpiecznych użytkowników
#         (hasło nie na figuruje liście oraz zmienili hasło od ataku)

# Dane:
#     hasła w bazie są hashowane algorytmem SHA1
#     lista 500 najczęstszych haseł w internecie -> top_500_most_common_passwords.txt
#     baza danych która wyciekła do internetu   -> confwrld_user_data_dump_10.11.2017.csv
#     aktualna baza klientów                    -> confwrld_user_database.csv
#     wszystkie daty są z tej samej strefy czasowej

# Wymagania szczegółowe:
#     ConfData
#         Struktura przechwująca dane
#     ConfData.weak_pass_users(pass_list)
#         Zwraca listę ludzi którzy mają słabe hasło figurujące na liście słaych haseł
#         pass_list = [["pass1", "pass1_hash"], ["pass1", "pass1_hash"], ...]
#     ConfData.common_pass(pass_list, n=10) = ["pass1", "pass2", ..... ]
#         Zwraca listę ludzi którzy mają najczęściej występujące hasła
#         pass_list = [["pass1", "pass1_hash"], ["pass1", "pass1_hash"], ...]
#     ConfData.pwned_users(pass_list, hack_time) = ["mail1", "mail2", ..... ]
#         Zwraca listę ludzi których musimy poinformować o wycieku ich hasła
#         hack_time -> objekt Datetime reprezentujący czas wycieku
#     ConfData.safe_users(pass_list, hack_time) = ["mail1", "mail2", ..... ]
#         Zwraca listę ludzi którzy nie figurowali w wycieku i mają bezpieczne hasła
#         hack_time -> objekt Datetime reprezentujący czas wycieku

# Do dyzpozycji jest tylko próbka danych które firma ConfWord przekazała do analizy
# Napisz program tak by działał dla dowolych danych i czasu wycieku

import hashlib
from collections import Counter
from datetime import datetime


class ConfData:
  def __init__(self, filename="confwrld_user_database.csv"):
    self.filename = filename
    self.confData = self.read_data(filename)

  @staticmethod
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

  @staticmethod
  def read_passwords(database_file="top_500_most_common_passwords.txt"):
    data = list()
    with open(database_file, "r") as f:
      for line in f:
        password = line.strip('\n')
        pass_hash = hashlib.sha1(password.encode('utf-8')).hexdigest()
        data.append([password, pass_hash])
    return data

  def weak_pass_users(self, input_list):
    pass_hash = list()
    weak_pass_users = list()
    for pass_and_hash in input_list:
      pass_hash.append(pass_and_hash[1])
    for i in range(0, len(self.confData["email"])):
      if self.confData["pass_hash"][i] in pass_hash:
        weak_pass_users.append(self.confData["email"][i])
    return weak_pass_users

  def common_pass_users(self, input_list, n=10):
    pass_counter = Counter(self.confData["pass_hash"])
    common_pass_hash = list(sorted(pass_counter.items(), key=lambda kv: kv[1], reverse=True))
    common_pass = [x[0] for x in common_pass_hash]
    common_top_pass = list()
    for i in range(0, len(common_pass)):
      for top_pass in input_list:
        if common_pass[i] == top_pass[1]:
          common_top_pass.append(top_pass[0])
    return common_top_pass[:n]

  def pwned_users(self, input_list, hack_time):
    pwned_users_list = list()
    date_format = "%Y-%m-%dT%H:%M:%S"
    pass_hash = list()
    for pass_and_hash in input_list:
      pass_hash.append(pass_and_hash[1])
    for i in range(0, len(self.confData["email"])):
      date = datetime.strptime(self.confData["date_updated"][i], date_format)
      if date < hack_time and self.confData["pass_hash"][i] in pass_hash:
        pwned_users_list.append(self.confData["email"][i])
    return pwned_users_list

  def safe_users(self, input_list, hack_time):
    unsafe_users = self.pwned_users(input_list, hack_time)
    return [email for email in self.confData["email"] if email not in unsafe_users]


# TESTS
cd = ConfData()
pass_list = ConfData.read_passwords()
print("Complete")

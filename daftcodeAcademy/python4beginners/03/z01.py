# W tym zadaniu zawsze będą poprawne dane.
# Nie ma potrzeby obsługiwania sytuacji wyjątkowych.

# Napisz klasę MyFraction.
# Ta klasa ma reprezentować ułamek.
# Ta klasa ma być mutowalna.#
# Ta klasa ma mieć dwa pola: `numerator` i `denominator`.

# Instancję klasy powinno dać się utworzyć na następujące sposoby:
# 	MyFraction(1, 2)
# 	MyFraction(1, denominator=2)
# 	MyFraction(numerator=1, denominator=2)
# 	MyFraction(5) == MyFraction(5, 1)
# 	MyFraction(numerator=6) == MyFraction(numerator=6, denominator=1)
# 	MyFraction(MyFraction(1, 2)) == MyFraction(1, 2)

# Dodatkowo mianownik ułamka powinien zawsze być najmniejszą możliwą liczbą.
# Przykład:
# 	a = MyFraction(10, 30)
# 	assert 1 == a.numerator
# 	assert 3 == a.denominator

# Ułamki powinno dać się do siebie dodać.
# 	MyFraction(5, 4) == MyFraction(2, 4) + MyFraction(3, 4)
# Ułamki powinno dać się do siebie porównać.
#         MyFraction(6, 3) == MyFraction(6, 3)
# Dodawanie int też powinno być możliwe.
# 	MyFraction(5, 4) == MyFraction(1, 4) + 1
# 	MyFraction(5, 4) == 1 + MyFraction(1, 4)

# Instancje klasy MyFraction powinno dać się rzutować na string
# Przykład:
# 	'MyFraction(numerator=1, denominator=2)' == str(MyFraction(1, 2))
# 	'MyFraction(numerator=1, denominator=2)' == repr(MyFraction(1, 2))


class MyFraction:
  def __init__(self, numerator, denominator=1):
    if type(numerator) is MyFraction:
      self.numerator = numerator.numerator
      self.denominator = numerator.denominator
    else:
      self.numerator, self.denominator = self.reduction(numerator, denominator)

  def __add__(self, other):
    other = MyFraction(other)
    return MyFraction(self.calculate_numerator(self, other), self.calculate_denominator(self, other))

  def __radd__(self, other):
    return self.__add__(other)

  def __iadd__(self, other):
    self.numerator, self.denominator = self.reduction(self.calculate_numerator(self, other),
                                                      self.calculate_denominator(self, other))
    return self

  def __eq__(self, other):
    other = MyFraction(other)
    return self.numerator == other.numerator and self.denominator == other.denominator

  def __repr__(self):
    return 'MyFraction(numerator={}, denominator={})'.format(self.numerator, self.denominator)

  def __str__(self):
    return self.__repr__()

  @staticmethod
  def reduction(num1, num2):
    temp1 = num1
    temp2 = num2
    while temp1 != temp2:
      if temp1 > temp2:
        temp1 -= temp2
      else:
        temp2 -= temp1
    divider = temp1
    return int(num1 / divider), int(num2 / divider)

  @staticmethod
  def calculate_numerator(fraction1, fraction2):
    return fraction1.numerator * fraction2.denominator + fraction2.numerator * fraction1.denominator

  @staticmethod
  def calculate_denominator(fraction1, fraction2):
    return fraction1.denominator * fraction2.denominator

# Dla modelowej lub swojej klasy MyFraction dodaj walidację wejścia i przetwarzania.
# Tym razem oczekujemy że MyFraction będzie obsługiwać nie tylko dodawanie ale również:
#     odejmowanie
#     mnożenie
#     dzielenie

# MyFraction ma nie działać z "podwójnymi" operatorami np ** // i rzucać odpowiednim wyjątkiem
# Jak i przekazywanie ułamków jako licznik czy mianownik.
# Przykład:
#     MyFraction(1, 2) * MyFraction(1, 2) == MyFraction(1, 4)
#     MyFraction(numerator=1, denominator=MyFraction(1,2)) == MyFraction(2, 1)
#     MyFraction(2, 3) / MyFraction(1, 3) == MyFraction(2, 1)


# Klasa MyFraction powinna też móc się dodawać, odejmować, mnożyć i dzielić
#     z liczbami zmiennoprzecinkowymi ale:
#     nie musi ich przyjmować jako argumenty
#     wynik operacji z operandem typu float jest typu float
#     MyFraction można przedstawić w notacji zmiennoprzecinkowej
# Przykład:
#     0.5 + MyFraction(1, 2) == 1.0
#     float(MyFraction(3, 20)) == 0.15

# Dodatkowo wejście może nie być poprawne.
# Z tego powodu klasa MyFraction powinna walidować wejściowe parametry i ich poprawność.

# By to osiągnąć zaimplementuj następujące wyjątki dziedziczące po wbudowanych wyjątkach:
#     InvalidOperandError
#     InvalidInputOperandError
#     OperationNotSupportedError

# Przykład:
#     MyFraction(5, 4) + "10"   #  <- ten test ma rzucić wyjątkiem InvalidOperand
#     MyFraction(5, [12])       #  <- ten test ma rzucić wyjątkiem InvalidInputOperand
#     MyFraction(99, 100)**2    #  <- ten test ma rzucić wyjątkiem OperationNotSupported

# Klasa MyFraction nie musi obsługiwać liczb ujemnych - w testach nigdy nie dojdzie do sytuacji gdzie wynik operacji matematycznej jest ujemny.

# Pamiętaj jednak że wszystkie dotychczasowej operacje na MyFraction z Zadania 3.1 powinny
# wciąż działać.

# UWAGA: Testy porównujące ze sobą floaty są wykonywane z domyślną dokładnością funkcji assertAlmostEqual z frameworku unittest tj z dokładnością do 7mego miejsca po przecinku

import math

class MyFraction():
  def __init__(self, numerator, denominator = 1):
    if isinstance(denominator, int) and denominator == 0:
      raise InvalidInputOperandError()
    elif isinstance(numerator, MyFraction) and isinstance(denominator, int):
      self.numerator = numerator.numerator
      self.denominator = numerator.denominator
    elif isinstance(denominator, MyFraction) and isinstance(numerator, int):
      self.numerator = numerator * denominator.denominator
      self.denominator = denominator.numerator
    elif isinstance(numerator, int) and isinstance(denominator, int):
      self.numerator = numerator
      self.denominator = denominator
    else:
      raise InvalidInputOperandError()
    self._reduce()

  def _reduce(self):
    nd_gcd = math.gcd(self.numerator, self.denominator)
    self.numerator //= nd_gcd
    self.denominator //= nd_gcd
    
  def __add__(self, other):
    if isinstance(other, float):
      return self.__float__() + other
    elif type(other) == int:
      other = MyFraction(other)
    if isinstance(other, MyFraction):
      return MyFraction(self._add_numerators(self, other), self._mul_divisors(self, other))
    else:
      raise InvalidOperandError()
    
  def __radd__(self, other):
    return self.__add__(other)
    
  def __iadd__(self, other):
    if isinstance(other, float):
      return self.__float__() + other
    elif type(other) == int:
      other = MyFraction(other)
    if isinstance(other, MyFraction):
      self.numerator = self._add_numerators(self, other)
      self.denominator = self._mul_divisors(self, other)
      self._reduce()
      return self
    else:
      raise InvalidOperandError()

  def __sub__(self, other):
    if isinstance(other, float):
      return self.__float__() - other
    elif type(other) == int:
      other = MyFraction(other)
    if isinstance(other, MyFraction):
      return MyFraction(self._sub_numerators(self, other), self._mul_divisors(self, other))
    else:
      raise InvalidOperandError()

  def __rsub__(self, other):
    if isinstance(other, float):
      return other - self.__float__()
    elif type(other) == int:
      other = MyFraction(other)
    if isinstance(other, MyFraction):
      return MyFraction(self._sub_numerators(other, self), self._mul_divisors(self, other))
    else:
      raise InvalidOperandError()

  def __isub__(self, other):
    if isinstance(other, float):
      return self.__float__() - other
    elif type(other) == int:
      other = MyFraction(other)
    if isinstance(other, MyFraction):
      self.numerator = self._sub_numerators(self, other)
      self.denominator = self._mul_divisors(self, other)
      self._reduce()
      return self
    else:
      raise InvalidOperandError()

  def __mul__(self, other):
    if isinstance(other, float):
      return self.__float__() * other
    elif type(other) == int:
      other = MyFraction(other)
    if isinstance(other, MyFraction):
      return MyFraction(self._mul_numerators(self, other), self._mul_divisors(self, other))
    else:
      raise InvalidOperandError()

  def __rmul__(self, other):
    return self.__mul__(other)

  def __imul__(self, other):
    if isinstance(other, float):
      return self.__float__() * other
    elif type(other) == int:
      other = MyFraction(other)
    if isinstance(other, MyFraction):
      self.numerator = self._mul_numerators(self, other)
      self.denominator = self._mul_divisors(self, other)
      self._reduce()
      return self
    else:
      raise InvalidOperandError()

  def __truediv__(self, other):
    if isinstance(other, float):
      return self.__float__() / other
    elif type(other) == int:
      other = MyFraction(other)
    if isinstance(other, MyFraction):
      reciprocal = MyFraction(other.denominator, other.numerator)
      return self.__mul__(reciprocal)
    else:
      raise InvalidOperandError()

  def __rtruediv__(self, other):
    reciprocal = MyFraction(self.denominator, self.numerator)
    return reciprocal.__mul__(other)

  def __itruediv__(self, other):
    if isinstance(other, float):
      return self.__float__() / other
    elif type(other) == int:
      other = MyFraction(other)
    if isinstance(other, MyFraction):
      reciprocal = MyFraction(other.denominator, other.numerator)
      self.numerator = self._mul_numerators(self, reciprocal)
      self.denominator = self._mul_divisors(self, reciprocal)
      self._reduce()
      return self
    else:
      raise InvalidOperandError()
		
  def _add_numerators(self, fraction1, fraction2):
    return fraction1.numerator * fraction2.denominator + fraction2.numerator * fraction1.denominator
    
  def _sub_numerators(self, fraction1, fraction2):
    return fraction1.numerator * fraction2.denominator - fraction2.numerator * fraction1.denominator
    
  def _mul_divisors(self, fraction1, fraction2):
    return fraction1.denominator * fraction2.denominator

  def _mul_numerators(self, fraction1, fraction2):
    return fraction1.numerator * fraction2.numerator

  def __eq__(self, other):
    other = MyFraction(other)
    return (
      self.numerator == other.numerator and 
      self.denominator == other.denominator
    )
    
  def __float__(self):
    return self.numerator / self.denominator
    
  def __floordiv__(self, other):
    raise OperationNotSupportedError()
    
  def __ifloordiv__(self, other):
    raise OperationNotSupportedError()
    
  def __pow__(self, other):
    raise OperationNotSupportedError()
    
  def __ipow__(self, other):
    raise OperationNotSupportedError()
    
  def __lshift__(self, other):
    raise OperationNotSupportedError()
    
  def __ilshift__(self, other):
    raise OperationNotSupportedError()
    
  def __rshift__(self, other):
    raise OperationNotSupportedError()
    
  def __irshift__(self, other):
    raise OperationNotSupportedError()
    
  def __repr__(self):
    return '{}(numerator={}, denominator={})'.format(self.__class__.__name__, self.numerator, self.denominator)
    
  def __str__(self):
    return self.__repr__()

class InvalidOperandError (Exception):
  pass

class InvalidInputOperandError (Exception):
  pass

class OperationNotSupportedError (Exception):
  pass

# TESTS
assert(MyFraction(1, 2) * MyFraction(1, 2) == MyFraction(1, 4))
assert(MyFraction(numerator=1, denominator=MyFraction(1,2)) == MyFraction(2, 1))
assert(MyFraction(2, 3) / MyFraction(1, 3) == MyFraction(2, 1))
assert(float(MyFraction(3, 20)) == 0.15)
assert(0.5 + MyFraction(1, 2) == 1.0)

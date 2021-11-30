from numpy import abs, cos, exp, mean, pi, prod, sin, sqrt, sum
import numpy as np
class TestFunc():               # Test fonksiyonlarının tutulduğu sınıf

    # Problem default parametreleri
    costfunc = None             # Setup.py dosyasında belirlenen maliyet fonk.
    nvar = 30                   # Problem boyutu
    varmin = -5.0               # Problem minimum default sınır
    varmax = 5.0                # Problem minimum default sınır

    # Sphere test fonksiyonu
    def Sphere(self):
        self.costfunc = lambda x: sum(x ** 2)
        self.varmin = -5.12
        self.varmax = 5.12
        return self

    # Rosenbrock test fonksiyonu
    def Rosenbrock(self):
        self.costfunc = lambda x: sum((1 - x[:-1]) ** 2) + 100 * sum((x[1:] - x[:-1] ** 2) ** 2)
        self.varmin = -2.048
        self.varmax = 2.048
        return self

    # Zakharov test fonksiyonu
    def Zakharow(self):
        self.costfunc = self.__ZakharowF
        self.varmin = -5
        self.varmax = 10
        return self

    # Schwefel test fonksiyonu
    def Schwefel(self):
        self.costfunc = lambda x: 418.9829 * len(x) - sum(x * sin(sqrt(abs(x))))
        self.varmin = -500.0
        self.varmax = 500.0
        return self

    # Rastrigin test fonksiyonu
    def Rastrigin(self):
        self.costfunc = lambda x: 10 * len(x) + sum(x**2 - 10 * cos(2 * pi * x))
        self.varmin = -5.12
        self.varmax = 5.12
        return self

    # Ackley test fonksiyonu
    def Ackley(self):
        self.costfunc = self.__ackleyF
        self.varmin = -5.12
        self.varmax = 5.12
        return self

    def __ZakharowF(self, x):
        n = len(x)
        j = np.arange(1., n + 1)
        s2 = sum(j * x) / 2
        return sum(x ** 2) + s2 ** 2 + s2 ** 4

    def __ackleyF(self, x):
        a = 20
        b = 0.2
        c = 2 * pi
        n = len(x)
        s1 = sum(x ** 2)
        s2 = sum(cos(c * x))
        return -a * exp(-b * sqrt(s1 / n)) - exp(s2 / n) + a + exp(1)
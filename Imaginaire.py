class Imaginaire:

    def __init__(self, ent, ima):
        self.e = ent
        self.i = ima
        self.value = (ent, ima)

    def __str__(self):
        return str(self.e) + ' + ' + str(self.i) + 'i'

    def __add__(self, y):
        return Imaginaire(self.e + y.e, self.i + y.i)

    def __sub__(self, y):
        return Imaginaire(self.e - y.e, self.i - y.i)

    def __mul__(self, y):
        return Imaginaire(self.e * y.e - self.i * y.i, self.e * y.i + y.e * self.i)

    def __truediv__(self, y):
        return Imaginaire((self.e * y.e + self.i * y.i) / (y.e ** 2 + y.i ** 2), (self.e * y.i + y.e * self.i) / (y.e ** 2 + y.i ** 2))

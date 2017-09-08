class Rationel:
    ''' x ∈ Q '''

    def __init__(self, value):
        self.value = value

    def __str__(self):
        return str(self.value)

    def __add__(self, y):
        return Rationel(self.value + y.value)

    def __sub__(self, y):
        return Rationel(self.value - y.value)

    def __mul__(self, y):
        return Rationel(self.value * y.value)

    def __mod__(self, y):
        return Rationel(self.value % y.value)

    def __truediv__(self, y):
        return Rationel(self.value / y.value)

    def __floordiv__(self, y):
        return Rationel(self.value // y.value)

    def __pow__(self, y):
        return Rationel(self.value ** y.value)

    def __and__(self, y):
        return Rationel(self.value & y.value)

    def __or__(self, y):
        return Rationel(self.value | y.value)

    def __xor__(self, y):
        return Rationel(self.value ^ y.value)


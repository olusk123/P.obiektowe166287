import math
class polynomial:
    def __init__(self, coefficients):
        self.coefficients = list(coefficients)

    def deg(self):
        z = len(self.coefficients) - 1
        y = self.coefficients[::-1]
        for x in range(len(y)):
            if y[x] == 0:
                z -= 1
            else:
                return z
            return z

    def __str__(self):
        return str(self.coefficients)

    def __neg__(self):
        return self.coefficients[::-1]

    def __add__(self, other_poly):
        for x in range(len(self.coefficients)):
            for x in other_poly:
                self.coefficients[x] = self.coefficients[x] + other_poly.coefficients[x]
                return self.coefficients

    def __sub__(self, other_poly):
        for x in range(len(self.coefficients)):
            for x in other_poly:
                self.coefficients[x] = self.coefficients[x] - other_poly.coefficients[x]
                return self.coefficients


    def __eq__(self, other_poly):
        for x in range(len(self.coefficients)):
            for x in other_poly:
                self.coefficients[x] = self.coefficients[x] != other_poly.coefficients[x]
                return False
            else:
                return True

    def __call__(self,x):
        return self.coefficients[x]

P = polynomial([5, 4, 3, 0, 1])
print(P.deg())
print(P)
print(P.__neg__())



class Vector(object):
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        return Vector(self.x + other.x, self.y + other.y)

    def __sub__(self, other):
        return Vector(self.x - other.x, self.y - other.y)

    def __mul__(self, other):
        return self.x*other.x + self.y*other.y

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    def __str__(self):
        return '(%g, %g)' % (self.x, self.y)

    def __repr__(self):
        return repr((self.x, self.y))







#zad1

def nwd(a: int,b: int ) -> int:
    if b == 0:
        return a
    return nwd(b,a % b)

class wymierna(object):
    def __init__(self,p: int=0, q: int=1):
        if type(p)!= int:
            p = int(p)
        if type(q)!= int:
            q = int(q)

        nwdWar = nwd(q,p)

        if nwdWar!= 1:
            q = int(q/nwdWar)
            p = int(p/nwdWar)

        if q < 0:
            p = -p
            q = -q
        self.p = p
        self.q = q
    @staticmethod
    def wzglednie_pierwsze(p,q):
        while p:
            p,q =q, p% q
        return abs(p) == 1

    def get_licznik(self):
        return self.p

    def get_mianownik(self):
        if self.q > 0:
            return self.q
        else:
            return False

    def __repr__(self):
        return f'{self.p}/{self.q}'

    def __float__(self):
        return float(self.p/self.q)

    def __add__(self, other):
        ilo = self.q * other.q
        if ilo < 0:
            ilo = -ilo

        self.p *= int(ilo / self.q)
        other.p *= int(ilo / other.q)

        return wymierna(self.p + other.p, ilo)


    def __sub__(self, other):
        return self + wymierna(-other.p,other.q)

    def __eq__(self, other):
        return self.p==other.p and self.q == other.q

    def __ne__(self, other):
        return self.p != other.p and self.q != other.q

    def __gt__(self,other):
       if self.p < 0 < other.p:
            return True
       if self.p > 0 > other.p:
           return False
       x = (self.p/other.p) / (self.q/other.q)
       if self.p > 0 and self.q >0:
           return x <1
       return x >1


    def __ge__(self, other):
        if self.p == other.p and self.q == other.q:
            return True

        return self > other

    def __le__(self,other):
        return not self > other

    def __lt__(self,other):
        return not self >= other

    def __mul__(self,other):
        return wymierna(self.p * other.p,self.q * other.q)

    def __truediv__(self, other):
        return wymierna(self.p * other.q,self.q * other.p)

    def nierowne(self,other):
        return  not (self > other or self < other)

l1 = wymierna(8/16)
l2 = wymierna(2/8)
print(l1.get_licznik())
print(l1.get_mianownik())
print((str(l1)))
print((float(l1)))
print(l1 + l2)
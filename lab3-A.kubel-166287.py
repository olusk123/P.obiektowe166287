import math
#zadanie1
class punkt(object):
    def __init__(self,a,b):
        self.a = a
        self.b = b
    @staticmethod
    def distance(P1,P2):
        dl = ((P1.a - P2.a) ** 2 + (P1.b - P2.b) ** 2)**(1/2)
        return dl

P1 = punkt(1,3)
NazwanyPunkt = punkt(3,7)
print((punkt.distance(P1,NazwanyPunkt)))
#zadanie2

class Adres(object):
    def __init__(self,NrDomu,Ulica,Miasto,KodP,NrM=None):
        self.NrDomu = NrDomu
        self.Ulica = Ulica
        self.Miasto = Miasto
        self.KodP = KodP

        if NrM is not None:
            self.NrM = NrM
    def show(self) -> None:
        if hasattr(self,'NrM'):
            print(f'{self.Ulica} {self.NrDomu}/{self.NrM}')
            print(f'{self.KodP} {self.Miasto}')
            return None
    def comes_before(self,other):
        for i in range(len(self.KodP)):
            if(self.kodP[i] == other.KodP[i]):
                continue
            if(self.KodP[i] < other.KodP[i]):
                return True
            return False
adres1 = Adres("wawrzyczka","5","14-300","Olsztyn","43")
adres1.show()
#zadanie3

class SodaCan(object):
    def __init__(self,h,r):
        self.h = h
        self.r = r


    def get_volume(self) -> float:
        return math.pi * self.r * self.r * self.h


    def get_surface_area(self) -> float:
        return ((2*math.pi*self.r)*self.h) + ((math.pi*self.r**2)**2)

class Car(object):
    def __init__(self , wydajnosc : float , paliwo : float):
        self.wydajnosc = wydajnosc
        self.paliwo = paliwo
        self.akt_paliwo = 0

    def drive(self,dystans) -> None:
        z_paliwa = dystans/self.wydajnosc
        if z_paliwa > self.akt_paliwo:
            print("nie masz tyle paliwa")
            return None
        self.akt_paliwo -= dystans/self.wydajnosc


    def get_fuel_level(self) -> float:
        return self.akt_paliwo


    def add_fuel(self,dod_paliwo: float) -> None:
        if dod_paliwo + self.akt_paliwo > self.paliwo:
            print("za duzo")
            return None
        self.akt_paliwo += dod_paliwo


my_car = Car(20, 40) # Wydajno ́s ́c 20 km/litr, pojemno ́s ́c baku 40
my_car.add_fuel(30) # Zatankuj co najwy ̇zej 30 litrów
my_car.drive(100) # Przejed ́z 100 m
print(my_car.get_fuel_level()) # Wydrukuj ilo ́s ́c pozostałego

class Student(object):
    def __init__(self,imie,nazwisko,**args):
        self.imie = imie
        self.nazwisko = nazwisko
        self.l_quizow = len(args)

    def get_name(self):
        self.imie = input("Wprowadz imie")
        self.nazwisko = input("Wprowadz nazwisko")

    def add_quiz(self, score):
        self.srednia_quizuw = ((self.srednia_quizuw * self.liczba_quizuw) + score) / (self.liczba_quizuw + 1)
        self.liczba_quizuw += 1

    def get_total_score(self):
        return self.srednia_quizuw * self.liczba_quizuw

    def get_average_score(self):
        return self.srednia_quizuw
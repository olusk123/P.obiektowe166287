import array
#zad1
print(dir(array))
#zad2

class wyswietl():
    def wys(self):
        return

print(dir(wyswietl()))

#zad3

class zadnie3():
    def __init__(self):
        self.name = 'ala ma kota'

x = zadnie3()
print(dir(x))

#zad4

print(dir(abs(1)))
y = -155
print(abs(y))

class student(object):
    def __init__(self,nazwa_ucznia:str, klasa_ucznia: str, student_id: int):
        self.nazwa_ucznia = nazwa_ucznia
        self.klasa_ucznia = klasa_ucznia
        self.student_id = student_id

student = student("olek","3c",12)
print(student.nazwa_ucznia)
print(student.klasa_ucznia)
print(student.student_id)


#zad7
class student(object):
    def __init__(self):
        self.a = "zad7"

a = type(student)
b = type(a.__dict__)
c = type(a.__module__)
print(a)
print(b)
print(c)

#zad8
class Student1(object):
    pass
class Marks(object):
    pass

instancja1= Student1()
instancja2= Student1()
instancja3= Marks()

print(isinstance(instancja1,Student1))
print(isinstance(instancja2,Marks))
print(isinstance(instancja3,Student1))

print(issubclass(Student1,object))
print(issubclass(Marks,object))


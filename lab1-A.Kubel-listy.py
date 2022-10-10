# zad 1
A = [1+x for x in range(0, 10)]
print(A)
B = [2*x for x in range(0, 11)]
print(B)
C = [x**2 for x in range(1,11)]
print(C)
D = [x*0 for x in range(1,10)]
print(D)
E = [x%2 for x in range(0,10)]
print(E)
f = [x%5 for x in range(0,10)]
print(f)
# zad 2
listaA = []
A = 1
while A in range (0,11):
     listaA.append(A)
     A+=1
print(listaA)

listaB = []
B = 0
while B in range (0,21):
     listaB.append(B)
     B+=2
print(listaB)
listaC = []
C = 1
while C in range (0,11):
     listaC.append(C**2)
     C+=1
print(listaC)

listaD = []
C = 1
while C in range (0,11):
     listaD.append(C*0)
     C+=1
print(listaD)

listaE = []
C = 0
while C in range (0,10):
     listaE.append(C%2)
     C+=1
print(listaE)

ListaF= []
F=0
while F in range(0,10):
     ListaF.append(F%5)
     F+=1
print(ListaF)

#zad 3
def ile_ujemnych(lista):
     licznik = 0
     for x in lista:
         if(x<0):
             licznik+=1
     print(licznik)
lista1 = [-1, -2, -8, -1, -5, 6, 7, -3]
ile_ujemnych((lista1))
#zad 4
def iloczyn(lista):
     wynik = 1
     for x in lista:
          wynik = wynik * x
     print(wynik)
list = [2,12,1,5,1]
iloczyn(list)
#zad 5
def minmax(lista):
     return (min(lista), max(lista))
lista =[31, 28, 31, 30, 31, 30, 31, 31,30, 31, 30, 31]
print(minmax(lista))
#zad 6
def suma(lista):
     wynik = 1
     suma = 0
     for x in lista:
          suma += wynik*x
          wynik = -wynik
     print(suma)
listaa = [1, 4, 16, 9, 9, 7, 4, 9, 11]
suma(listaa)
# zad 7
i = 0
listaBAA = []
while i < 10:
     x = input()
     while x in listaBAA:
          print("juz jest na liscie")
          x = input()
     listaBAA.append(x)
     i += 1
print(listaBAA)
# zad8
lista = []
for x in range(2, 10001):
    lista.append(x)

for x in lista:
    if (x % 2 == 0 and x != 2):
        lista.remove(x)

for x in lista:
    if (x % 3 == 0 and x != 3):
        lista.remove(x)

print(lista)
# zad9
# a

def foo(list):
    list[0], list[len(list) - 1] = list[len(list) - 1], list[0]


lista = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
foo(lista)
print(lista)
# b

lista = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]


def foo1(list):
    temp = list[-1]
    list.pop(-1)
    list.insert(0, temp)


foo1(lista)
print(lista)


# c
def foo2(list):
    for x in list:
        if x % 2 == 0:
            list[x] = 0


lista = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
foo2(lista)
print(lista)


# d

def foo3(list):
    a = list.copy()
    for i in range(1, len(list) - 1):
        if a[i - 1] > a[i + 1]:
            list[i] = a[i - 1]
        else:
            list[i] = a[i + 1]


lista = [0, 4, 2, 3, 5, 9]
foo3(lista)
print(lista)


# e

def foo4(list):
    if len(list) % 2 == 1:
        del list[len(list) // 2]
    else:
        del list[int(len(list) / 2)]
        del list[len(list) // 2]


lista = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
foo4(lista)
print(lista)


# f

def foo5(list):
    j = 0
    for i in range(len(list)):
        if list[i] % 2 == 0:
            temp = list[i]
            list.pop(i)
            lista.insert(j, temp)
            j += 1


lista = [0, 2, 2, 3, 4, 5, 6, 7, 8, 9, 10]
foo5(lista)
print(lista)


# g

def foo6(list):
    list.sort()
    return list[-2]


lista = [0, 1, 5, 4, 2, 3, 8, 7, 9, 6]
print(foo6(lista))


# h
def foo7(list):
    for i in range(1, len(list) - 1):
        if list[i] < list[i - 1] or list[i] > list[i + 1]:
            return False
    return True


lista = [0, 1, 2, 3, 4, 5, 6, 7, 8, 8]
print(foo7(lista))


# i
def foo8(list):
    for i in range(len(list) - 1):
        if list[i] == list[i + 1]:
            return True
    return False


lista = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
print(foo8(lista))


# j
def foo9(list):
    for i in range(len(list)):
        for j in range(i + 1, len(list)):
            if list[i] == list[j]:
                return True
    return False


lista = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
print(foo9(lista))
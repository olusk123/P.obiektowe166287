#zad2.1
def mult(a):
    wynik = 1
    for x in range(0,len(a)):
        wynik*=a[x]
    return wynik

print(mult([3, 5, 7]))
#zad2.2
def mult_ints(*a):
    wynik = 1
    for x in range(0, len(a)):
        if type(a[x]) == int:
            wynik *= a[x]
    return wynik
print(mult_ints(3, 3.14, 5, "abc", 7))
#zad2.3
def multiply(*a):
    wynik = 1
    for x in a:
            wynik *= x
    return wynik
print(multiply(3, 5, 7))

#zad2.4
def multiply_ints(*a):
    wynik = 1
    for x in a:
        if type(x) == int:
            wynik *= x
    return wynik
print(multiply_ints(3, 5, 7))

#zad2.5
def make_car(firma,model,**a):
    slownik= a
    slownik["firma"]=firma
    slownik["model"]=model
    return slownik
print(make_car("Kia","Picanto", kolor = "cafemocca", poj_silnika = 900))

#zad3.1.1
def zad3_1_1():
    lista = []
    lista.append(x for x in range(1,11))
    lista.append(x**2 for x in range(1,11))
    lista.append(x**3 for x in range(1,11))
    for x in lista:
        for y in x:
            print(y)
print(zad3_1_1())

#zad3.1.2
def zad3_1_2():
    lista =[]
    aktualnaLiczba=1
    dlugoscListy=1
    for i in range(0,10):
        lista.append([])
        for j in range(dlugoscListy):
            lista[i].append(aktualnaLiczba)
            aktualnaLiczba+=1
        dlugoscListy+=1
    suma=0
    iterator=0
    for i in lista:
        arraySum=0
        for j in i:
            arraySum+=j
        suma += arraySum
        print(f'Array[{iterator}] suma== {arraySum}')
        iterator +=1
    print(f'suma wszystkiego == {suma}')
print(zad3_1_2())

#zad3.2.1
a = [[1, 2, 3, 4], [8, 9, 10, 12]]
b = [[1, 2, 3, 4], [8, 9, 10, 12]]
def dodawanie(a,b):
    n = 3
    c = [[0]*n for i in range(n)]
    for i in range(n):
        for j in range(n):
            c[i][j] = a[i][j] + b[i][j]
    return c
print(dodawanie([[3,2,1],[-1,2,3],[1,2,3]],[[3,2,1],[-1,2,3],[1,2,3]]))
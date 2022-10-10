# zad1a
def foo(a):
    dict = {}
    for x in a:
        if x not in dict.keys():
            dict.update({x: 1})
        else:
            dict[x] += 1
    return dict

# zad1b
def foo1(a):
    dict = {}
    for x in a:
        if x.isalpha():
            if x not in dict.keys():
                dict.update({x: 1})
            else:
                dict[x] += 1
    return dict

# zad1c
def foo2(c):
    a = c.lower()
    dict = {}
    for x in a:
        if x.isalpha():
            if x not in dict.keys():
                dict.update({x: 1})
            else:
                dict[x] += 1
    return dict

# zad1d

def foo3(c):
    a = c.lower()
    dict = {}
    i = 0
    for x in a:
        if x.isalpha():
            if x not in dict.keys():
                dict.update({x: 1})
            else:
                dict[x] += 1
        else:
            i += 1
    if len(a) == i:
        return "Brak liter"
    return max(dict, key=dict.get)

a = input()
print(foo(a))
print(foo1(a))
print(foo2(a))
print(foo3(a))

f = open("zadanie.txt")
b = f.read()
print(foo(b))
print(foo1(b))
print(foo2(b))
print(foo3(b))
f.close()


#zad2
dict = {}
while True:
    a = input()
    if not a:
        break
    else:
        if a not in dict:
            dict.update({a: 1})
        else:
            dict[a] += 1
print(dict)

# zad3

f = open("zadanie.txt")
b = f.read()

a = b.lower()
dict = {}
for x in a:
    if x.isalpha():
        if x not in dict.keys():
            dict.update({x: 1})
        else:
            dict[x] += 1
print(dict)

f.close()
# zad4

f = open("zadanie.txt")
lines = f.readlines()

dict = {}
for l in lines:
    a = l.split()
    for x in a:
        if x.isnumeric():
            if x not in dict:
                dict.update({x: 1})
            else:
                dict[x] += 1
print(dict)

f.close()
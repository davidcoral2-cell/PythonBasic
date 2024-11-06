def ej1():
    a = "Hola"
    b = input("Di alguna palabra ")
    c = [a, b]

    for e in b:
        print(e)

    print(len (b))
    if a == b:
        print("Son iguales")
    else:
        print("Son diferentes")

    print("-".join(c))

    print(b*3)

    if "a" in b:
        print("Tiene la letra A ")
    else:
        print("No tiene A ")


    p = [1, 5, 2, 9, 0, 3, 5, 1, 2, 123, 90]
    print(p[0:9:2])

    p.append("Aguita")
    print(p)
    for w in p:
        print(w)

    p.extend(["koi", "Mando", 33])
    print(p)
    for f in p:
        print(f)
def ej2():
    k = [1, 2, 4, 46, 23, 12]
    m = [12, 123,649, "uwu", 0]
    print(k+m)

def ej3():
    lis = [9, 1, 5, 3, 0, 1, 23, 53]
    lis.insert(2,["iuow", 723])

    print(lis)

def ej4():
    kr = [9, 1, 5, 42, 0, 12312344124, 23, 53]
    kr[5] = "Awah"
    print(kr)

def ej5():
    kr = [9, 1, 5, 42, 0, 12312344124, 23, 53]
    del kr[3:6]
    print(kr)

def ej6():
    kr = [9, 1, 5, 42, 0, 12312344124, 23, 53]
    kr.pop(4)
    print(kr)

def ej7():
    kr = [9, 1, 5, 42, 0, 12312344124, 23, 53]
    kr.clear()
    print(kr)

def ej8():
    kr = [9, 1, 5, 42, 0, 12312344124, 23, 53, 1]
    print(kr.count(1))

def ej9():
    kr = [9, 1, 5, 42, 0, 12312344124, 23, 53]
    kr.sort()
    print(kr)

def ej10():
    kr = [9, 1, 5, 42, 0, 12312344124, 23, 53, 1]
    kr.reverse()
    print(kr)

def ej11():
    kr = [9123, 1, 5, 4221, 12301, 1234124, 23, 53, 1]
    kbr = kr[::-1]
    print(kbr)

ej11()
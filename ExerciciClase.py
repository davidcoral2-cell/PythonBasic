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

def ej12():
    l=[]
    for i in range(4):
        l.append(int(input("Introduce un número: ")))
    print(l)
    suma = 0
    for e in l:
        suma = suma+e
    print("La suma de la lista {} es {} ".format(l, suma))

def ej13():
    p=[]
    a="1"
    suma = 0
    
    while a!=".":
        a =input("Introduce un numero o '.' para acabar: ")
        if a != ".":
            p.append(int(a))
        else:
            print("Adeu")

    f = len(p)

    for e in range(f):
        suma = suma+ p[e]
        
    
    print("La suma de la lista {} es {} y mide {} ".format(p, suma, f))

# Leer lista de num. 

def ej14():
    def listanombres():
        l = []
        a = "0"
        while a != ".":
            a =input("Introduce un numero o '.' para acabar: ")
            if a != ".":
                l.append(int(a))
            else:
                print("Grácias por darme la lsita!")
        return l
    
    def sumarlista(l):
        suma = 0
        for e in l:
            suma = suma + e
        return suma
    
    
    p = listanombres()
    s = sumarlista(p)
    print("La lista es: {} ".format(p))
    print("La suma de toda esa lista es de {} ".format(s))
    print("La lista invertida es: {} ".format(p[::-1]))
    print("Los 2 últimos numeros de tu lista son: {} ".format(p[-2:]))

def ej15():
    def listacaracters():
        l = []
        a = "0"
        while a != ".":
            a =input("Introduce un caracter o '.' para acabar: ")
            if a != ".":
                l.append(a)
            else:
                print("Grácias por darme la lsita!")
        return l
    lis = listacaracters()
    cl = set(lis)
    for i in cl:

        y = lis.count(i)
        print("En la lista: {} . El nuermo {} se repite {} veces ".format(lis,i, y))

def ej16():
    def listacaracters():
        l = []
        a = "0"
        while a != ".":
            a =input("Introduce un caracter o '.' para acabar: ")
            if a != ".":
                l.append(a)
            else:
                print("Grácias por darme la lsita!")
        return l
    lis = listacaracters()
    cl = set(lis)
    if len(lis) == len(cl):
        print("No hay repetidas")
    else:
        print("Hay repetidas")
    


def ej17():
    def listacaracters():
        l = []
        a = "0"
        while a != ".":
            a =input("Introduce un caracter o '.' para acabar: ")
            if a != ".":
                l.append(a)
            else:
                print("Grácias por darme la lsita!")
        return l
    lis = listacaracters()
    cl = set(lis)
    if len(lis) == len(cl):
        print("No hay repetidas")
    else:
        print("Hay repetidas")
    for e in cl:
        if lis.count(str(e)) != 1:
            print("{} Si está repetido!".format(e))
        else: 
            print("{} NO está repetido!".format(e))

def ej18(): #Tuples
    a = (1,2,6,7,3,5,"pito",)
    print(a.count(1))
    print("----------------------")
    print(a.index(3,2))
    print("----------------------")

def ej19(): #Conjunts
    a= {1,2,3,5,7,34,976,3123}
    for e in a:
        print(e)
    print(len(a))

def ej20(): #Diccionaris
    a = {"p":"Pepe","v":"Victor","e3":{"awd":"wdawda","g":"dawd"}}
    print(a["p"])
    print(a["v"])
    print("___________________________")
    a["p"] = "Jose"
    print(a["p"])
    print("___________________________")
    for e in a:
        print('"{}" es igual a: {}'.format(e, a[e]))
    print("__________________________-")
    for x,y in a.items():
        print(x,y)
    print("_____________________")
    print(a.get("e3"))
    print("___________________________")
    print(a.keys())
    print("___________________________")
    print(a.values())

def ej21(): #Operadors
    def matematics():
        a = 12
        b = 18
        c = a%b #+, -, /, *, ** (Exponente), ///// Orden: (), **, * /, + -.
        print(c)
    def comparació():
        a = input("Dime un número ")
        b = int(input("Dime Otro número "))
        if a == b:
            print("SI")
        else:
            print("NO")
        print("-----------------")
        if int(a) == b:
            print("Ahora si que si bby")
        else:
            print("Ahora tampoco")
    
    #Lógics. and, not, or, nor
    
    comparació()

def ej22():
    e = (3+(4*5))/7**4-27
    print(e)

ej22()
from functools import reduce



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

def ej23(): #Menú match
    def mostramenu():
        print("""Este es nuestro menú, estas son las opciones:
              1. Sumar
              2. restar
              3. multiplicar
              4. Dividir
              5. Elevar
              6. Saludar
              7. Despedir
              8. Chiste
              9. Adivinanza
              10. Alago 
              11. Salir""")
            
        op = input("Que quieres hacer? (Numero) ")
        return op

    def suma():
        k = int(input("Dime el primer numero a sumar: "))
        l = int(input("Dime el segundo numero a sumar: "))
        sum = k+l
        print("{} + {} = {}".format(k, l, sum))        
    def resta():
        k = int(input("Dime el primer numero a restar: "))
        l = int(input("Dime el segundo numero a restar: "))
        sum = k-l
        print("{} - {} = {}".format(k, l, sum))    
    def multiplicar():
        k = int(input("Dime el primer numero a multiplicar: "))
        l = int(input("Dime el segundo numero a multiplicar: "))
        sum = k*l
        print("{} x {} = {}".format(k, l, sum))    

    def elevar():
        i = int(input("Dime la base a elevar: "))
        o = int(input("Dime el exponente: "))
        exp = i**o
        print("{} elevado a {} es = {} ".format(i, o, exp)) 

    def dividir():
        k = int(input("Dime el primer numero a dividir: "))
        l = int(input("Dime el segundo numero a dividir: "))
        div = k/l
        print("{} / {} = {}".format(k, l, div))

    def saludar():
        n = input("Como te llamas? ")
        print("Hola, {}. Estoy muy feliz de que hayas venido <3 ")

    def despedir():
        n = input("Como te llamas? ")
        print("Siento que te tengas que ir {} pero que te vaya bien! :) ".format(n)) 
        
    def chiste():
        print("Te voy a contar un chiste, van tres en una moto, y con Harrison FORD :) ")

    def adivinanza():
        b = input("Oro parece, plata no es, ¿Que és?")
        if b == "platano" or b == "Platano":
            print("Has adivinado!")
        else:
            print("Oh no, has perdido, la respuesta era 'Platano'! ")

    def alago():
        print("Eres una persona preciosa, tu mirada es penetrante y tu aroma perfecto.")
    a = ""
    x = mostramenu()
    
    match(x):
        case "1":
            suma()
        case "2":
            resta()
        case "3":
            multiplicar()
        case "4":
            dividir()
        case "5":
            elevar()
        case "6":
            saludar()
        case "7":
            despedir()
        case "8":
            chiste()
        case "9":
            adivinanza()
        case "10":
            alago()
        case "11":
            print("Adeuuuu")
        case _:
            print("Opción no válida \n")


def ej24():
    a = 5
    while(a<=15):
        print(a)
        a = a+1
    print("Acabé ooooo")


def ej25():
    a = 10
    while(a>=0):
        print(a)
        a-=1
    print("UWU")

def ej26():
    a = list()
    b = ""
    while b != ".":
        b = input("Dime una palabra de 4 letras, si no es de 4 no la agregaré. Pon un '.' para acabar ")
        if b != "." and len(b) == 4:
            a.append(b)
        if len(a) == 4:
            break
    print("Tu lista es: {} ".format(a))

def ej27():
    a = list()
    b = ""
    while b != ":":
        b = input("Dime una palabra que empiece por 'A', si no empieza por 'A' no la agregaré. Pon un ':' para acabar ")
        if b != ":" and b[0]=="A":
            a.append(b)
    print("Tu lista es: {} ".format(a))

def ej28():
    a = list()
    b = ""
    while b != "?":
        b = input("Dime una palabra para pasarla entera a minusculas. Pon un '?' para acabar ")
        if b != "?":
            a.append(b.lower())
    print("Tu lista es: {} ".format(a))

def ej29():
    a = list()
    b = ""
    while b != "/":
        b = input("Dime una palabra para pasarla entera a MAYUSCULAS. Pon un '/' para acabar ")
        if b != "/":
            a.append(b.upper())
    print("Tu lista es: {} ".format(a))

def ej30():
    a = list()
    b = ""
    while b != "%":
        b = input("Dime una palabra para pasarla entera a MAYUSCULAS. Pon un '%' para acabar ")
        if b != "%":
            a.append(b.title())
    print("Tu lista es: {} ".format(a))

def ej31():
    l = list()
    a = ""

    while a != ".":
        a = input("Dime una frase de máximo 80 caracteres: ")
        if len(a) <= 80 and a != ".":
            l.append(a.title())
    
    print(l)

def ej31():
    l = list()
    a = ""

    while a != ".":
        a = input("Dime una frase de máximo 80 caracteres: ")
        if len(a) <= 80 and a != ".":
            s=a.lower()
            p = s.title()
            l.append(p)
    
    print(l)

def ej32():
    def hacerlista():
        l=[]
        p=""
        while p != ".":
            p = input("Dime un número ")
            if p != ".":
                l.append(int(p))
        return l
    
    l = hacerlista()
    r = list()
    for i,e in enumerate(l):
        if e == i:
            r.append(e)
    print(r)
            
def ej33():
    def hacerlista():
        l=[]
        p=""
        while p != ".":
            p = input("Dime un número ")
            if p != ".":
                l.append(int(p))
        return l
    
    l = hacerlista()

def ej34():
    
    def sumarlista(l):
        for i in range (len(l)):
            l[i]*=3

    l = [3,4,5]
    print(l)
    sumarlista(l)
    print(l)

def ej35():
    def sumarl(l):
        ls=[]
        for e in l:
            e = e+5
            ls.append(e)
        return ls

    l = [2,3,4 ]
    print(l)
    s = sumarl(l)
    print("La lista modificada es  {} y sin modificar {}".format(s,l))

def ej36():
    l = [3,4,5,7,10]
    r = list(map(lambda x: x*2, l))
    print(r)

def ej37():
    def aaa(x):
        return x**5
    
    l = [3,4,5,7,10]

    k = list(map(lambda x: aaa(x), l))
    print(k)

    r = list(map(lambda x: x**5, l))
    print(r)

    m = list()
    for e in l:
        m.append(e**5)
    print(m)

def ej38():
    l = [3,4,5,7,10]
    def sino(x):
        if x%2==0:
            return True
        return False
    a = list(filter(sino,l))
    print(a)

    r = list(filter(lambda x: x%2!=0,l))

    print(r)

def ej39():
    n = int(input('Dime un numero: '))
    def fact(n):
        if n <= 0:
            return 1
        else:
            return n*fact(n-1)
    print(fact(n))

def ej40():

    l=[2,5,6,123,754,864]
    j=[1,3,65,8566,45,3]

    x = reduce(lambda x,y:x+y, l)
    h = reduce(lambda x,y:x*y, j)

    print("{} ||||| {} ".format(x, h))

def ej41():

    s = input("Una cadena de caracteres ")
    l=list(s)
    r = []
    for e in l:
        if e in "aeiouAEIOUáéíóúàèìòùäöëïüÄËÏÖÜ":
            r.append(".")
        else:
            r.append(e)
    s = " ".join(r)
    print(s)

def ej42():
    s = input("Una cadena de caracteres ")
    l=list(s)
    r = []
    for e in l:
        if e in "AQWSZXCDERFVBGTYHNMJUIKLOPÑÇ":
            r.append(".")
        else:
            r.append(e)
    s = " ".join(r)
    print(s)

def ej43():
    
    s = input("Una cadena de caracteres ")
    l=list(s)
    r = []
    for e in l:
        if e in "QWSZXCDRFVBGTYHNMJKLPÑÇ":
            r.append("-")
        elif e in "aeiouAEIOUáéíóúàèìòùäöëïüÄËÏÖÜ":
            r.append(".")
        else:
            r.append(e)
    s = " ".join(r)
    print(s)

def ej44():
    def crearlista():
        l = []
        par = ""
        while par != ".":
            par = input("Dime una palabra, pon un '.' para acabar: ")
            if par != ".":
                l.append(par)
        return l

    def paraules(l):
        a = []
        c = []
        for e in l:
            a.append(len(e))
        b = set(a)
        a.clear()
        for e in b:
            y = len(list(filter(lambda x:x==e,a)))
            c.append([e, y])
        return c

    l = crearlista()
    p = paraules(l)
    print("En la lista {} Se repiten: {}".format(l, p))

def ej45():
    a = "adwawdahoijoduiawidohdp"
    b = a.split()
    print(b)

def ej46():
    def crearlista():
        l = []
        par = ""
        while par != ".":
            par = input("Dime una palabra, pon un '.' para acabar: ")
            if par != ".":
                l.append(par)
        return l
    def mostrar(t, min, max):
        print("Els números entre aquests 2 son: {}".format(list(filter(lambda x: x>min and x<max,t))))

    crearlista()   

def ej47():
    def crearlista():
        l = []
        par = ""
        while par != ".":
            par = input("Dime un nombre, pon un '.' para acabar: ")
            if par != ".":
                l.append(par)
        return l


    def nums_que_comencen_per(l):
        r = []
        for e in l:
            if len(e) % 2== 1:
                m = len(e)//2
                r.append(e[m])
            else:
                m = len(e)//2
                m2 = m-1
                r.append(e[m2]+e[m])
                
        print("De tu lista {}, los que comienzan por són: {}. Estos en total són {} nombres. ".format(l, r, len(r)))

    l = crearlista()
    nums_que_comencen_per(l)
 
def ej47():
    def crearlista():
        l = []
        par = ""
        while par != ".":
            par = input("Dime un nombre, pon un '.' para acabar: ")
            if par != ".":
                l.append(par)
        return l


    def nums_que_comencen_per(l):
        def comparar(e,l):
             
             e and l
        def comparar2(e1, e2, l):
          aaa = "a"  
        
        r = []
        for e in l:
            senar = len(e) % 2 == 1
            if senar:
                comparar(e[len(e)//2],*l.remove(e))
            else:
                comparar2(e[len(e)//2], e[len(e)//2 +1], + l.remove(e))
        
                       
                
        print("De tu lista {}, los que comienzan por són: {}. Estos en total són {} nombres. ".format(l, r, len(r)))

    l = crearlista()
    nums_que_comencen_per(l)






ej47()


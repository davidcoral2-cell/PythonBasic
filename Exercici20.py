
def menu():
    op=0
    while op < 1 or op > 16:
    
        print("-------------------------")
        print("1. Sumar" )
        print("2. Restar ")
        print("3. Multiplicar ")
        print("4. Dividir ")
        print("5. Cambio de base ")
        print("6. ¿Que numero es mayor? ")
        print("7. De 3 numeros, ¿cual es mayor? ")
        print("8. Calcular longitud de una cadena ")
        print("9. Calcular longitud de una lista ")
        print("10. ¿Esto es una vocal? ")
        print("11. Sumar lista ")
        print("12. Multiplicar lista ")
        print("13. Invertir texto ")
        print("14. Encontrar palindromos ")
        print("15. Comparar 2 llistes ")
        print("16. Salir ")
        print("-------------------------")
        

        print("-------------------------")

        op = int(input("Que operación quieres hacer? "))


        print("-------------------------")
        
    return op

def suma():
    print("-------------------------")

    n1 = int(input("Dime el primer numero a calcular: "))

    print("-------------------------")

    print("-------------------------")

    n2 = int(input("Dime el segundo numero a calcular: "))

    print("-------------------------")

    s = n1 + n2
    print ("{} + {} = {}".format(n1, n2, s))

def resta():

    print("-------------------------")

    n1 = int(input("Dime el primer numero a calcular: "))

    print("-------------------------")

    print("-------------------------")

    n2 = int(input("Dime el segundo numero a calcular: "))

    print("-------------------------")
    s = n1 - n2
    print ("{} - {} = {}".format(n1, n2, s))

def multi():
    print("-------------------------")

    n1 = int(input("Dime el primer numero a calcular: "))
    
    print("-------------------------")

    print("-------------------------")

    n2 = int(input("Dime el segundo numero a calcular: "))

    print("-------------------------")
    s = n1 * n2
    print ("{} x {} = {}".format(n1, n2, s))

def divi():
    print("-------------------------")

    n1 = int(input("Dime el primer numero a calcular: "))

    print("-------------------------")

    print("-------------------------")

    n2 = int(input("Dime el segundo numero a calcular: "))

    print("-------------------------")

    if n2 == 0:
        print("No se puede dividir por cero.")
    else:
        s = n1 / n2
    print ("{} / {} = {}".format(n1, n2, s))

def cdb():
    numero = input("¿Que numero quieres convertir? ")
    bini = int(input("¿En que base está el numero introducido anteriormente? (Base: 2 = binario | 8=octal | 10=decimal | 16=hexadecimal) "))
    bfin = int(input("¿A que base lo quieres convertir? (Base: 2 = binario | 8=octal | 10=decimal | 16=hexadecimal) "))
    
    if bini == 2:
        dec= int(numero, 2)
    elif bini == 8: 
        dec= int(numero, 8)
    elif bini == 10:
        dec= int(numero, 10)
    elif bini == 16:
        dec = int(numero, 16)
    else:
        print("Base inicial no válida")
        return
    
    if bfin == 2:
        r = bin(dec)[2:]
    elif bfin == 8:
        r = oct(dec)[2:]
    elif bfin == 10:
        r = str(dec)
    elif bfin == 16:
        r = hex(dec)[2:]
    else:
        print("Base final no válida")
        return

    print("el número {} de base {} pasandolo a base {} es igual a {}".format(numero, bini, bfin, r))

def gran():
    k = int(input("Dime un numero "))
    l = int(input("Dime otro numero "))

    if k > l:
        print("{} es mayor que {} ".format(k, l))
    elif l > k:
        print("{} es mayor que {} ".format(l, k))
    else:
        print("Los números {} y {} son iguales. ".format(k, l))

def grandetres():
    g = int(input("Dime un numero "))
    h = int(input("Dime otro numero "))
    j = int(input("Dime un tercero "))

    if g > h and g > j:
        print("{} es mayor que {} y {} ".format(g, h, j))
        print("{} es mayor que {} y {} ".format(h, g, j))
    elif j > g and j > h:
        print("{} es mayor que {} y {} ".format(j, g, h))
    else:
        print("Los tres numeros son iguales.")

def calclon():    
    q = input("Dime una cadena ")
    def long(q):
        return len(q)
    lgcad = long(q)
    print("La longitud de la cadena {} és: {}".format(q, lgcad))

def lista():
    def crlista():
        i = []
        while True:
            o = input('Escribe valores a tu lista y pon "fin" para acabar: ')
            if o.lower() == "fin":
                break
            i.append(o)
        return i

    def calcularlista(i):
        return len(i)

    i = crlista() 
    print("La lista creada es: {}".format(i))    
    print("La longitud es de: {}".format(calcularlista(i)))

def vocal():
    def posiblesvocal(letra):
        vocales = "aeiouAEIOUáéíóúàèìòùäëïöü"
        return letra in vocales
    
    def listavocales():
        i = []
        while True:
            o = input('Escribe las letras a tu lista y pon "fin" para acabar: ')
            if o.lower() == "fin":
                 break
            i.append(o)
        return i
    
    letras = listavocales()

    for letra in letras:
        r = posiblesvocal(letra)
        print("El carácter {} és una vocal? {} ".format(letra, r))

def r_sumar_lista():
    def crear_lista():
        i = []
        while True:
            o = input('Escribe los numeros a la lista y pon "fin" para acabar: ')
            if o.lower() == "fin":
                 break
            i.append(float(o))
        return i
    def sumar_lista(i):
        suma = 0
        for num in i:
            suma += num
        return suma
    listaa = crear_lista()
    r = sumar_lista(listaa)
    print("La suma de la lista es: {} ".format(r))

def r_multi_lista():
    def crear_lista():
        i = []
        while True:
            o = input('Escribe los numeros a la lista y pon "fin" para acabar: ')
            if o.lower() == "fin":
                 break
            i.append(float(o))
        return i
    def multip_lista(i):
        mult = 1
        for num in i:
            mult *= num
        return mult
    listaa = crear_lista()
    r = multip_lista(listaa)
    print("La multiplicacion de la lista es: {} ".format(r))

def invertir():
    a = input("Dime el texto que quieres invertir: ")
    inva = a[::-1]
    print(inva)

def palindrom():
    a = input("Dime una palabra y te dire si es palindroma o no. ")
    inva = a[::-1]
    if a == inva:
        print("La palabra {} es palindroma".format(a))
    else:
        print("La palabra {} NO es palindroma".format(a))

def superposicio():
    def lista1(a):
       i = []
       while True:
            o = input('Escribe valores a tu lista y pon "fin" para acabar: ')
            if o.lower() == "fin":
                break
            i.append(o)
            return i
    def lista2(b):
        y = []
        while True:
            o = input('Escribe valores a tu segunda lista y pon "fin" para acabar: ')
            if o.lower() == "fin":
                break
            y.append(o)
            return y
    def compararlista():
        p = str(i.split)
        l = str(y.split)
        return p in l        


def error():
    print("-------------------------")
    print("La opción no es valida ")
    print("-------------------------")

a = True
while a:

    op=menu()

    match op:
        case 1:
            suma()
        case 2:
            resta()
        case 3:
            multi()
        case 4:
            divi()
        case 5:
            cdb()
        case 6:
            gran()
        case 7:
            grandetres()
        case 8:
            calclon()
        case 9:
            lista()
        case 10:
            vocal()
        case 11:
            r_sumar_lista()
        case 12:
            r_multi_lista()
        case 13:
            invertir()
        case 14:
            palindrom()
        case 15:
            superposicio()
        case 16:
            print("Adios")
            a = False
        case _:
            error()
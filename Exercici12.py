def menu():
    op=0
    while op < 1 or op > 6:
    
        print("-------------------------")
        print("1. Sumar")
        print("2. Restar")
        print("3. Multiplicar")
        print("4. Dividir")
        print("5. Cambio de base")
        print("6. Salir")
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
    numero = input("¿Que nuemro quieres convertir? ")
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
            print("Adeu")
            a=False
        case _:
            error()

def menu():
    op=0
    while op < 1 or op > 5:
    
        print("-------------------------")
        print("1. Sumar")
        print("2. Restar")
        print("3. Multiplicar")
        print("4. Dividir")
        print("5. Salir")
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
            print("Adeu")
            a=False
        case _:
            error()
def suma(num):
    a = sum(int(b) for b in str(num) )
    return a
def comprobar(num, sumar):
    if sumar % 2 == 1:
        print("El número {}, sumamos sus digitos, (el resultado es {}) y este es INPAR. ".format(num,sumar))
    else:
        print("El número {}, sumamos sus digitos, (el resultado es {}) y este es PAR. ".format(num,sumar))

num = int(input("Dime un numero: "))
sumar = suma(num)
comprobar(num, sumar)



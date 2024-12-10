def numini():
    b= 0
    while b != 1:
        a = int(input("Dime un numero entre 1 y 900000: "))
        if a > 1 and a < 900000:
            b = 1
            return a
        else:
            print("número no válido")

a = numini()
print("El digito {} tiene {} digitos.".format(a, len(str(a))))
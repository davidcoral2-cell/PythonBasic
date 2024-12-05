def bintodec(a):
    b = int(a, 2)
    return b

a=input("Dime un numero en binario: ")
c = bintodec(a)
print("El número binario {}, en decima, es: {}".format(a, c))
def calcular(a):
    suma = 0
    while a > 0:
        suma += a**2
        print("{} ** 2 = {}".format(a, a**2))  
        a -= 4
    return suma
def numini():
    b = 0
    while b != 1:
        a = int(input("Dime un numero entre 4 y 100: "))
        if a >=4 and a <= 100:
            b=1 
        else:
            print("VALOR NO VALIDO.")
    return a
a = numini()
suma = calcular(a)
print("La suma de cuadrados, quedaria así: ")


    
    
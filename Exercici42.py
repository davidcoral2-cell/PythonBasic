def numero():
    b = 1
    while b != 0:
        a = int(input("Dime un numero entre el 1 y el 20: "))
        if a >=1 and a <=20:
            b = 0
            return a
        else:
            print("Numero fuera de rango (1-20).")

def tablas(a):
    b = 1
    while b != 21:
        n = a * b
        print("{} * {} = {}".format(a,b,n))
        b += 1

a = numero()
tablas(a)

def calcular(r, a):
    while a-4 >=0:
        r.append("{} ** 2 = {}".format(a, a**2))
        a -= 4
    return r

b = 0
r= []
while b != 1:
    a = int(input("Dime un numero entre 4 y 100: "))
    if a >=4 and a <= 100:
        for e in r: 
            calcular(r, a)
    else:
        print("VALOR NO VALIDO.")
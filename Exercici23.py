def puntos():
    i1 = []
    n = 0
    print("Vamos a crear tu lista de 3 números para hacer el dibujo.")
    while n != 3:
        f = input("Añade un número entero a la lista: ")
        i1.append(int(f))
        n += 1
    return i1
def creardib(lista1):
    for e in lista1:
        print("." * e)
def creardib(lista2):
    for e in lista2:
        print("." * e)


lista1 = puntos()
lista2 = puntos()
creardib(lista1)
creardib(lista2)

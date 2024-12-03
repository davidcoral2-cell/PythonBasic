def sumar_lista():
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

def multi_lista():
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

q = input("Que quieres hacer, 'sumar' o 'multiplicar': ")
if q == "sumar":
    sumar_lista()
elif q == "multiplicar":
    multi_lista()
else: 
    print("Error, opción no válida. ")
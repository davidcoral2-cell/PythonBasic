def calclon():    
    q = input("Dime una cadena ")
    def long(q):
        return len(q)
    lgcad = long(q)
    print("La longitud de la cadena {} és: {}".format(q, lgcad))

def lista():
    def crlista():
        i = []
        while True:
            o = input('Escribe valores a tu lista y pon "fin" para acabar: ')
            if o.lower() == "fin":
                break
            i.append(o)
        return i

    def calcularlista(i):
        return len(i)

    i = crlista() 
    print("La lista creada es: {}".format(i))    
    print("La longitud es de: {}".format(calcularlista(i)))

y = input("Que quieres calcular, una 'lista' o 'cadena': ")
if y == "lista":
    lista()
elif y == "cadena":
    calclon()
else: 
    print("Error, opción no válida. ")
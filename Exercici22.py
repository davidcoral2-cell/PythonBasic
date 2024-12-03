       
def puntos():
    i1=list()
    f = ""
    u = "."
    n = 0
    print("Vamos a crear tu lista de 3 numeros para ver cuantas veces repito los numeros. ")
    while n!= 3:
        f = input("Añade un numero a la lista. Pon un '.' ")
        i1.append(int(f))
        n += 1
    for e in i1:
        print(u*e)
    
puntos()

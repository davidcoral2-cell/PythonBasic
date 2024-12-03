def crearlista():
    l = []
    par = ""
    while par != ".":
        par = input("Dime una palabra, pon un '.' para acabar: ")
        if par != ".":
            l.append(par)
    return l

a = int(input("Cuantas letras mínimas tiene que tener la palabra para poder pasar el filtro?"))

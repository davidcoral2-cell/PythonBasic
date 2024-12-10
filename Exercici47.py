def crearlista():
        l = []
        par = ""
        while par != ".":
            par = input("Dime un elemento, pon un '.' para acabar: ")
            if par != "." :
                l.append(par)
        return l

def comprobarrepes(l):
    if len(l) == len(set(l)):
        print("No hay repetidas")
    else:
        print("Si hay repetidas")

l = crearlista()
comprobarrepes(l)
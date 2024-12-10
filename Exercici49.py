def crearlista():
    l = []
    par = ""
    while par != ".":
        par = input("Dime un elemento, pon un '.' para acabar: ")
        if par != ".":
            l.append(par)
    return l

def comprobarrepes(l,repes):
    if len(l) == len(set(l)):
        print("No hay repetidas")
    else:
        print("la lista sin repetidas es: {}. Es decir, habia {} repetidas ({})".format(set(l), len(l)-len(set(l)),repes ))

def listarepes(l):
    repes = []
    for e in l:
        if l.count(e) > 1 and e not in repes:
            repes.append(e)
    return repes

l = crearlista()
print("Tu lista es: {}".format(l))
repes = listarepes(l)
comprobarrepes(l,repes)
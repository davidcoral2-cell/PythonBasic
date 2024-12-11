def crearlista():
    l = []
    par = ""
    while par != ".":
        par = input("Dime un elemento, pon un '.' para acabar: ")
        if par != ".":
            l.append(par)
    return l

def index_paraules(l):
    u = 0
    par = input("Dime una palara y te diré en que lugar está. ")
    if par not in l:
        u = -1
        print("La palabra está en la posición {} (NO ESTÄ)".format(u))
    for e in l: 
        if e == par:
            print("La palabra está en la posición {} ".format(u)) 
        else:
            u +=1
    



l = crearlista()
index_paraules(l)


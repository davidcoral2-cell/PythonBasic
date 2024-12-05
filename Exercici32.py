def crearlista():
    l = []
    par = ""
    while par != ".":
        par = input("Dime un nombre, pon un '.' para acabar: ")
        if par != ".":
            l.append(par)
    return l


def nums_que_comencen_per(l, a):
    r = []
    for e in l:
        if e[0] == a.upper() or e[0] == a.lower():
            r.append(e)
    print("De tu lista {}, los que comienzan por {} són: {}. Estos en total són {} nombres. ".format(l, a, r, len(r)))

l = crearlista()
a = input("Por que letra quieres filtrar? ")
nums_que_comencen_per(l, a)
    
    
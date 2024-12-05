def crearlista():
    l = []
    par = ""
    while par != ".":
        par = input("Dime un nombre, pon un '.' para acabar: ")
        if par != ".":
            l.append(par)
    return l


def nums_que_comencen_per(l):
    r = []
    for e in l:
        if e[0] == "A" or e[0]=="a":
            r.append(e)
    print("De tu lista {}, los que comienzan por 'A' són: {}. Estos en total són {} nombres. ".format(l, r, len(r)))

l = crearlista()
nums_que_comencen_per(l)
    
    
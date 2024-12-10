import random
def crearlista():
    r = []
    h = 0
    while h != 20:
        a = random.randint(1,100)
        r.append(a)
        h += 1
    return r

def comprobarrepes(l,repes):
    if len(l) == len(set(l)):
        print("No hay repetidas")
    else:
        print("Si hay repetidas")
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
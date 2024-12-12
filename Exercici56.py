def crearlista():
        l = []
        par = ""
        while par != ".":
            par = input("Dime un elemento, pon un '.' para acabar: ")
            if par != "." :
                l.append(par)
        return l
def elementsparells(l):
    return [l[i] for i in range(len(l)) if i % 2 == 0]

l = crearlista()
r = elementsparells(l)
print("De la lista {}, los elementos en indice par son: {}".format(l,r))

def crearlista():
    l = []
    par = ""
    while par != ".":
        par = input("Dime una palabra, pon un '.' para acabar: ")
        if par != ".":
            l.append(par)
    return l

def filtro(x, y):
    g = list()
    for e in x:
        if y <= len(e):
            g.append(e)
    return g


x = crearlista()
y = int(input("De cuantas letras debe ser el filtro? "))
k = filtro(x, y)

filtro(x, y)
print("de la lista {} que tenguin més de {} carácters, són: {}".format(x, y, k))
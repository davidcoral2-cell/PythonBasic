def crearlista():
    l = []
    par = ""
    while par != ".":
        par = input("Dime un nombre, pon un '.' para acabar: ")
        if par != ".":
            l.append(par)
    return l

def eliminarcapycua(l):
    return l[1:-1]

l = crearlista()
cc = eliminarcapycua(l)
print("{}. Sin el inicio y el final es = {} ".format(l,cc))
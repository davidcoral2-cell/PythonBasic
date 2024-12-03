def crearlista():
    l = []
    par = ""
    while par != ".":
        par = input("Dime una palabra, pon un '.' para acabar: ")
        if par != ".":
            l.append(par)
    return l

def paraula_llarga(l):
        return(max(l, key=len))
 
l=[]
print("Tu lista inicial es: {} (vacio) ".format(l))
l = crearlista()
print("Tu lista final es: {} ".format(l))
print("La palabra más larga és: {} que tiene {} caracteres".format(paraula_llarga(l), len(paraula_llarga(l))))


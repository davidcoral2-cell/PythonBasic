def crearlista():
        l = []
        par = ""
        while par != ".":
            par = input("Dime un numero, pon un '.' para acabar: ")
            if par != "." :
                l.append(int(par))
        return l

def orden(lista):
    
    if lista == sorted(lista):
        return("la lista está ordenada correctamente ASCENDENTEMENTE.")
    elif lista == sorted(lista, reverse=True):
        return("la lista está ordenada en orden DESCENDENTE correctamente.")
    else:
        return "La lista NO está ordenada"
        
lista= crearlista()
print(orden(lista))
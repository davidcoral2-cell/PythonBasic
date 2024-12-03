def vocal():
    def posiblesvocal(letra):
        vocales = "aeiouAEIOUáéíóúàèìòùäëïöü"
        return letra in vocales
    
    def listavocales():
        i = []
        while True:
            o = input('Escribe las letras a tu lista y pon "fin" para acabar: ')
            if o.lower() == "fin":
                 break
            i.append(o)
        return i
    
    letras = listavocales()

    for letra in letras:
        r = posiblesvocal(letra)
        print("El carácter {} és una vocal? {} ".format(letra, r))
        
vocal()

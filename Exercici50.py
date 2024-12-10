def crear_llista_fitxer(fichero):
    l = []
    Archivo = open(fichero, "r")
    for line in Archivo:
        for e in line.split():
            l.append(e.strip())
    Archivo.close()
    return l

print(crear_llista_fitxer("palabras.txt"))
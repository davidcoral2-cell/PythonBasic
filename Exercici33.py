def contar(p2):
    a = 0
    e = 0
    i = 0
    o = 0
    u = 0
    for letra in p2:
        if letra == 'a':
            a += 1
        elif letra == 'e':
            e += 1
        elif letra == 'i':
            i += 1
        elif letra == 'o':
            o += 1
        elif letra == 'u':
            u += 1
    print("Hay {} A, {} E, {} I, {} O, {} U".format(a,e,i,o,u))

p = input("Dime una palabra ")
p2 = p.lower()
contar(p2)


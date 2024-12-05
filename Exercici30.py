def mostrar_majors_que(numeros, major):
    majors = []
    for num in numeros:
        if num > major:
            majors.append(num)
    print("Els nombres majors que {} són: {}".format(major, majors))

valors = input("Escriu els nombres, però separats per comes: ")
valsep = valors.split(',')
tupla = tuple(int(num) for num in valsep)

mostrar_majors_que(tupla, 18)
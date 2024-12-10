def estrepas(any):
    if any % 4 == 0:
        if any % 100 != 0 or any % 400 == 0:
            print("El año {} es bisiesto".format(any))
    else:
           print("El año {} NO es bisiesto".format(any))

any = int(input("Dime un año: "))
estrepas(any)
        

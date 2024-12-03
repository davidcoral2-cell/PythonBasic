def grandetres():
    g = int(input("Dime un numero "))
    h = int(input("Dime otro numero "))
    j = int(input("Dime un tercero "))

    if g == h and h == j:
        print("Los tres números son iguales.")
    elif g >= h and g >= j: 
        print("{} es mayor que {} y {}.".format(g, h, j))
    elif h >= g and h >= j:
        print("{} es mayor que {} y {}.".format(h, g, j))
    elif j >= g and j >= h:
        print("{} es mayor que {} y {}.".format(j, g, h))

grandetres()
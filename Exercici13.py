def gran():
    k = int(input("Dime un numero "))
    l = int(input("Dime otro numero "))

    if k > l:
        print("{} es mayor que {} ".format(k, l))
    elif l > k:
        print("{} es mayor que {} ".format(l, k))
    else:
        print("Los números {} y {} son iguales. ".format(k, l))
        
gran()

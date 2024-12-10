def digits(num):
    b = list()
    for a in str(num):
        if int(a) % 2 == 0 :
            b.append(int(a))
    return b

num = int(input("Introdueix un número: "))
parells = digits(num)

if parells:
    print("Els dígits parells de {} són: {}".format(num, parells))
else:
    print("El número {} no té dígits parells.".format(num))
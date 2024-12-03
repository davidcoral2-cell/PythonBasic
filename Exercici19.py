def palindrom():
    a = input("Dime una palabra y te dire si es palindroma o no. ")
    inva = a[::-1]
    if a == inva:
        print("La palabra {} es palindroma".format(a))
    else:
        print("La palabra {} NO es palindroma".format(a))


palindrom()
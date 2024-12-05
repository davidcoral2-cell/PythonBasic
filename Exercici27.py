
def numdemayus(a):
    mayus = 0
    for e in a:
        if e.isupper():
            mayus += 1
    return mayus

def numdeminus(a):
    min = 0
    for e in a:
        if e.islower():
            min += 1
    return min

a = input("Dime una cadena de texto y te diré cuantas letras en mayuscula y en minuscula hay. ")
nmy = numdemayus(a)
nms = numdeminus(a)
print("En la cadena {} hay {} mayusculas y {} minusculas. ".format(a, nmy, nms))


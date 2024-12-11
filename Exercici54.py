def suma(num1, num2):
    s = 0
    b = 0
    if num2 > num1:
        while num1 <= num2:
            s += num1
            num1 += 1
    else:
        while num2 <= num1:
            s += num2 
            num2 += 1
    return s

num1 = int(input("Dime el 1er numero "))
num2 = int(input("Dime el 2ndo numero "))
s = suma(num1, num2)
print("La suma de todos los numeros entre {} y {} es: {}".format(num1,num2,s))
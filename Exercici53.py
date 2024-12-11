def pares():
    for i in range(1,101):
        if i % 2 == 0:
            print(i)

def inpares():
    for i in range(1,101):
        if i % 2 != 0:
            print(i)

pares()
print("-------------------")
inpares()
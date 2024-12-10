def rimas(pal1, pal2):
    fin1 = pal1[-3:]
    fin2 = pal2[-3:]
    cas1 = pal1[-2:]
    cas2 = pal2[-2:]
    if fin1 == fin2:
        print("{} y {} RIMAN. ".format(pal1, pal2))
    elif cas1 == cas2:
        print("{} y {} RIMAN UN POCO. ".format(pal1, pal2))
    else:
        print("{} y {} NO RIMAN. ".format(pal1, pal2))

pal1 = input("Dime la primera palabra. ")
pal2 = input("Dime la segunda palabra. ")
rimas(pal1, pal2)

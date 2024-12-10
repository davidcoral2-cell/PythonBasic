import random

def solicitar():
    a= 0
    while a != 1:
        cini= int(input("Dime tu capital a solicitar (mínim 50000€ màxim 800000€): "))
        if cini >= 50000 and cini <=800000:
            a = 1
        else: 
            print("Valor NO válido. Introduce un valor válido. ")
    return cini

def plazo():
    a= 0
    while a != 1:
        años = int(input("En cuantos años lo quieres pagar? (MIN: 3 años // MAX 40 años. )"))
        if años >= 3 and años <=40:
            a = 1
        else: 
            print("Valor NO válido. Introduce un valor válido. ")
    return años

def interes():
    a= 0
    while a != 1:
        interes = random.uniform(0.5, 13)
        if interes >= 0.5 and interes <=13:
            a = 1
        else: 
            print("Valor NO válido. Introduce un valor válido. ")
    return interes

solici = solicitar()
pl = plazo()
inter = interes()
nose = "%"
Cfinal = solici * (1+ inter/100) ** pl

print("{}€ a {}{} d'interés a {} anys s'ha de convertir en: {}".format(solici, inter,nose, pl, Cfinal))
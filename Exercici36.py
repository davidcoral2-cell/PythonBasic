import random

def generar_codi():
    return [random.randint(0, 9) for _ in range(4)]


def comparar_codis(codi_secret, codi_usuari):
    correctes = sum(1 for i in range(4) if codi_secret[i] == codi_usuari[i])
    coinc = sum(1 for x in codi_usuari if x in codi_secret) - correctes
    return correctes, coinc

def main():
    print("MasterMind: Endevina el codi secret de 4 xifres!")
    codi_secret = generar_codi()
    intents = 0

    while True:
        a = input("Introdueix un codi de 4 xifres: ")
        if len(a) != 4 or not a.isdigit():
            print("Entrada no vàlida.")
            continue
        codi_usuari = [int(x) for x in a]
        intents += 1
        correctes, coinc = comparar_codis(codi_secret, codi_usuari)
        if correctes == 4:
            print("Felicitats! Has encertat el codi {} en {} intents.".format(codi_secret, intents))
            break
        print("Correctes: {}, Coincidents: {}".format(correctes, coinc))

main()
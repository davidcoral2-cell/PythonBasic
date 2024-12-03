def superposicio():
    def crlist1():
        i1=list()
        f = ""
        print("Vamos a crear tu 1era lista ")
        while f!= ".":
            f = input("Añade un elemento a la PRIMERA lista. Pon un '.' para acabar ")
            if f!= ".":
                i1.append(f)
            else:
                print("Has acabado la lista número 1")

        return i1
    

    list1 = crlist1()
    list2 = crlist1()
    ls = list()
    lm = list()
    t = set(list1)
    u = set(list2)
    for e in t:
            for n in u:
                if e in n or n in e:
                    ls.append(e)
                else:
                    lm.append(e)
    print("Se repiten: {} || No se repiten: {} ".format(set(ls), set(lm)))

superposicio()
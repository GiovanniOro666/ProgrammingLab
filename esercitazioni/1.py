def stampa(lista):
    for item in lista:
        print(item)

def statistica(lista):
    for item in lista:
        if type(item) is int:
            lista.sort()
    print('somma', sum(lista))
    print('media', sum(lista)/len(lista))
    print('minimo', lista[0])
    print('massimo', lista[-1])

def sommavettoriale(lista1, lista2):
    listarisultato = []
    if len(lista1) == len(lista2):
        for item in lista1:
            if type(item) is not int:
                print('non sono interi l1')
        for item in lista2:
            if type(item) is not int:
                print('non sono interi l2')

        for i, item in enumerate(lista1):
            listarisultato.append(lista1[i]+lista2[i])
        print(listarisultato)
    else:
        print('sei scemo')
        
lista1 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
lista2 = [0, 0, 0, 0, 0, 0, 0, 0, 0]
sommavettoriale(lista1, lista2)
#stampa(listaprova)
#statistica(listaprova)

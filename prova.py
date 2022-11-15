lista = [1,6,4,9]
def somma(lista):       #funzione somma
    if None in lista:
        return 0
    else:
        som = 0
        for item in lista:
            som = som + item
        return som


risultato = somma(lista)
print('somma = {}'.format(risultato))
    
    
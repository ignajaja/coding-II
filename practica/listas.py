def contar_pares_slicing(lista): #version slicing, se altera la lista
    cantidad_pares = 0
    while lista != []:
        if lista[0] % 2 == 0:
            cantidad_pares += 1
        lista = lista[1:]
    return cantidad_pares


def contar_pares_index(lista): #version indice, no se altera la lista
    cantidad_pares = 0
    n = len(lista)
    i = 0
    while i != n:
        if lista[i] %2 == 0:
            cantidad_pares += 1
        i += 1
    return cantidad_pares


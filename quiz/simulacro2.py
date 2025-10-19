def maximas_secuencias(lista):
    lista.append(lista[-1])
    res = []
    secuencia = []
    largo_max = 1

    for i in range(1, len(lista)):
        secuencia.append(lista[i-1])

        if not lista[i] >= lista[i-1]:
            if len(secuencia) == largo_max:
                res.append(secuencia)
            elif len(secuencia) > largo_max:
                res = [secuencia]
                largo_max = len(secuencia)
            secuencia = []
    if len(secuencia) == 1:
        return res[0]
    return res


# print(maximas_secuencias([1,2,3,2,3]))


def es_magica(matriz):
    suma = 0
    list_result_colu = []
    list_result_diag = []

    for num in matriz[0]:
        suma += num
        list_result_colu.append(0)
        list_result_diag.append(0)

    for i1 in range(len(matriz)):
        if not sum(matriz[i1]) == suma:
            return False
        for i2 in range(len(matriz[0])):
            list_result_colu[i2] += matriz[i1][i2]

            if i1 == i2:
                list_result_diag[i1] += matriz[i1][i2]

                

    for item in list_result_colu:
        if not item == suma:
            return False
        
    it = 0 
    for item in list_result_diag:
        it += item
    if not it == suma:
        return False
    
    return True

# print(es_magica([[8,1,6],[3,5,7],[4,9,2]]))


def es_magica_v2(matriz):
    suma = sum(matriz[0])
    filas = len(matriz)
    columnas = len(matriz[0])

    for fila in matriz:
        if not fila == suma:
            return False

    for i in range(columnas):
        actual = []
        for j in range(filas):
            actual.append(matriz[j][i])
        if not sum(actual) == suma:
            return False
        
    diagonal = []
    anti_diag = []

    for i in range(filas):
        diagonal.append(matriz[i][i])
        anti_diag.append(matriz[i][filas-1-i])

    if sum(diagonal) != suma or sum(anti_diag) != suma:
        return False
    
    return True


def eliminar_con_ceros(matriz):
    list_result = []

    list_ceros_fil = []
    list_ceros_col = []

    for i1 in range(len(matriz)):
        for i2 in range(len(matriz[0])):
            if matriz[i1][i2] == 0:
                list_ceros_col.append(i2)
                list_ceros_fil.append(i1)

    for i1 in range(len(matriz)):
        if not i1 in list_ceros_fil:
            for i2 in range(len(matriz[0])):
                if not i2 in list_ceros_col:
                    list_result.append(matriz[i1][i2])

    size = len(matriz[0]) - len(list_result[0])

    return list_result

# print(eliminar_con_ceros([[1,2,0],[4,5,6],[7,8,9]]))
# print(eliminar_con_ceros([[1,2,3,4],[5,6,7,8],[9,10,0,0],[13,14,15,16]]))

def elementos_unicos(lista):
    res = []

    for item in lista:
        cant = 0    
        for item2 in lista:
            if item == item2:
                cant += 1

        if not cant > 1:
            res.append(item)


    return res

# print(elementos_unicos([1,2,2,3,4,4,5]))
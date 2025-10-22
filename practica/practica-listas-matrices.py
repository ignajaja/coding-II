def trasponer_matriz(matriz):
    result = []
    
    for _ in matriz[0]:
        result.append([])
            
    for i in range(len(matriz)):
        for j in range(len(matriz[0])):
            result[j].append(matriz[i][j])
            print(result[j])        
    return result

# print(trasponer_matriz([[1,2,3],[4,5,6]]))


def obtener_diagonal(matriz):
    result = []
    
    for i in range(len(matriz)):
        for j in range(len(matriz[0])):
            if i == j:
                result.append(matriz[i][j])
                
    return result

# print(obtener_diagonal([[1,2,3],[4,5,6],[7,8,9]]))


def crear_matriz(n):
    result = []
    
    for i in range(n):
        result.append([])
        for j in range(n):
            result[i].append(0)
            
    return result

# print(crear_matriz(5))


def suma_filas_columnas(matriz):
    result = []
    suma_filas = []
    suma_columnas = []
    
    for fila in matriz:
        suma_filas.append(sum(fila))
        actual = 0
        for colu in fila:
            actual += colu
        suma_columnas.append(actual)
        
    return suma_filas, suma_columnas

# print(suma_filas_columnas([[1,2,3],[4,5,6],[7,8,9]]))


def multiplicar_matrices(matriz1, matriz2):
    result = []

    for index in range(len(matriz2)):
        result.append([])
        for __ in matriz1[0]:
            result[index].append(0)
  
    filas1 = len(matriz1)
    columnas1 = len(matriz1[0])
    filas2 = len(matriz2)
    columnas2 = len(matriz2[0])
    
    for i in range(filas1):
        for j in range(columnas2):
            for k in range(columnas1):
                
                if matriz2[i][k] == matriz1[k][j] == 1:
                    result[i][j] = 1
                        
    return result

# print(multiplicar_matrices([[1,0,0],[0,0,0],[0,0,0]], [[1,0,0],[0,1,0],[1,0,0]]))


def rotar_matriz(matriz):
    
    filas = len(matriz)
    columnas = len(matriz[0])
    
    result = [[0 for _ in range(columnas)] for __ in range(filas)]
    
    
    for i in range(filas):
        for j in range(columnas):
            
            result[columnas - j -1][i] = matriz[i][j]
    
    return result
    
# print(rotar_matriz([[1,2,3],[4,5,6],[7,8,9]]))
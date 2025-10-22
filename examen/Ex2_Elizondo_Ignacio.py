def comprimir_texto(texto):
    resultado = []
    
    texto += '*'
    
    suma = 1
    actual = 0
    for i in range(len(texto)):
        if i == 0:
            continue
        if texto[i] == texto[i-1]:
            suma += 1
        else:
            resultado.append([])
            resultado[actual] = [texto[i-1], suma]
            actual += 1
            suma = 1
            
    return resultado

    
    
def saltos(lista, diferencia):
    resultado = []
    
    lista.append(lista[-1]+diferencia+1)
    
    actual = 0
    lista_actual = []
    
    for i in range(len(lista)):
        if i == 0:
            continue
        
        lista_actual.append(lista[i-1])

        if abs(lista[i] - lista[i-1]) >= diferencia:
            resultado.append([])
            resultado[actual] = lista_actual
            lista_actual = []
            actual += 1
        
        
    return resultado


def islas(matriz):
    resultado = 0
    
    islas_hor = 0
    islas_ver = 0
    
    filas = len(matriz)
    columnas = len(matriz[0])
            
    for i in range(filas):
        for j in range(columnas):
            
            if not j == 0:
                if not j == filas-1:
                    if matriz[i][j] == matriz[i][j-1] == 1 and matriz[i][j+1] == 0:
                        islas_hor += 1
                else:
                    if matriz[i][j] == matriz[i][j-1] == 1:
                        islas_hor += 1
                
            if not i == 0:
                if not i == columnas-1:
                    if matriz[i][j] == matriz[i-1][j] == 1 and matriz[i+1][j] == 0:
                        islas_ver += 1
                else:
                    if matriz[i][j] == matriz[i-1][j] == 1:
                        islas_ver += 1
    return islas_hor + islas_ver
    


def triangular_superior(matriz):
    
    filas = len(matriz)
    
    for i in range(filas):
        if 0 in matriz[i][i:]:
            return False
        continue
            
    return True



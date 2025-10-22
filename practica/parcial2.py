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

# print(saltos([1,2,3,7,8,9,15,16,1,2], 3))
# print(saltos([5,6,7,10,12,13,15], 2))


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
                    
            # if matriz[i][j] == 1 and j > 0:
            
            
                
                
    return islas_hor + islas_ver
    

print(islas([[1,1],[1,0]]))
print(islas([[1,0,0,1],[1,0,1,1],[0,0,0,0],[1,1,0,1]]))
print(islas([[1,1,0,0,0],[1,1,0,0,1],[0,0,0,1,1],[0,1,0,0,0],[1,1,1,0,0]]))
    
# para la numero 4, contar filas y que aumente el unmbral en uno, hasta llegar a la última que va a ser len(matriz)-1



def triangular_superior(matriz):
    
    filas = len(matriz)
    
    for i in range(filas):
        if 0 in matriz[i][i:]:
            return False
        continue
            
            
    return True

# print(triangular_superior([[1,1,6],[0,1,1],[0,0,1]]))
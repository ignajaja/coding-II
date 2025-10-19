#E: lista
#S: lista

res = [[2,4,5,8]]
[1,2,3,2,4,5,5]
secuencia = []
largo_max = 4

def maximas_secuencias(lista):
        lista.append(lista[-1]) # TRUCO: agrego el ultimo elemento al final, otra vez, para que siempre haga corte
        res = [] #lista de secuencias
        secuencia = [] #secuencia actual que iré conformando
        largo_max = 1  #contador de la maxima secuencia encontrada

        for i in range(1, len(lista)): #inicio en 1, para comparar con i-1 el anterior
                secuencia.append(lista[i-1])  # pongo el anterior en la secuencia actual

                if lista[i] <= lista[i-1]:  #si se rompe el orden con el anterior debo ver si la secuencia tiene mayor tamaño de lo que llevo en secuencia máxima
                        if len(secuencia) == largo_max: #si la secuencia es igual al largo que encontré maximo hasta el momento
                                res.append(secuencia)   #se mete la secuencia, porque es igual en tamaño a las maximas encontradas hasta el momento.
                        elif len(secuencia) > largo_max: #si la secuencia actual es mejor que el largo hasta ahorita, se descartan las secuencias en res y empieza solo con la que acaba de encontrar
                                res = [secuencia]   #res solo tiene la nueva mayor
                                largo_max = len(secuencia) #se actualiza largo_max porque se encontró una mejor
                        secuencia = []  #se reinicia secuencia, porque ya se incluyó en res y se inicia una nueva
        if len(res) == 1:  #si solo 1 secuencia hay en res, se retorna solo
                return res[0]
        return res

l1_1 = [1, 2, 2, 3, 4, 2, 5]
l1_2 = [5, 6, 7, 1, 2, 3, 4]
l1_3 = [1, 2, 3, 0, 1, 2, 3, 4, 0, 1, 2, 3, 55]

print ('maximas_secuencias')
print (l1_1, '  >>>  ', maximas_secuencias(l1_1))
print (l1_2, '  >>>  ', maximas_secuencias(l1_2))
print (l1_3, '  >>>  ', maximas_secuencias(l1_3))


#es_magica
#E: matriz
#S: boolean

def es_magica (matriz):
        filas = len(matriz)     #saca cantidad de filas
        columnas = len (matriz[0])  #saca cantidad de columnas
        objetivo = sum(matriz[0])  #determina la suma de la primera fila que debe ser la misma de todas las demás

        #recorre todas las filas buscando una que no sume el objetivo
        for fila in matriz:
                if sum(fila) != objetivo: # con solo una diferente que encuentre, retorna False
                        return False

        #recorre la matriz, formando las columnas, para luego sumar cada una
        for col_i in range (columnas): #recorre las columnas
                columna_actual = []     #cada columna, crea un vector para ir poniendo los valores con el siguiente for
                for fila_j in range(filas): #saca un valor de la columna col_i por cada fila para formar la columna
                        columna_actual.append(matriz[fila_j][col_i])
                if sum(columna_actual) != objetivo:  #al finalizar el for se tiene la columna, para ver si suma distinto
                        return False

        #saca un vector con la diagonal y otro con la antidigonal
        diagonal = []
        anti_diagonal = []
        for i in range (filas):  #como es cuadrada se recorre a filas o columnas, da igual
                diagonal.append(matriz[i][i])
                anti_diagonal.append(matriz[i][filas-1-i])
        # ya con los vectores, se consulta si alguno no suma como el objetivo
        if sum(diagonal) != objetivo or sum(anti_diagonal) != objetivo:
                return False
        #aca llegaría solo si todo sumó igual
        return True



m2_1 = [[8,1,6],[3,5,7],[4,9,2]]
m2_2 = [[8,1,6],[3,5,7],[4,9,-2]]
print()
print('es_magica')
print(m2_1, ' >>> ', es_magica(m2_1))
print(m2_1, ' >>> ', es_magica(m2_2))


#eliminar_con_ceros (matriz)
#E:matriz
#S: matriz
def eliminar_con_ceros (matriz):
        filas = len(matriz)     #saca cantidad de filas
        columnas = len (matriz[0])  #saca cantidad de columnas
        filas_con_ceros = [] # se colocarán los indices de las filas con ceros
        columnas_con_ceros = [] #se colocarán los indices de las cols con ceros

        #recorrido para determina cuáles filas, columnas tienen ceros
        for i in range(filas):  #recorre la matriz para determinar quiénes tienen ceros
                for j in range(columnas):
                        if matriz[i][j] == 0: # si es cero la celda, guarda la fila y columna 
                                filas_con_ceros.append(i)       #en filas mete el i de la fila
                                columnas_con_ceros.append(j)    #en cols mete el j de la columna

        #recorrido para determinar cuales columnas debe incluir o no
        #segun si la fila o columna está en filas_conceros y columnas_con_ceros
        matriz_resultado = []   # para reconstruir la matriz
        for i in range(filas):  #recorre la matriz para determinar nueva matriz
                if i in filas_con_ceros: #si la fila debe eliminarse, no la incluye
                        continue
                nueva_fila = []  #cada iteración de las filas que sí van, crea una nueva lsita para ver cuales columnas debe meter en esa fila
                for j in range(columnas): #es el for normal para las columnas de cada fila
                        if j in columnas_con_ceros: #si la columna está en los ceros, no la mete a nueva fila
                                continue
                        nueva_fila.append(matriz[i][j])
                #al finalizar de crear la nueva fila, la mete en matriz_resultado solo si no es nula
                if nueva_fila != []:
                        matriz_resultado.append(nueva_fila)

        return matriz_resultado



m3_1 = [
    [1,  2,  0,  4,  5],
    [6,  7,  8,  9, 10],
    [11, 0, 13, 14, 15],
    [16, 17, 18, 19, 20],
    [21, 22, 23, 24, 25]
]

m3_2 = [
        [1,2,3,4],
        [5,6,7,8],
        [9,10,11,12]
        ]

m3_3 = [
        [0,2,3,4],
        [5,0,7,0],
        [9,10,11,12],

        ]
print()
print('eliminar_con_ceros (matriz)')
print(m3_1, '   >>>   ', eliminar_con_ceros (m3_1))
print(m3_2, '   >>>   ', eliminar_con_ceros (m3_2))
print(m3_3, '   >>>   ', eliminar_con_ceros (m3_3))





def apariciones(elemento, lista):
        cont = 0
        for elem in lista:
                if elem == elemento:
                        cont += 1
        return cont       

#E:lista
#S: lista
def elementos_unicos(lista):
        res = []
        for elem in lista:
                if apariciones(elem, lista) == 1:
                        res.append(elem)
        return res

l4_1 = [1, 2, 2, 3, 4, 4, 5]
l4_2 = [7, 8, 8, 9, 7, 10, 11, 11, 12]
l4_3 = [5,5,5,6,6,6,7,7]
print()
print('elementos_unicos')
print(l4_1, '  >>>  ', elementos_unicos(l4_1))
print(l4_2, '  >>>  ', elementos_unicos(l4_2))
print(l4_3, '  >>>  ', elementos_unicos(l4_3))







''' 1
Frecuencia de elementos
Dada una lista, cuenta cuántas veces aparece cada elemento y muestra el resultado como una lista de pares [elemento, frecuencia].

Ejemplo:
Entrada: ["a", "b", "a", "c", "b", "a"]
Salida: [["a", 3], ["b", 2], ["c", 1]]
'''

def despejar_lista(lista):
    return list(set(lista))

def frecuencia(lista):
    result = []

    lista_despejada = despejar_lista(lista)
    
    for item in lista_despejada:
        result.append([item, lista.count(item)])
        
    return result

# print(frecuencia(["a", "b", "a", "c", "b", "a"]))

''' 2
Intersección sin sets
Dadas dos listas, crea una nueva lista que contenga los elementos que aparecen en ambas, sin usar conjuntos (set).
Ejemplo:
Lista 1: [1, 2, 3, 4]
Lista 2: [3, 4, 5, 6]
Salida: [3, 4]

'''

def interseccion(lista1, lista2):
    result = []

    for item1 in lista1:
        for item2 in lista2:
            if item1 == item2:
                result.append(item1)

    return result

# print(interseccion([1,2,3,4],[3,4,5,6]))

''' 3
Búsqueda del segundo mayor
Crea un programa que encuentre el segundo número más grande en una lista, sin usar funciones predefinidas como sort() o max().
Ejemplo:
Entrada: [4,6,8,9,4,6,8]
Salida: 8

Ejemplo:
Entrada: [4,9,6,8,9,4,6,8]
Salida: 9
'''

def buscar_segundo(lista):
    big = 0
    sec = 0

    for item in lista:
        if item > big:
            sec = big
            big = item

    return sec

# print(buscar_segundo([8,9,8,7,6,5]))

''' 4
Compactar valores consecutivos
Dada una lista de números, agrupa los elementos consecutivos iguales en sublistas.
Entrada: [1, 1, 2, 3, 3, 3, 2, 2]
Salida: [[1, 1], [2], [3, 3, 3], [2, 2]]
'''

def compactar(lista):
    result = []
    cons = []

    lista.append(lista[-1]+1)

    for i in range(len(lista)-1):
        cons.append(lista[i])

        if not lista[i] == lista[i+1]:
            result.append(cons)
            cons = []
    
    return result

# print(compactar([1,1,2,3,3,3,2,2]))

''' 5
Verificar palíndromo con listas
Pide al usuario una palabra, conviértela en una lista de caracteres y verifica si es un palíndromo (se lee igual al revés).

Ejemplo:
Entrada: "reconocer"
Salida: True
'''

def verificar_palindromos(pal):
    lista = []
    for letra in pal:
        lista.append(letra)

    for i in range(len(lista)//2):
        if not lista[i] == lista[-1]:
            return False
        lista.pop()

    return True

print (verificar_palindromos("reconnocer"))
    

''' 6
Sublistas de longitud fija
Escribe un programa que divida una lista en sublistas de n elementos cada una.
Entradas: [1, 2, 3, 4, 5, 6, 7], n=3
Salida: [[1, 2, 3], [4, 5, 6], [7]]
'''

''' 7
Lista de pares (combinaciones)
Dada una lista, genera todas las combinaciones posibles de pares de elementos (sin repetir ni repetir al revés).

Ejemplo:
Entrada: [1, 2, 3]
Salida: [(1,2), (1,3), (2,3)]

Ejemplo:
Entrada: ['a', 'b', 'c', 'd']
Salida: [('a', 'b'), ('a', 'c'), ('a', 'd'), ('b', 'c'), ('b', 'd'), ('c', 'd')]

Ejemplo:
Entrada: [1, 2, 2, 3]
Salida: [(1, 2), (1, 2), (1, 3), (2, 2), (2, 3), (2, 3)]
'''

''' 8
Matriz identidad: matriz cuadrada de ceros con diagonal de 1s
Escribe un programa que genere una matriz identidad de tamaño n x n usando listas de listas.
n = 3
Salida:
[[1, 0, 0],
 [0, 1, 0],
 [0, 0, 1]]

Ejemplo:
Entrada: n = 5

Salida:
[[1, 0, 0, 0, 0],
 [0, 1, 0, 0, 0],
 [0, 0, 1, 0, 0],
 [0, 0, 0, 1, 0],
 [0, 0, 0, 0, 1]]
'''

''' 9
Encontrar picos: izquierda y derecha del elemento menores
Dada una lista de números, encuentra los picos, es decir, los elementos que son mayores que sus vecinos inmediatos.

Ejemplo:
Entrada: [1, 3, 2, 4, 1, 5, 3]
Salida: [3, 4, 5]
'''

''' 10
Producto de todos menos el actual
Dada una lista de números, crea una nueva lista donde cada elemento es el producto de todos los elementos de la lista original excepto el que está en esa posición (sin usar división).

Ejemplo;
Entrada: [2, 1, 4, 3]
Salida: [12, 24, 6, 8]
Explicación:
Pos 0: 1×4×3 = 12
Pos 1: 2×4×3 = 24
Pos 2: 2×1×3 = 6
Pos 3: 2×1×4 = 8

Ejemplo:
Entrada: [1, 2, 3, 4]
Salida: [24, 12, 8, 6]

Ejemplo:
Entrada: [5, 0, 2]
Salida: [0, 10, 0]

Ejemplo:
Entrada: [3, 3, 3]
Salida: [9, 9, 9]
'''


''' 10
Números que aparecen una sola vez
Dada una lista de enteros, crea una nueva lista que contenga solo los elementos que aparecen una única vez en la lista original.
Ejemplo:
Entrada: [1, 2, 2, 3, 4, 1, 5]
Salida: [3, 4, 5]
'''

'''11
Sumar diagonales de una matriz cuadrada
Dada una matriz cuadrada n x n, escribe un programa que:
-Sume los valores de la diagonal principal y la diagonal secundaria.
-Si el tamaño es impar, que el elemento del centro solo se sume una vez.
Ejemplo:
Entrada:
[[1, 2, 3],
 [4, 5, 6],
 [7, 8, 9]]
Salida:
Diagonal principal: 1 + 5 + 9 = 15  
Diagonal secundaria: 3 + 5 + 7 = 15  
Total: 15 + 15 - 5 = 25
'''

'''12
Transponer una matriz: las filas se convierten en las columnas
Dada una matriz de m x n, genera una nueva matriz transpuesta (n x m), donde las filas se convierten en columnas.
Ejemplo:
Entrada:
[[1, 2, 3],
 [4, 5, 6]]
Salida:
[[1, 4],
 [2, 5],
 [3, 6]]

'''

'''13
Suma por fila y por columna
Dada una matriz n x m, calcula:
- La suma de cada fila
- La suma de cada columna
Retorna una tupla con una lista de la suma de filas y una lista con la suma de columnas
Ejemplo:
Entrada:
[[1, 2, 3],
 [4, 5, 6],
 [7, 8, 9]]
Salida: ( [6, 15, 24],[12, 15, 18])

Ejemplo:
[
 [4, 1, 3, 2],
 [7, 0, 5, 9],
 [6, 2, 8, 4]
]
Salida: ([10, 21, 20] , [17, 3, 16, 15])
'''

'''14
Rotar una matriz 90° a la derecha
Dada una matriz cuadrada, crea una nueva matriz que sea la original rotada 90 grados hacia la derecha.
Entrada:
[[1, 2, 3],
 [4, 5, 6],
 [7, 8, 9]]
Salida:
[[7, 4, 1],
 [8, 5, 2],
 [9, 6, 3]]

 Ejemplo:
Entrada:
[
 [1, 2, 3, 4],
 [5, 6, 7, 8]
]
Salida:
[
 [5, 1],
 [6, 2],
 [7, 3],
 [8, 4]
]

'''


'''15
Patrón de tablero de ajedrez
Crea una matriz n x n donde los elementos se alternen entre 0 y 1 como un tablero de ajedrez, empezando por 0.

Entrada: n = 4
Salida:
[[0, 1, 0, 1],
 [1, 0, 1, 0],
 [0, 1, 0, 1],
 [1, 0, 1, 0]]
'''

'''16
Buscar un elemento en una matriz
Crea una función que busque un número dentro de una matriz n x m y retorne la posición (fila, columna) donde se encuentra, o indique con (-1,-1) que no está.
Ejemplo:
Matriz:
[
 [10, 22, 35],
 [47, 53, 66],
 [72, 85, 90],
 [91, 93, 99]
]
Número a buscar: 85
Salida: (2,1)

Número a buscar: 1000
Salida: (-1,-1)
'''

'''17
Búsqueda de palabras horizontales
Dada una matriz de caracteres y una palabra, verifica si la palabra se encuentra en alguna fila de izquierda a derecha.
Entradas: una matriz de caracteres (string de len 1) y una palabra
[['C', 'A', 'S', 'A'],
 ['P', 'E', 'R', 'O'],
 ['G', 'A', 'T', 'O']]
Palabra: "CASA"
Salida: True
'''

'''18
Bordes de una matriz
Dada una matriz n x n, genera una nueva matriz con solo los valores del borde, y el resto en 0.
Ejemplo:
Entrada:
[[1, 2, 3],
 [4, 5, 6],
 [7, 8, 9]]
Salida:
[[1, 2, 3],
 [4, 0, 6],
 [7, 8, 9]]

Ejemplo:
Entrada:
[
 [11, 12, 13, 14, 15],
 [21, 22, 23, 24, 25],
 [31, 32, 33, 34, 35],
 [41, 42, 43, 44, 45],
 [51, 52, 53, 54, 55]
]

Salida:
[
 [11, 12, 13, 14, 15],
 [21,  0,  0,  0, 25],
 [31,  0,  0,  0, 35],
 [41,  0,  0,  0, 45],
 [51, 52, 53, 54, 55]
]
'''

'''19
Expandir filas
Dada una matriz, genera una nueva matriz donde cada fila se repite k veces.

Entrada:
[[1, 2], [3, 4]], k = 2
Salida:
[[1, 2],
 [1, 2],
 [3, 4],
 [3, 4]]
'''

'''20
Buscar el valor máximo y su posición
Dada una matriz n x m, encuentra el valor más alto y su posición (fila, columna).
Debe retornar una tupla con el (valor, (fila,columna))
Entrada:
[
 [3, 9, 4],
 [1, 12, 6],
 [0, 7, 8]
]
Salida:
( 12, (1, 1) )
'''

"""
I: list
O: a number
Receives a list of numbers and returns the sum.
"""

def suma_lista(lista):
    result = 0

    for element in lista:
        result += element

    return result
    

"""
I: list
O: a tuple with two numbers
Receives a list of numbers and returns a tuple with the largest and smallest number in the list.
"""

def mayor_menor(lista):
    max_num = 0
    min_num = 999999999

    for element in lista:
        if element > max_num:
            max_num = element
        if element < min_num:
            min_num = element

    return (max_num, min_num)

"""
I: list
O: a number
Receives a list of numbers and returns the count of even numbers in the list.
"""

def contar_pares(lista):
    acumulator = 0

    for element in lista:
        if element % 2 == 0:
            acumulator += 1

    return acumulator


"""
I: list
O: list
recibe una lista y devuelve la lista invertida
"""
# Ya existe la función invertir_lista justo debajo de este docstring.

def invertir_lista(lista):
    inverted_list = []
    counter = len(lista) - 1

    for element in lista:
        inverted_list.append(lista[counter])
        counter -= 1

    return inverted_list


"""
I: list
O: a number 
Receives a list of numbers and returns the average.
"""

def promedio(lista):
    return suma_lista(lista) / len(lista)


"""
I: a list and a number
O: boolean
Receives a list and a number and returns True if the number is in the list and False otherwise.
"""

def buscar_elemento(lista, element):
    list_found = []

    for i in range(len(lista)):
        if lista[i] == element:
            list_found.append(i)
    
    return list_found            


"""
I: list
O: a number
Receives a list of numbers and returns the product of all the numbers in the list.
"""

def producto_lista(lista):
    result = 1

    for element in lista:
        result *= element

    return result


"""
I: list
O: list
Receives a list and returns a list without duplicates.
"""
def eliminar_duplicados(lista):
    list_result = []
    for element in lista:
        if not element in list_result:
            list_result.append(element)

    return list_result


"""
I: list and a number
O: list
Receives a list of numbers and a number, and returns a list with the numbers greater than the given number.
"""

def filtrar_mayores(lista, numero):
    list_result = []
    for element in lista:
        if element > numero:
            list_result.append(element)

    return list_result


"""
I: two lists
O: list
Receives two lists of equal length and returns a list containing the concatenation of the elements
from both lists at the same position. If the elements are numbers, they are added; if they are strings, they are concatenated.
"""

def concatenar_listas(lista1, lista2):
    list_result = []

    for i in range(len(lista1)):
        if type(lista1[i]) == int and type(lista2[i]) == int:
            list_result.append(lista1[i] + lista2[i])
        elif type(lista1[i]) == str and type(lista2[i]) == str:
            list_result.append(str(lista1[i]) + str(lista2[i]))

    return list_result


"""
I: list and a value
O: a number
Receives a list and a value and returns the number of times the value appears in the list
"""

def contar_valor(lista, valor):
    counter = 0

    for element in lista:
        if element == valor:
            counter += 1

    return counter


"""
I: list
O: a number
Receives a list of numbers and returns the sum of the odd numbers in the list
"""

def suma_impares(lista):
    result = 0

    for element in lista:
        if not element % 2 == 0 :
            result += element

    return result


"""
I: list
O: list
Receives a list of numbers and returns a list with the squares of the numbers in the original list
"""

def cuadrados(lista):
    list_result = []

    for element in lista:
        list_result.append(element ** 2)

    return list_result


"""
I: list and a number
O: list
Receives a list of numbers and a limit number, and returns a list with the numbers greater than or equal to the limit number
"""

def eliminar_menores(lista, limite):
    list_result = []

    for element in lista:
        if element >= limite:
            list_result.append(element)

    return list_result


"""
I: two lists
O: list
Receives two lists of equal length and returns a list that interleaves the elements from both lists
"""

def intercalar_listas(lista1, lista2):
    list_result = []

    for i in range(len(lista1)):
        list_result.append(lista1[i])
        list_result.append(lista2[i])

    return list_result


"""
I: list
O: a number
Receives a list of numbers and returns the count of numbers greater than the average of the list"""

def mayores_que_promedio(lista):
    average = promedio(lista)
    result = 0

    for element in lista:
        if element > average:
            result += 1

    return result


"""
I: list
O: boolean
Receives a list and returns True if the list is sorted in ascending order, and False otherwise.
"""

def esta_ordenada(lista):
    for i in range(len(lista)):
        if i == 0:
            continue
        elif lista[i] < lista[i - 1]:
            return False
        
    return True


"""
I: list
O: list
Receives a list and returns a list of the elements that appear more than once in the original list.
"""

def valores_unicos(lista):
    list_storage = []
    list_result = []

    for element in lista:
        if element in list_storage and element not in list_result:
            list_result.append(element)
        list_storage.append(element)

    return list_result


"""
I: list
O: list
Receives a list and returns a list without the zeros."""

def eliminar_ceros(lista):
    list_result = []

    for element in lista:
        if not element == 0:
            list_result.append(element)

    return list_result



"""
I: list and a number
O: list
Receives a list and a number, and returns a list with each element of the original list repeated n times.
"""

def repetir_elementos(lista, n):
    list_result = []
    
    for element in lista:
        for i in range(n):
            list_result.append(element)

    return list_result

"""
e: un numero
s: un numero
r: tiene que ser un numero
"""


def sumar_impar(num):
    suma = 0
    while num > 0:
        if not (num % 10) % 2 == 0:
            suma += num % 10
        num = num // 10
    return suma


"""
e: un int
s: un int
r: la entrada debe ser un int
"""


def cuente_par(num):
    cont = 0
    while num > 0:
        if (num % 10) % 2 == 0:
            cont += 1
        num //= 10
    return cont


"""
E: un int
S: valor booleano
R: la entrada debe ser int
"""


def todos_pares(num):
    if num == 0:
        return True
    while num > 0:
        if not (num % 10) % 2 == 0:
            return False
        num //= 10
    return True


"""
E: un numero
S: valor booleano
R: la entrada debe ser un numero
"""


def hay_cero(num):
    if num == 0:
        return True
    while num > 0:
        if num % 10 == 0:
            return True
        num //= 10
    return False


"""
E: un numero
S: valor booleano
R: la entrada debe ser un numero
"""


def es_binario(num):
    if num == 0:
        return True
    while num > 0:
        if not (num % 10 == 0 or num % 10 == 1):
            return False
        num //= 10
    return True


"""
cuenta cuántos 1 hay en un número
E: un numero
S: la cantidad de 1 en el numero, en forma de int
R: la entrada debe ser un numero
"""


def q(n):
    t = 0
    while n != 0:
        if n % 10 == 1:  # le falta el doble ==
            t + 1
            n //= 10
        else:
            n //= 10  # hacer division entera en vez de simplee
    return t  # le falta el retorno de el resultado


"""
E: un numero
S: valor booleano
R: entrada debe ser un numero
"""


def iguales(num):
    largo = 0
    ini = num % 10
    rep = num

    while rep > 0:
        largo += 1
        rep //= 10

    while largo > 1:
        num //= 10
        largo -= 1

    if ini == num:
        return True
    else:
        return False


"""
E: un numero
S: valor booleano
R: entrada debe ser un numero
"""


def estan_ordenados(num):
    last = 0
    while num > 0:
        if not (num % 10 >= last):
            return False
        else:
            last = num % 10
            num //= 10
    return True


"""
E: un numero
S: un numero (una sumatoria)
R: que sea un numero
"""


def sumatoria(n):
    sumatoria = 1
    while n > 0:
        print(sumatoria)
        sumatoria += 1
        n -= 1


"""
E: un numero
S: una serie de numeros
R: que sea un numero
"""


def serie(n):
    rep = 4
    while n > 0:
        if n % 2 == 0:
            print(6)
        else:
            print(rep)
            rep += 5
        n -= 1


serie(9)

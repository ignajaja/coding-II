def componer_numero(num):
    acumulador = 0
    exp = 0
    while num > 0:

        acumulador += (num % 10) * (10**exp)
        print(acumulador, "exp", exp, "que sumó: ", (num % 10) * (10**exp))

        exp += 1
        num //= 10

    return acumulador


def solo_pares(num):
    acumulador = 0
    exp = 0

    while num > 0:

        if num % 2 == 0:
            acumulador += (num % 10) * (10**exp)
            exp += 1

        num //= 10

    return acumulador


def get_largo(n):
    c = 0
    while n > 0:
        c += 1
        n //= 10
    return c


"""
E: num
S: un int del número invertido 
R: tiene que ser un número
"""


def invertir_numero(num):
    exp = get_largo(num) - 1
    acumulador = 0

    while num > 0:
        acumulador += (num % 10) * (10**exp)
        exp -= 1
        num //= 10

    return acumulador


def eliminar_primera(x, num):
    acumulador = 0
    exponente = 0
    condicion = False

    while num > 0:
        if not num % 10 == x or condicion == True:
            acumulador += (num % 10) * (10**exponente)
            exponente += 1
        else:
            condicion = True

        num //= 10
    return acumulador


print(eliminar_primera(2, 123452))

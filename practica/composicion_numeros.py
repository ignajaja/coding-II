def largo(num):
    acumulador = 1
    while num > 9:
        acumulador += 1
        num //= 10
    return acumulador


# 3
def borrar_posicion(n, x):
    acumulador = 0
    exponente = 0
    n *= 10
    while n > 0:
        if not exponente == x:
            acumulador += (n % 10) * (10**exponente)
            exponente += 1
        else:
            acumulador += (n // 10) * (10**exponente)
            return acumulador // 10
        n //= 10


# 4
def divisibles(numero, divisor):
    acumulador = 0
    exponente = 0
    while numero > 0:
        if (numero % 10) % divisor == 0:
            acumulador += (numero % 10) * (10**exponente)
            exponente += 1
        numero //= 10
    return acumulador


# 5
def posiciones_impares(numero):
    exponente = 0
    contador = 0
    acumulador = 0
    while numero > 0:
        if not contador % 2 == 0:
            acumulador += (numero % 10) * (10**exponente)
            exponente += 1
        contador += 1
        numero //= 10
    return acumulador


# 6
def posiciones_impares_desde_izquierda(numero):
    largo_numero = largo(numero) - 1
    contador = 0
    acumulador = 0
    while numero > 0:
        if contador % 2 == 0:
            acumulador = (acumulador * 10) + numero // (10**largo_numero)
        largo_numero -= 1
        contador += 1
        numero = numero % (10**largo_numero)

    return acumulador


print(posiciones_impares_desde_izquierda(98765))

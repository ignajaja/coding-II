# Realiza un programa en Python,
# nota, cuando se le pide rangos, considérelos cerrados
# cunado se les pide muestre, se refiere a PRINT


# 1 que muestre los primeros 100 números enteros iniciando desde el 1.
def mostrar_primeros_100():
    num = 1
    while num <= 100:
        print(num)
        num += 1
    return


# 2 que muestre los primeros 100 números de forma inversa, es decir, del 100 al 1


def mostrar_primeros_100_inversa():
    num = 100
    while num >= 1:
        print(num)
        num -= 1
    return


# 3 que muestre únicamente, los números pares en el rango del 1 al 100


def mostrar_primeros_100_pares():
    num = 1
    while num <= 100:
        if num % 2 == 0:
            print(num)
        num += 1
    return


# 4 que muestre la suma de los números del 1 al 100


def sumar_primeros_100():
    num = 1
    resul = 0
    while num <= 100:
        resul += num
        num += 1
    return print(resul)


# 5 que muestre la suma de los números impares del 1 al 100


def sumar_impares_al_100():
    num = 1
    resul = 0
    while num <= 100:
        if not num % 2 == 0:
            resul += num
        num += 1
    return print(resul)


# 6 dados dos números, inicio y final, retorne la suma entre ese rango,
#  incluyendo inicio y final como rango cerrado.


def sumar_rango(ini, fin):
    resul = 0
    while ini <= fin:
        resul += ini
        ini += 1
    return resul


# 7 dados dos números, inicio y final, retorne la cantidad de números pares
#  en ese rango cerrado.


def contar_numeros_pares_rango(ini, fin):
    resul = 0
    while ini <= fin:
        if ini % 2 == 0:
            resul += 1
        ini += 1
    return resul


# 8 dados dos números, inicio y final, retorne la cantidad de números
#  negativos entre ese rango


def contar_negativos_rango(ini, fin):
    resul = 0
    while ini <= fin:
        if ini < 0:
            resul += 1
        ini += 1
    return resul


# 9 Escribir un programa que pida al usuario un número entero y
#  muestre por pantalla un triángulo rectángulo como el de más abajo,
#  de altura el número introducido.
#      *
#      **
#      ***
#      ****
# este ejemplo usa el número 4


def construir_triangulo():
    num = input("Ingrese un número: ")

    if not num.isnumeric():
        print("Debe ingresar un número")
        return construir_triangulo()

    num = float(num)
    triangulo = "\n"
    contador = 1

    while contador <= num:
        triangulo += "*" * contador + "\n"

        contador += 1
    return print(triangulo)


# 10 Escribir un programa que pida al usuario un número entero y muestre
# por pantalla un triángulo rectángulo como el de más abajo.
# 1
# 3 1
# 5 3 1
# 7 5 3 1
# 9 7 5 3 1


def construir_triangulo_numeros():
    num = input("Ingrese un número: ")

    if not num.isnumeric():
        print("Debe ingresar un número")
        return construir_triangulo()

    num = float(num)
    triangulo = "\n"
    contador = 1
    num_triangulo = 1
    num_display = 1

    while contador <= num:
        num_display = num_triangulo
        while num_display > 0:
            triangulo += f"{num_display} "
            num_display -= 2

        triangulo += "\n"
        contador += 1
        num_triangulo += 2

    return print(triangulo)


# 11 Escribir un programa que pida al usuario un número entero y retorne
#  si es un número primo o no.


def es_primo():
    num = input("Ingrese un número: ")

    if not num.isnumeric():
        print("Debe ingresar un número")
        return es_primo()

    num = int(num)
    divisor = 2

    if num <= 1:
        return print("No es un número primo")

    while divisor <= (num // 2):
        print((num // divisor), (num / divisor))
        if num // divisor == num / divisor:
            return print("No es un número primo")
        divisor += 1
    return print("Sí es un número primo")


# 12 sumatoria hasta: dado un numero natural, retorne la suma de los
# primeros números naturales hasta el número dado inclusive.
# sumatoria (5) > 15 que es 1+2+3+4+5


def mostrar_sumatoria(num):
    suma = 0
    contador = 0
    while contador <= num:
        suma += contador
        contador += 1
    return suma


# 13 sumatoria hasta n, n es un número natural dado. La suma será de
#      ___1___ + ___1___ + ___1___ + . . . + ___1___
#      1*(1+1)  2* (2+1)  3*(3+1)          n (n+2) aqui hay un error, debe ser (n+1)


def mostrar_sumatoria2(num):
    suma = 0
    contador = 1
    while contador <= num:
        suma += 1 / (contador * (contador + 1))
        contador += 1
    return suma


# 14 sumatoria hasta n, n es un natural dado, la suma de
#      ___1___ - ___1___ + ___1___ - . . . + ___1___
#      1*(1+1)  2* (2+1)  3*(3+1)          n (n+1)


def mostrar_sumatoria3(num):
    suma = 0
    contador = 1
    while contador <= num:
        if contador % 2 == 0:
            suma -= 1 / (contador * (contador + 1))
        else:
            suma += 1 / (contador * (contador + 1))
        contador += 1
    return suma


# RETO opcional
# 15 Haga un programa que dado un número entero positivo,
# retorna la sumatoria de los dígitos de ese número
# ejemplo: sumarDigitos(14501) > 11 el resultado de 1+4+5+0+1


def sumar_digitos(num):
    resul = 0

    if num == 0:
        return 1

    while num > 0:
        resul += num % 10
        num //= 10
    return resul


mostrar_primeros_100()
mostrar_primeros_100_inversa()
mostrar_primeros_100_pares()
sumar_primeros_100()
sumar_impares_al_100()
sumar_rango(10, 20)
contar_numeros_pares_rango(10, 20)
contar_negativos_rango(-10, 10)
construir_triangulo()
construir_triangulo_numeros()
es_primo()
print(mostrar_sumatoria2(10))
print(mostrar_sumatoria3(10))
print(sumar_digitos(14501))

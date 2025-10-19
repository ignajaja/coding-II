from math import *

# reto 1
# E: 3 numeros
# S: 1 numero
# R:


def sumar_tres(n1, n2, n3):
    return n1 + (n2 * n3)


# reto 2
# E: 3 numeros
# S: 1 numero
# R:


def promediar_tres(n1, n2, n3):
    return (n1 + n2 + n3) / 3


# reto 3
# E: 1 numero
# S: 1 numero
# R:


def calcular_formula(num):
    return (num**3 + num**2) / 2


# reto 4
# E: 2 numeros
# S: 1 numero
# R:


def calcular_distancia(velocidad, tiempo):
    return velocidad * tiempo


# reto 5
# E: 3 numeros
# S: 1 numero
# R:


def calcular_monto_final(capital, interes, annos):
    return capital * (1 + interes) ** annos


# reto 6
# E: 1 numero
# S: 1 numero
# R:


def convertir_kelvin_farenheit(celcius):
    kelvin = celcius + 273.15
    faren = celcius * (9 / 5) + 32
    return (kelvin, faren)


# reto 7
# E: 4 numeros (dos cordenadas por dos puntos)
# S: 1 numero
# R:


def obtener_distancia_puntos(x1, y1, x2, y2):
    return sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)


# reto 8
# E: 1 numero
# S: 1 numero
# R:


def obtener_decimal(num):
    return num - floor(num)


# reto 9
# E: 1 numero
# S: 1 numero
# R:


def sumar_cifras(num):
    return len(str(num))


# reto 10
# E: 1 numero
# S: 1 numero
# R:


def obtener_volumen(num):
    return (4 / 3) * pi * num**3


# reto 11
# E: 1 numero y una palabra
# S: un string
# R:


def repetir_palabra(num, pal):
    return pal * num


# reto 12
# E: 1 numero y 1 palabra
# S: un string
# R:


def reemplazar_vocales(texto):
    texto = texto.replace("a", "*")
    texto = texto.replace("e", "*")
    texto = texto.replace("i", "*")
    texto = texto.replace("o", "*")
    texto = texto.replace("u", "*")
    return texto


# reto 13
# E: un texto
# S: un string
# R: palabras de más de 5 caracteres


def mostrar_primeros_cinco(texto):
    return texto[0:5]


# reto 14
# E: un texto
# S: un string
# R:


def capitalizar_primera(palabra):
    return palabra.capitalize()


# reto 15
# E: un texto
# S: un string
# R: un texto con mas de 30 caracteres


def centrar_30(texto):
    # n = int((len(texto)) / 2)
    # return texto[n - 15 : n + 15]
    n = 15 - int((len(texto)) / 2)
    palabra = " " * n + texto + " " * n + " "
    return palabra[:30]


# reto 16
# E: un texto
# S: un string
# R:


def mezclar_mitades(p1, p2):
    n1 = (len(p1)) // 2
    n2 = (len(p2)) // 2
    return p1[:n1] + p2[n2:]


# reto 17
# E: 2 palabras
# S: un string
# R:


def sin_espacios(palabra):
    return palabra.replace(" ", "")


# reto 18
# E: 1 palabra
# S: un string
# R:


def ultimas_3(texto):
    return texto[-3:]


# reto 19
# E: 1 palabra
# S: un string
# R: un texto con mas de 50 caracteres


def rodear_con_asteriscos(texto):
    n = int((50 - len(texto)) / 2)
    return "*" * n + texto + "*" * n


# reto 20
# E: 1 palabra
# S: un string
# R:


def inicia_con(texto, inicio):
    texto_l = texto.lower()
    inicio_l = inicio.lower()
    resultado = texto_l.startswith(inicio_l)
    return resultado

"""
Ejercicio 1
E: salario (int)
S: la clasificación del empleado por medio de un string
R: numero negativo, un string, un
"""

def clasificar_empleado(salario):
    if salario >= 2500:
        if salario > 5000:
            return "Gerente de alto nivel"
        else:
            return "Supervisor"
    elif salario >= 1000:
        return "Empleado intermedio"
    else:
        return "Empleado de nivel básico"

print(clasificar_empleado(800))
print(clasificar_empleado(1500))
print(clasificar_empleado(3000))
print(clasificar_empleado(6000))


"""
Ejercicio 2
E: num (int)
S: la clasificación del numero por medio de un string
R: tipos de datos que no sean numericos
"""

def clasificar_numero(num):
    if num > 0:
        if num % 2 == 0:
            return "El número es positivo y par"
        else:
            return "El número es positivo e impar"
    elif num < 0:
        if num < -10:
            return "El número es negativo y su valor absoluto es mayor a 10"
        else:
            return "El número es negativo y su valor absoluto es menor o igual a 10"
    else:
        return "El número es cero"

print(clasificar_numero(8))
print(clasificar_numero(7))
print(clasificar_numero(-5))
print(clasificar_numero(-15))
print(clasificar_numero(0))
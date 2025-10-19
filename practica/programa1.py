# utilizar PEP8: numero_uno_dos_tres_cuatro


# ejercicio 1
def multiplicar_nombre(nombre, repetir):
    return nombre * repetir


def multiplicar_nombre_prints():
    nombre = input("Ingrese su nombre: ")
    repetir = int(input("Cuántas veces lo va a repetir?: "))
    resultado = multiplicar_nombre(nombre, repetir)
    print(resultado)


# ejercicio 2
def imprimir_tarjeta(nombre, carrera, universidad):
    nombre = input("Ingrese su nombre: ")
    carrea = input("Ingrese su carrera: ")
    universidad = input("Ingrese su universidad: ")

    print("Tarjeta de presentación:")
    print("-----------------------")
    print("| Nombre: ", nombre)
    print("| Carrera: ", carrea)
    print("| Universidad: ", universidad)
    print("-----------------------")


# ejercicio 3
def calcular_propina(monto, porcentaje):
    """
    calcula el porcentaje que hay que agregarse a la cuenta
    E: monto de la cuenta, porcentaje de la propina
    S: monto de la propina
    R: n/a
    """
    propina = monto * (porcentaje * 0.01)
    return propina


def calcular_propina_ES():
    monto = float(input("Ingrese el costo: "))
    porcentaje = float(input("Ingrese el porcentaje de la propina: "))
    propina = calcular_propina(monto, porcentaje)
    print("La propina es de", propina, ", y el total de ", monto + propina)

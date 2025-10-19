# E: num. un numero
# S: los valores que el usuario requiere
# R:


def sacar_dinero_cajero(num):

    n20 = num // 20000
    num = num - 20000 * n20
    n10 = num // 10000
    num = num - 10000 * n10
    n5 = num // 5000
    num = num - 5000 * n5
    n2 = num // 2000
    num = num - 2000 * n2

    return (  # nota: estas lineas no fueron escritas así, fueron corregidas por la extención "Prettier" de VS code. una disculpa si parece sospechozo
        "20000: "
        + str(n20)
        + ". 10000: "
        + str(n10)
        + ". 5000: "
        + str(n5)
        + ". 2000:"
        + str(n2)
        + ". No entregado: "
        + str(num)
    )


print(sacar_dinero_cajero(75000))

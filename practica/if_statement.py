def f1(x, y):
    if x < 0:
        return x + y / 2
    elif x == 0:
        return y
    else:
        return x / y


def f1_1(x, y):
    if x < 0:
        return x + y / 2
    if x == 0:
        return y
    return x / y


def es_mayor_de_edad(x):
    if x >= 18:
        return True
    return False


def is_able_rollercoaster(age, height):
    if age > 18:
        if height >= 160 and height < 220:
            return True
    return False


def clissify_number(num):
    if num > 0:
        return "Positivo"
    elif num == 0:
        return "Cero"
    else:
        return "Negativo"


def es_par_digitos(num):
    n1 = num % 10
    num = num // 10
    n2 = num % 10
    num = num // 10
    n3 = num % 10

    if (n1 + n2 + n3) % 2 == 0:
        return True
    return False


print(es_par_digitos(747))


def es_par_digitos_v2(num):
    n1 = num % 10
    n2 = num // 10 % 10
    n3 = num // 100 % 10

    if (n1 + n2 + n3) % 2 == 0:
        return True
    return False


print(es_par_digitos_v2(458))

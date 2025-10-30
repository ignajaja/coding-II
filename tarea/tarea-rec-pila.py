def es_binario(num):
    if num == 0:
        return True
    if not (num%10 == 1 or num%10 == 0):
        return False
    return es_binario(num//10)

print(es_binario(101002))
print(es_binario(111001110))

"""
es_binario(1010)
    1010%10 == 0
    es_binario(101)
        101%10 == 1
        es_binario(10)
            10%10 == 0
            es_binario(1)
                1%10 == 1
                    es_binario(0)
                        0 == 0
                        True
"""


def en_posiciones_pares(num, i = 1):
    if num == 0:
        return True
    if i % 2 == 0:
        if not (num%10) % 2 == 0:
            return False
    return en_posiciones_pares(num//10, i + 1)

print(en_posiciones_pares(94322))
print(en_posiciones_pares(23296689))

"""
en_posiciones_pares(12345, 1)
    i=1, num=12345
    en_posiciones_pares(1234, 2)
        i=2, num=1234,
        num//10 = 4
        en_posiciones_pares(123, 3)
            i=3, num=123
            en_posiciones_pares(12, 4)
                i=4, num=12, 
                num//10=2
                en_posiciones_pares(1, 5)
                    i=5, num=1
                    en_posiciones_pares(0, 6)
                        num=0
                        True
"""

def cantidad_divisible(num, car):
    if num == 0:
        return 0
    if (num%10)%car == 0:
        return 1 + cantidad_divisible(num//10, car)
    return cantidad_divisible(num//10, car)

print(cantidad_divisible(66,6))
print(cantidad_divisible(84265,2))

"""
cantidad_divisible(12345, 2)
    num=12345, num//10=5
    0 + cantidad_divisible(1234, 2)
        num=1234, num//10=4 +1
        1 + cantidad_divisible(123, 2)
            num=123, num//10=3
            0 + cantidad_divisible(12, 2)
                num=12, num//10=2
                1 + cantidad_divisible(1, 2)
                    num=1, num//10=1 
                    0 + cantidad_divisible(0, 2)
                        num=0
                        0
                    0 + 0
                0 + 1
            1 + 0
        1 + 1
    2 + 0
2
"""
    
def eliminar(car, num):
    if num == 0:
        return 0
    if num%10 == car:
        return eliminar(car, num//10)
    return eliminar(car, num//10)*10 + (num%10)

print(eliminar(0,1280138104))
print(eliminar(1,231412831))

"""
eliminar(5, 12535)
    num=12535, num//10=5
    0 + eliminar(5, 1253)
        num=1253, num//10=3 
        3 + eliminar(5, 125)
            num=125, num//10=5
            0 + eliminar(5, 12)
                num=12, num//10=2
                20 + eliminar(5, 1)
                    num=1, num//10=1
                    100 + eliminar(5, 0)
                        num=0
                        0
                    0 + 100
                100 + 20
            120 + 0
        120 + 3
    123 + 0
123
"""
    
def mayor_de_dos(n1, n2):
    if n1 > n2:
        return n1
    return n2

def contar_digitos(num):
    if num == 0:
        return 0
    return 1 + contar_digitos(num//10)

def maximo_digito(num):
    if contar_digitos(num) == 1:
        return num%10
    return mayor_de_dos(num%10, maximo_digito(num//10))

print(maximo_digito(823546))
print(maximo_digito(7539))

"""
maximo_digito(12345)
    num=12345, último dígito=5
    mayor_de_dos(5, maximo_digito(1234))
        num=1234, último dígito=4
        mayor_de_dos(4, maximo_digito(123))
            num=123, último dígito=3
            mayor_de_dos(3, maximo_digito(12))
                num=12, último dígito=2
                mayor_de_dos(2, maximo_digito(1))
                    num=1
                    1
                mayor_de_dos(2, 1) = 2
            mayor_de_dos(3, 2) = 3
        mayor_de_dos(4, 3) = 4
    mayor_de_dos(5, 4) = 5
"""

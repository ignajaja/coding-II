def largo(n):
    res = 0
    n = abs(n)
    while n > 9:
        res += 1
        n //= 10
    return res + 1

def amigos(num1, num2):
    num1 = abs(num1)
    num2 = abs(num2)
    acumulador1 = 0
    acumulador2 = 0

    contador = 1

    while contador <= num1 //2: #while para el primero número
        if num1 / contador == num1 // contador:
            acumulador1 += contador
        contador += 1

    contador = 1

    while contador <= num2 //2:
        if num2 / contador == num2 // contador:
            acumulador2 += contador
        contador += 1

    if acumulador1 == num2 and acumulador2 == num1:
        return True
    return False

print(amigos(220, 284))
print(amigos(6, 6))


def resta(num1, num2):
    num1 = abs(num1)
    num2 = abs(num2)
    if num1 == 0 or num2 == 0:
        return False
    
    acumulador = 0
    potencia = 0

    while num1 > 0:
        n2 = num2
        flag = False

        while n2 > 0:
            if num1%10 == n2%10:
                flag = True

            n2 //=10

        if flag == False:            
            acumulador += (num1%10) * (10**potencia)
            potencia += 1

        num1 //= 10

    if acumulador == 0:
        return -1
    
    return acumulador

print(resta(241, 42542))
print(resta(123, 2319) )
print(resta(4544511, 409))
print(resta(40544511, 419))


def menor(num):
    if num == 0:
        return 0
    num = abs(num)
    menor = 9
    while num > 0:
        if num%10<menor:
            menor = num%10
        num//=10
    return menor

print(menor(9450441))
print(menor(4444))
print(menor(-3245))


def suma_espejo(num):
    num = abs(num)

    largo_num = largo(num)
    potencia = largo_num//2

    if largo == 1:
        return False

    if largo_num%2==0:
        mitad1 = num//(10**potencia)
        mitad2 = num%(10**potencia)
    else:
        mitad1 = num//(10**(potencia+1))
        mitad2 = num%(10**(potencia-1))

    acumulador1 = 0
    acumulador2 = 0
    while mitad1 > 0:
        acumulador1 += mitad1%10
        mitad1 //= 10
    while mitad2 > 0:
        acumulador2 += mitad2%10
        mitad2 //= 10

    if acumulador1 == acumulador2:
        return True
    return False

print(suma_espejo(14642256))
print(suma_espejo(249650993))
print(suma_espejo(14742256))
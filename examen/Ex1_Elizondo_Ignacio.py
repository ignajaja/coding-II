def largo(num):
    res = 0
    num = abs(num)
    while num > 9:
        res += 1
        num //= 10
    return res + 1

def invertir_distintos(num):
    if num == 0:
        return 0
    
    acumulador = 0
    potencia = 0
    res = 0

    while num > 0:
        copia_num = num
        num = 0
        pot_copia = 0

        while copia_num > 0:
            if not copia_num%10 == num%10:
                num += (copia_num%10)*(10**pot_copia)
                pot_copia += 1

            copia_num //= 10

        acumulador += (num%10)*(10**potencia)
        potencia += 1

        num //= 10

    potencia = largo(acumulador)-1

    while acumulador > 0:
        res += (acumulador%10)*(10**potencia)
        potencia -= 1
        acumulador //= 10

    return res




def digitos_comunes_mayores(num1, num2, limite):
    acumulador = 0
    potencia = 0
    flag_cambio_acumulador = False

    while num1 > 0:
        copia2 = num2

        if num1%10 >= limite:
            while copia2 > 0:
                if num1%10 == copia2%10:
                    acumulador += (num1%10)*(10**potencia)
                    potencia += 1
                    flag_cambio_acumulador = True
                    break

                copia2 //= 10

        num1 //= 10

    if flag_cambio_acumulador == False:
        return -1
    
    return acumulador




def digitos_opuestos(num):
    largo_num = largo(num) 
    potencia = 0
    dos_digitos = False

    acumulador = 0

    while num > 0:

        if dos_digitos == True:
            acumulador *= 100
        else:
            acumulador *= 10
        dos_digitos = False


        acumulador += (num%10) + num//(10**(largo_num-1))
        if (num%10) + num//(10**(largo_num-1)) > 9:
            dos_digitos = True

        largo_num -= 2
        num %= 10**(largo_num+1)
        num //= 10

    return acumulador



def alternar_sumas(num1, num2):
    dig1 = 0
    dig2 = largo(num2)-1

    acumulador = 0
    dos_digitos = False

    while num1 > 0:

        if dos_digitos == True:
            acumulador *= 100
        else:
            acumulador *= 10
            dos_digitos = False

        acumulador += num1%10 + num2//(10**dig2)
        print(num1%10 + num2//(10**dig2) > 9, num1%10 + num2//(10**dig2))
        if num1%10 + num2//(10**dig2) == 10:
            dos_digitos = True

        dig1 += 1
        dig2 -= 1

        num2 %= 10**(dig2+1)
        num1 //= 10

    if largo(num1) < largo(num2):
        acumulador = acumulador*(10**(dig2+1)) + num2

    return acumulador

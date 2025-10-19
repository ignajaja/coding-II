def sumar_pares(num):
    resultado = 0
    contador = 0

    while contador <= num:
        if contador % 2 == 0:
            resultado += contador

        contador += 1

    return resultado



def sumar_rango(n1, n2):
    resultado = 0

    while n1 <= n2:
        resultado += n1
        n1 += 1
    
    return resultado

# print(sumar_rango(30, 33))



def sumar_par_impar(n1, n2, clase):
    resultado = 0
    contador = 0

    if clase == "pares":
        while n1 <= n2:
            if n1 % 2 == 0:    
                resultado += n1

            n1 += 1
            
    if clase == "impares":
        while n1 <= n2:
            if not n1 % 2 == 0:
                resultado += n1

            n1 += 1
    return resultado


print(sumar_par_impar(3, 10, "impares"))

def recorrer_numero(num):
    while num >0:
        print(num)
        num //= 10

def contar_digitos(num):
    contador = 0
    if num == 0:
        return 1
    while num > 0:
        contador += 1
        num //= 10

# commons 
def contar_digitos(num):
    res = 0
    while not num == 0:
        num //=10
        res += 1
    return res

def promedio_lista(lis):
    res = 0

    for elem in lis:
        res += elem

    return res // len(lis)


# funciones
def contar_ocurrencias(num, car):
    if num == 0:
        return 0
    if num%10 == car:
        return 1 + contar_ocurrencias(num//10, car)
    return contar_ocurrencias(num//10,car)

def divisible(num, con):
    if con == 1:
        return False
    elif num % con == 0:
        return True
    else:
        return divisible(num, con - 1)

def es_primo(num):
    if num < 2:
        return False
    elif num == 2:
        return True
    else:
        return not divisible(num, num - 1)
    
def contar_ceros(num):
    if num == 0:
        return 0
    if num%10 == 0:
        return 1 + contar_ceros(num//10)
    return contar_ceros(num//10)

def verificar_pares(num):
    if num == 0:
        return True
    if not (num%10) % 2 == 0:
        return False
    return verificar_pares(num//10)

def suma_alterna(num):
    if num == 0:
        return 0
    
    signo = -1 if contar_digitos(num)%2 ==0 else 1
    
    return (num%10)*signo + suma_alterna(num//10)
    
def eliminar_pares(num, exp = 0):
    if num == 0:
        return 0
       
    if (num%10)%2 == 0:
        return eliminar_pares(num//10, exp)
    return (num%10)*(10**exp) + eliminar_pares(num//10, exp + 1)

def sin_repetidos(lis):
    if lis == []:
        return lis
    
    if lis[0] in lis[1:]:
        return sin_repetidos(lis[1:])
    return [lis[0]] + sin_repetidos(lis[1:])

def suma_pos_pares(lis):
    if lis == []:
        return 0
    
    if not len(lis)%2 == 0:
        return lis[0] + suma_pos_pares(lis[1:])
    return suma_pos_pares(lis[1:])

def suma_rango(lis, ran_i, ran_f):
    if lis == []:
        return 0
    
    if ran_f < 0:
        return suma_rango([], 0, 0)
    if ran_i <= 0:
        return lis[0] + suma_rango(lis[1:], ran_i-1, ran_f-1)
    return suma_rango(lis[1:], ran_i-1, ran_f-1)

def mayores_promedio(lis, prom = 0):
    if lis == []:
        return 0
    
    if prom == 0:
        prom = promedio_lista(lis)
    if lis[0] > prom:
        return lis[0] + mayores_promedio(lis[1:], prom)
    return mayores_promedio(lis[1:], prom)
    

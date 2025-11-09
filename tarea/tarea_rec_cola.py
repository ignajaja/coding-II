# commons 
def contar_digitos(num):
    res = 0
    while not num == 0:
        num //=10
        res += 1
    return res

    return res

def promedio_lista(lis):
    res = 0

    for elem in lis:
        res += elem

    return res // len(lis)


# funciones
def contar_ocurrencias(n, d, r = 0):
    if n == 0:
        return r
    
    if n%10 == d:
        return contar_ocurrencias(n//10, d, r+1)
    return contar_ocurrencias(n//10, d, r)

def es_primo(num, d=2):
    if d == num:
        return True
    if num % d == 0:
        return False
    return es_primo(num, d+1)

def contar_ceros(num, r = 0):
    if num == 0:
        return r
    
    if num%10 == 0:
        return contar_ceros(num//10, r+1)
    return contar_ceros(num//10, r)

def todos_pares(num, r = True):
    if num == 0 or r == False:
        return r
    
    if (num%10)%2 == 0:
        return todos_pares(num//10, r) 
    return todos_pares(num//10, False)
    
def suma_alternada(num, r = 0):
    if num == 0:
        return r
    
    signo = -1 if contar_digitos(num)%2 ==0 else 1
    
    return suma_alternada(num//10, r + (num%10)*signo)

def elimina_pares(num, exp = 0, r = 0):
    if num == 0:
        return r
    
    if not (num%10)%2 == 0:
        return elimina_pares(num//10, exp+1, r+((num%10)*(10**exp)))
    return elimina_pares(num//10, exp, r)

def sin_repetidos(lis, r = []):
    if lis == []:
        return r
    
    if lis[0] in lis[1:]:
        return sin_repetidos(lis[1:], r)
    return sin_repetidos(lis[1:], r + [lis[0]])

def suma_por_pares(lis, r = 0, pos_par = True):
    if lis == []:
        return r
    
    if pos_par:
        return suma_por_pares(lis[1:], r + lis[0], False)
    return suma_por_pares(lis[1:], r, True)

def suma_rango(lis, ran_i, ran_f, r = 0):
    if lis == [] or ran_f < 0:
        return r
    
    if ran_i <= 0:
        return suma_rango(lis[1:], ran_i -1, ran_f -1, r + lis[0])
    return suma_rango(lis[1:], ran_i-1, ran_f-1, r)

def mayores_promedio(lis, prom = 0, r = 0):
    if lis == []:
        return r
    
    if prom == 0:
        prom = promedio_lista(lis)

    if lis[0] > prom:
        return mayores_promedio(lis[1:], prom, r + lis[0])
    return mayores_promedio(lis[1:], prom, r)

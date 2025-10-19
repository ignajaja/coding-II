def show_menu():
    print(
        "Menú de opciónes\n" \
        "1. Potencia positiva de 10 más cercana.\n" \
        "2. Contar decimales. \n" \
        "3. Contar dígitos. \n" \
        "4. Es palindromo. \n" \
        "5. Division truncada(sumas y restas). \n" \
        "6. Ocurre en. \n" \
        "7. Ocurre en (izq a der). \n" \
        "8. Mayor dígito. \n" \
        "9. Ocurre más. \n" \
        "10. Agregar dígito. \n" \
        "11. Obtener residuo. \n" \
        "12. Suprimir dígito. \n" \
        "13. Es primo palíndromo. \n" \
        "14. Cuadrado perfecto menor. \n" \
        "15. Calcular expresión 1. \n" \
        "16. Calcular expresión 2\n" \
        "17. Contar días de nacimiento. \n" \
        "18. Suma pares. \n" \
        "19. Nació en bisiesto. \n" \
        "20. Cuántos cuadrados perfectos. \n" \
        "21. Primo próximo. \n" \
        "22. Cuántos palíndromos. \n" \
        "23. Cuántos cuadrados perfectos. \n" \
        "24. Truncar valor. \n" \
        "25. Cuántos números fibonacci son menores. \n" \
        "26. Números fibonacci pares\n" \
        "27. Redondear. \n" \
        "28. Primos entre dos números. \n" \
        "29. Cuantos cuadrados hay que sumar. \n" \
        "30. Cuantos primos hay que sumar. \n" \
        "31. Salir. \n"
    )


def get_largo(n):
    c = 0
    while n > 0:
        c += 1
        n //= 10
    return c


def invert_number(n):
    r = 0
    l = get_largo(n) - 1
    while n > 0:
        r += (n % 10) * (10**l)
        l -= 1
        n //= 10
    return r


def is_prime(n):
    c = 2
    while c < (n // 2):
        if n // c == n / c:
            return False
        c += 1

    return True


# funcion para saber si es float
# sacado de https://stackoverflow.com/questions/354038/how-do-i-check-if-a-string-represents-a-number-float-or-int
def is_float(n): 
    try:
        float(n)
        return True
    except ValueError:
        return False


# 1
def menu_potencia_mas_cercana():
    n = input(
        "Ingrese el número del que quiere averiguar su potencia de 10 más cercana: "
    )

    if not n.isnumeric():
        print("Ingrese un número válido")
        return menu_potencia_mas_cercana()
    n = float(n)

    return potencia_mas_cercana(n)


def potencia_mas_cercana(n):
    if (10 ** get_largo(n) - n) < (n - 10 ** (get_largo(n) - 1)):
        return 10 ** get_largo(n)
    return 10 ** (get_largo(n) - 1)


# 2
def menu_cantidad_decimales():
    n = input("Ingrese el número del cual quiera saber la cantidad de dígitos: ")

    if not n.isnumeric():
        print("Ingrese un número válido")
        return menu_cantidad_decimales()
    n = float(n)
    return cantidad_decimales(n)


def cantidad_decimales(n):
    return get_largo(n)


# 3
def menu_digitos_diferentes():
    n = input("Ingrese el número del cual quiera saber los diferentes dígitos: ")

    if not n.isnumeric():
        print("Ingrese un número válido")
        return menu_digitos_diferentes()
    n = float(n)
    return digitos_diferentes(n)


def digitos_diferentes(n):
    result = 0
    power = 0
    counter = 0

    if n == 0:
        return 1


    while n > 0:
        number = n
        n = 0
        power = 0

        while number > 0:
            
            if not number % 10 == n%10:
                n += (number % 10) * (10**power)
                power += 1
            number //= 10

        n//=10
        result += 1

    return result 


# 4
def menu_es_palindromo():
    n = input("Ingrese el número que quiere saber si es palíndromo: ")

    if not n.isnumeric():
        print("Ingrese un dato válido")
        return menu_es_palindromo()
    n = float(n)
    return es_palindromo(n)


def es_palindromo(n):

    largo = get_largo(n)

    if largo % 2 == 0:
        n1 = n % 10 ** (largo // 2)
        n2 = n // 10 ** (largo // 2)
    else:
        n1 = n % 10 ** ((largo - 1) // 2)
        n2 = n // 10 ** ((largo + 1) // 2)

    if (n1 - n2) % 9 == 0 or (n2 - n1) % 9 == 0:
        return True
    return False


# 5
def menu_division_truncada():
    n1 = input("Ingrese el número que será dividido: ")
    if not n1.isnumeric():
        print("Ingrese datos válidos para el primer número")
        return division_truncada()
    n2 = input("Ingrese el número divisor: ")
    if not n2.isnumeric():
        print("Ingrese un dato válido para el divisor")
    n1 = float(n1)
    n2 = float(n2)

    if n2 == 0:
        print("No se puede dividir entre 0")
        return menu_division_truncada()

    return division_truncada(n1, n2)


def division_truncada(n1, n2):

    cont = 0

    if n1 / n2 == n1 // n2:
        cont += 1

    while n1 > n2:
        n1 -= n2
        cont += 1

    return cont


# 6
def menu_ocurre_en():
    num = input("Ingrese el número entero: ")
    dig = input("Ingrese el dígito que quiera buscar: ")

    if not (num.isnumeric() or dig.isnumeric()):
        print("Datos inválidos")
        return menu_ocurre_en()
    num = int(num)
    dig = int(dig)

    return ocurre_en(dig, num)


def ocurre_en(dig, num):

    res = 1
    while num > 0:
        if num % 10 == dig:
            return res
        num //= 10
        res += 1
    return print("El dígito no está dentro del número")


# 7
def menu_ocurre_en_v2():
    num = input("Ingrese el número entero: ")
    dig = input("Ingrese el dígito que quiera buscar: ")

    if not (num.isnumeric() or dig.isnumeric()):
        print("Datos inválidos")
        return menu_ocurre_en_v2()
    num = int(num)
    dig = int(dig)

    return ocurre_en_v2(dig, num)


def ocurre_en_v2(dig, num):
    res = 1
    largo = get_largo(num) - 1

    while num > 0:
        if num // 10**largo == dig:
            return res
        
        num %= 10**largo
        res += 1
        largo -= 1


# 8
def menu_mayor_digito():
    num = input("Ingrese el número que quiera encontrar su mayor dígito: ")

    if not num.isnumeric():
        print("Ingrese datos válidos")
        return menu_mayor_digito()
    num = int(num)

    return mayor_digito(num)


def mayor_digito(num):

    mayor = 0
    while num > 0:
        if num % 10 > mayor:
            mayor = num % 10
        num //= 10
    return mayor


# 9
def menu_ocurre_mas():
    num = input("Ingrese el número: ")

    if not num.isnumeric():
        print("Ingrese datos válidos")
        return menu_ocurre_mas()
    num = int(num)

    return ocurre_mas(num)


def ocurre_mas(num):
    res = num % 10
    biggest = 0

    while num > 0:
        current = 0
        num2 = num
        while num2 > 0:

            if current > biggest:
                res = num % 10
                biggest = current
                
            elif current == biggest:
                res = -1                

            if num2 % 10 == num % 10:
                current += 1
                
            print(current, biggest, res)

            num2 //= 10
        num //= 10
    return res


# 10
def menu_agregar_digito():
    num = input("Ingrese el número: ")
    dig = input("Ingrese el dígito de la suma: ")

    if not (num.isnumeric() or dig.isnumeric()):
        print("Ingrese datos válidos")
        return agregar_digito()
    num = int(num)
    dig = int(dig)

    return agregar_digito(num, dig)


def agregar_digito(num, dig):

    power = 0
    res = 0

    while num > 0:
        res += ((num % 10 + dig) % 10) * (10**power)
        power += 1
        num //= 10

    return res


# 11
def menu_residuo_division():
    n1 = input("Ingrese el número que será dividido: ")
    if not n1.isnumeric():
        print("Ingrese datos válidos para el primer número")
        return menu_residuo_division()
    n2 = input("Ingrese el número divisor: ")
    if not n2.isnumeric():
        print("Ingrese un dato válido para el divisor")
        return menu_residuo_division()
    n1 = float(n1)
    n2 = float(n2)

    return residuo_division(n1, n2)


def residuo_division(n1, n2):

    if n2 == 0:
        print("No se puede dividir entre 0")
        return division_truncada()

    cont = 0
    while n1 > n2:
        n1 -= n2
        cont += 1

    return n1


# 12
def menu_suprimir_digito():
    n1 = input("Ingrese el número: ")
    if not n1.isnumeric():
        print("Ingrese datos válidos para el primer número")
        return menu_suprimir_digito()
    n2 = input("Ingrese el número que será suprimido: ")
    if not n2.isnumeric():
        print("Ingrese un dato válido para el divisor")
        return menu_suprimir_digito()
    n1 = int(n1)
    n2 = int(n2)

    return suprimir_digito(n1, n2)


def suprimir_digito(n1, n2):

    res = 0
    power = 0

    while n1 > 0:
        if not n1 % 10 == n2:
            res += (n1 % 10) * (10**power)
            power += 1
        n1 //= 10
    return res


# 13
def menu_primo_palindromo():
    num = input("Ingrese el número: ")

    if not num.isnumeric():
        print("Ingrese un dato válido")
        return menu_primo_palindromo()
    num = int(num)

    return primo_palindromo(num)


def primo_palindromo(num):
    if num == invert_number(num) and is_prime(num) == True:
        return "Sí es un número primo palíndromo"
    return "No es un número primo palíndromo"


# 14
def menu_cuadradado_mas_cercano():
    num = input("Ingrese el número: ")

    if not num.isnumeric():
        print("Ingrese un dato válido")
        return menu_cuadradado_mas_cercano()
    num = int(num)

    return cuadradado_mas_cercano(num)


def cuadradado_mas_cercano(num):

    c = 1
    while c**2 < num:
        c += 1

    return (c - 1) ** 2


# 15
def menu_sumatoria_expresion():
    num = input("Ingrese el número: ")

    if not num.isnumeric():
        print("Ingrese un dato válido")
        return menu_sumatoria_expresion()
    num = int(num)

    return sumatoria_expresion(num)


def sumatoria_expresion(n):
    sum = 0
    while n != 0:
        sum += 2 * n / (1 + 3 * n)
        n -= 1
    return sum


# 16
def menu_sumatoria_expresion_2():
    num = input("Ingrese el número: ")

    if not num.isnumeric():
        print("Ingrese un dato válido")
        return menu_sumatoria_expresion_2()
    num = int(num)

    return sumatoria_expresion_2(num)


def sumatoria_expresion_2(n):
    sum = 0
    while n != 0:
        sum += (3 * n - 2) / (1 + 3 * n)
        n -= 1
    return sum


# 17
def menu_calcular_fecha():
    day = input("Ingrese el día: ")
    month = input("Ingrese el mes: ")
    year = input("Ingrese el año: ")

    if not( day.isnumeric() or month.isnumeric() or year.isnumeric()):
        print("Ingrese datos válidos")
        return menu_calcular_fecha()
    day = int(day)
    month = int(month)
    year = int(year)

    return calcular_fecha(day, month, year)


def calcular_fecha(day, month, year):
    if year < 1980:
        return

    if month == 1:
        sum_month = 0
    elif month == 2:
        sum_month = 31
    elif month == 3:
        sum_month = 59
    elif month == 4:
        sum_month = 90
    elif month == 5:
        sum_month = 120
    elif month == 6:
        sum_month = 151
    elif month == 7:
        sum_month = 181
    elif month == 8:
        sum_month = 212
    elif month == 9:
        sum_month = 243
    elif month == 10:
        sum_month = 273
    elif month == 11:
        sum_month = 304
    elif month == 12:
        sum_month = 334

    return (year - 1980) * 365 + (year - 1980) // 4 + sum_month + day


# 18
def menu_sumas_pares():
    n = input("Ingrese su número: ")

    if not n.isnumeric():
        print("Ingrese un dato válido")
        return menu_sumas_pares()

    n = int(n)

    return sumas_pares(n)


def sumas_pares(n):
    sum = 0
    while n != 0:
        if (n % 10 % 2) == 0:
            sum += n % 10
        n = n // 10
    return sum


# 19
def menu_es_anno_bisiesto():
    year = input("Ingrese el año: ")

    if not year.isnumeric():
        print("Ingrese un dato válido")
        return menu_es_anno_bisiesto()
    year = int(year)

    return es_anno_bisiesto(year)


def es_anno_bisiesto(year):
    return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)


# 20
def menu_encontrar_cuadrados():
    n = input("Ingrese el número: ")

    if not n.isnumeric():
        print("Ingrese un dato válido")
        return menu_encontrar_cuadrados()
    n = int(n)

    return encontrar_cuadrados(n)


def encontrar_cuadrados(n):
    x = int(n ** (0.5))
    if x * x == n:
        return x - 1
    return x


# 21
def menu_primo_cercano():
    n = input("Ingrese el número: ")

    if not n.isnumeric():
        print("Ingrese un dato válido")
        return menu_primo_cercano()
    n = int(n)

    return primo_cercano(n)


def primo_cercano(n):
    counter = n
    while is_prime(counter) == False:
        counter += 1
    return counter

# 22
def menu_cantidad_palindromos():
    n = input("Ingrese el número: ")

    if not n.isnumeric():
        print("Ingrese un dato válido")
        return menu_cantidad_palindromos()
    n = int(n)

    return cantidad_palindromos(n)


def cantidad_palindromos(n):
    x = 0
    while n != 0:
        if es_palindromo(n):
            x += 1
        n -= 1
    return x


# 23
def menu_cuadrados_entre_numeros():
    n1 = input("Ingrese su primer número: ")
    n2 = input("Ingrese su primer número: ")

    if not (n1.isnumeric() or n2.isnumeric()):
        print("Ingrese datos válidos")
        return menu_cuadrados_entre_numeros()

    n1 = int(n1)
    n2 = int(n2)

    return cuadrados_entre_numeros(n1, n2)


def cuadrados_entre_numeros(n1, n2):
    return abs(int(n1 ** (0.5)) - int(n2 ** (0.5)))


# 24
def menu_truncar():
    n = input("Ingrese el número: ")

    if not is_float(n):
        print("Ingrese un dato válido")
        return menu_truncar()
    n = float(n)

    return truncar(n)


def truncar(n):
    return int(n)


# 25
def menu_menores_fibonacci():
    n = input("Ingrese el número: ")

    if not n.isnumeric():
        print("Ingrese un dato válido")
        return menu_menores_fibonacci()
    n = int(n)

    return menores_fibonacci(n)


def menores_fibonacci(n):
    current = 1
    last = 0
    result = 0
    con = 0

    while current < n:
        result = last + current
        last = current
        current = result

        con += 1

    return con + 1  # se suma uno por el primer 0 que no se cuenta en el while


# 26
def menu_pares_fibonacci():
    n = input("Ingrese el número: ")

    if not n.isnumeric():
        print("Ingrese un dato válido")
        return menu_pares_fibonacci()
    n = int(n)

    return pares_fibonacci(n)


def pares_fibonacci(n):
    current = 1
    last = 0
    result = 0
    con = 0

    while current < n:
        if result % 2 == 0 and result > 1:
            con += 1

        result = last + current
        last = current
        current = result

    return con


# 27
def menu_redondear_valor():
    n = input("Ingrese el número: ")

    if not is_float(n):
        print("Ingrese un dato válido")
        return menu_redondear_valor()
    n = float(n)

    return redondear_valor(n)


def redondear_valor(n):
    if (n + 0.5) // 1 == (n // 1):
        return int(n // 1)
    return int((n // 1) + 1)


# 28
def menu_cuenta_primos():
    n1 = input("Ingrese su primer número: ")
    n2 = input("Ingrese su segundo número: ")

    if not (n1.isnumeric() or n2.isnumeric()):
        print("Ingrese datos válidos")
        return menu_cuenta_primos()

    n1 = int(n1)
    n2 = int(n2)

    return cuenta_primos(n1, n2)


def cuenta_primos(n1, n2):
    counter = 0
    while n1 < n2:
        if is_prime(n1):
            counter += 1
        n1 += 1
    return counter


# 29
def menu_cuantos_cuadrados():
    n = input("Ingrese el número: ")

    if not n.isnumeric():
        print("Ingrese un dato válido")
        return menu_cuantos_cuadrados()
    n = int(n)

    return cuantos_cuadrados(n)


def cuantos_cuadrados(n):
    power = 1
    sum_power = 0

    while sum_power < n:
        sum_power += power**2
        power += 1

    return power - 1


# 30
def menu_cuantos_primos():
    n = input("Ingrese el número: ")

    if not n.isnumeric():
        print("Ingrese un dato válido")
        return menu_cuantos_primos()
    n = int(n)

    return cuantos_primos(n)


def cuantos_primos(n):

    result = 0
    counter = 2
    sum_prime = 0

    while sum_prime < n:
        if is_prime(counter) == True:
            result += 1
            sum_prime += counter
        counter += 1
    return result


def ask_menu():
    opt = input(
        "\n---------------------------------------------------------------------------------------\n Menú de los ejercicios, por favor seleccione una opción (Para mostrar menú, digite 0)\n---------------------------------------------------------------------------------------\n>"
    )

    match opt:
        case "0":
            show_menu()
            return ask_menu()

        case "1":
            print(menu_potencia_mas_cercana())
            return ask_menu()

        case "2":
            print(menu_cantidad_decimales())
            return ask_menu()

        case "3":
            print(menu_digitos_diferentes())
            return ask_menu()

        case "4":
            print(menu_es_palindromo())
            return ask_menu()

        case "5":
            print(menu_division_truncada())
            return ask_menu()

        case "6":
            print(menu_ocurre_en())
            return ask_menu()

        case "7":
            print(menu_ocurre_en_v2())
            return ask_menu()

        case "8":
            print(menu_mayor_digito())
            return ask_menu()

        case "9":
            print(menu_ocurre_mas())
            return ask_menu()

        case "10":
            print(menu_agregar_digito())
            return ask_menu()

        case "11":
            print(menu_residuo_division())
            return ask_menu()

        case "12":
            print(menu_suprimir_digito())
            return ask_menu()

        case "13":
            print(menu_primo_palindromo())
            return ask_menu()

        case "14":
            print(menu_cuadradado_mas_cercano())
            return ask_menu()

        case "15":
            print(menu_sumatoria_expresion())
            return ask_menu()

        case "16":
            print(menu_sumatoria_expresion_2())
            return ask_menu()
        case "17":
            print(menu_calcular_fecha())
            return ask_menu()
        case "18":
            print(menu_sumas_pares())
            return ask_menu()
        case "19":
            print(menu_es_anno_bisiesto())
            return ask_menu()
        case "20":
            print(menu_encontrar_cuadrados())
            return ask_menu()
        case "21":
            print(menu_primo_cercano())
            return ask_menu()
        case "22":
            print(menu_cantidad_palindromos())
            return ask_menu()
        case "23":
            print(menu_cuadrados_entre_numeros())
            return ask_menu()
        case "24":
            print(menu_truncar())
            return ask_menu()
        case "25":
            print(menu_menores_fibonacci())
            return ask_menu()
        case "26":
            print(menu_pares_fibonacci())
            return ask_menu()
        case "27":
            print(menu_redondear_valor())
            return ask_menu()
        case "28":
            print(menu_cuenta_primos())
            return ask_menu()
        case "29":
            print(menu_cuantos_cuadrados())
            return ask_menu()
        case "30":
            print(menu_cuantos_primos())
            return ask_menu()
        case "31":
            return print("Cerrando programa...")


ask_menu()

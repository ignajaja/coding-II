'''Ejercicios de Programación – Menús
A continuación se presentan 11 ejercicios en los que deberá implementar
funciones en Python.
Para las 11 funciones programe un menú en consola, con inpust y prints.
Todos los programas deben tener un menú propio, y el programa un menú principal
donde se seleccione el ejercicio a evaluar. Debe hacer las validaciones de las
entradas y dar los mensajes conrrespondientes para cada opción.
Agregue una opción en el menú para salir.
'''

'''
Ejercicio 1: Número dentro de rango
Crea una función que reciba un número y devuelva
"Dentro del rango" si está entre 10 y 20 (inclusive), y "Fuera del rango" en caso contrario.
'''

def menu_is_inside_range():
    print("MENU Número dentro de rango")
    num = input("Ingrese un número: ")

    if not num.isnumeric():
        print("Error, debe ingresar un número")
    else:
        num_numeric = float(num)
        if 10 <= num_numeric <= 20:
            return "Dentro del rango"
        else:
            return "Fuera del rango"

#Ejericio 2: No utilizar else ni elif
'''
Ejercicio 2: Comparar con cero
Escribe una función que reciba un número y devuelva "Cero" si es exactamente 0,
"Mayor que cero" si es positivo, y "Menor que cero" si es negativo.
'''

def menu_compare_to_cero():
    print("MENU Comparar número a cero")
    num = input("Ingrese un número: ")

    if not num.isnumeric():
        print("Error, debe ingresar un número")
    else:
        num_numeric = float(num)
        if num_numeric > 0:
            return "Mayor que cero"
        if num_numeric < 0:
            return "Menor que cero"
        return "Cero"

#Ejericio 3: utilizar elif
'''
Ejercicio 3: Clasificación de temperatura
Haz una función que reciba una temperatura en °C y devuelva:
"Frío" si es menor a 15
"Templado" si está entre 15 y 25
"Calor" si es mayor a 25
'''

def menu_classify_temperature():
    print("MENU Clasificar temperatura")
    temp = input("Ingrese la temperatura: ")

    if not temp.isnumeric():
        print("Error, debe ingresar un número")
    else:
        temp_numeric = float(temp)
        if temp_numeric < 15:
            return "Frío"
        elif temp_numeric > 25:
            return "Calor"
        else:
            return "Templado"

#Ejercicio 4: No utilizar elif, solo if y else
'''
Ejercicio 4: Determinar mayor de tres números
Crea una función que reciba tres números y devuelva el mayor de ellos.
Si hay dos iguales que sean los mayores, igual debe devolver ese número.
'''

def menu_determine_larger():
    print("MENU Determinar número mayor")
    num1 = input("Ingrese el primer número: ")
    if not num1.isnumeric():
        print("Error, ingrese un número válido")
    else:
        num1_numeric = float(num1)
        num2 = input("Ingrese el segundo número: ")
        if not num2.isnumeric():
            print("Error, ingrese un número válido")
        else:
            num2_numeric = float(num2)
            num3 = input("Ingrese el tercer número: ")
            if not num3.isnumeric():
                print("Error, ingrese un número válido")
            else:
                num3_numeric = float(num3)

                if num1_numeric >= num2_numeric:
                    if num1_numeric >= num3_numeric:
                        return num1_numeric
                    else:
                        return num3_numeric
                else:
                    if num2_numeric >= num3_numeric:
                        return num2_numeric
                    else: 
                        return num3_numeric


#Ejericio 5: Utilizar if y elif
'''
Ejercicio 5: Categoría de edad
Diseña una función que reciba la edad de una persona y devuelva:
"Niño" si es menor de 12
"Adolescente" si está entre 12 y 17
"Adulto" si está entre 18 y 59
"Adulto mayor" si es 60 o más
'''

def menu_categorize_age():
    print("MENU Categorizar edad")
    age = input("Ingrese la edad: ")

    if not age.isnumeric():
        print("Error, ingrese un número")
    else:
        age_numeric = float(age)
        if age_numeric < 12:
            return "Niño"
        elif age_numeric < 17:
            return "Adolescente"
        elif age_numeric < 59:
            return "Adulto"
        return "Adulto mayor"

'''
Ejercicio 6: Nota en letra
Haz una función que reciba una calificación numérica (0-100) y retorne la letra correspondiente:
A: 90 a 100
B: 80 a 89
C: 70 a 79
D: 60 a 69
F: menos de 60
'''

def menu_convert_grade_to_letter():
    print("MENU Convertir nota a letra")
    grade = input("Ingrese la nota: ")

    if not grade.isnumeric():
        print("Error, ingrese un número")
    else:
        grade_numeric = float(grade)
        if grade_numeric < 60:
            return "Su nota es: F"
        elif grade_numeric < 70:
            return "Su nota es: D"
        elif grade_numeric < 80:
            return "Su nota es: C"
        elif grade_numeric < 90:
            return "Su nota es: B"
        return "Su nota es: A"

# Hacerlo con print,no con returns
'''
Ejercicio 6.1: Nota en letra
Haz una función que reciba una calificación numérica (0-100) y muestre (PRINT) la letra correspondiente:
A: 90 a 100
B: 80 a 89
C: 70 a 79
D: 60 a 69
F: menos de 60
'''

def menu_convert_grade_to_letter_v2():
    print("MENU Convertir nota a letra")
    grade = input("Ingrese la nota: ")

    if not grade.isnumeric():
        print("Error, ingrese un número")
    else:
        grade_numeric = float(grade)
        letter = ""
        if grade_numeric < 60:
            letter = "F"
        elif grade_numeric < 70:
            letter = "D"
        elif grade_numeric < 80:
            letter = "C"
        elif grade_numeric < 90:
            letter = "B"
        else:
            letter = "A"
        print(f"Su nota es de: {letter}")
        return


'''
Ejercicio 7: Año bisiesto
Crea una función que reciba un año y devuelva True si es bisiesto o False en caso contrario.
Recuerde:
Si es divisible entre 400 → bisiesto.
Si es divisible entre 100 → no bisiesto
Si es divisible entre 4 → bisiesto.
'''

def menu_is_leap_year():
    print("MENU Es año bisiesto")
    year = input("Ingrese el año: ")

    if not year.isnumeric():
        print("Error, ingrese un número")
    else:
        year_numeric = float(year)
        if anno % 4 == 0:
            return "Es año bisiesto"
        return "No es año bisiesto"

'''
Ejercicio 8: Descuento en tienda
Una tienda aplica descuentos según el monto de la compra.
Crea una función que reciba el total de la compra y devuelva el porcentaje de descuento aplicado:
10% si es mayor o igual a 1000
5% si es mayor o igual a 500
0% en caso contrario
'''

def menu_calculate_discount():
    print("MENU Es año bisiesto")
    price = input("Ingrese el año: ")

    if not price.isnumeric():
        print("Error, ingrese un número")
    else:
        price_numeric = float(price)
        if costo >= 1000:
            return "Su descuento es de 10%"
        elif costo >= 500:
            return "Su descuento es de 5%"
        else:
            return "Su descuento es de 0%"

'''
Ejercicio 9: Identificar vocal o consonante
Crea una función que reciba una letra del alfabeto y devuelva "Vocal"
si es a, e, i, o, u (mayúscula o minúscula) y "Consonante" en caso contrario.
'''

def menu_identify_letter():
    print("MENU Identificar vocal o consonante")
    letter = input("Ingrese la letra: ")

    letra = letra.lower()
    if letra == "a" or letra == "e" or letra == "i" or letra == "o" or letra == "u":
        return "Vocal"
    else:
        return "Consonante"

'''
Ejercicio 10: Comparar dos cadenas
Escribe una función que reciba dos cadenas y devuelva:
"Son iguales" si ambas son idénticas.
"Primera mayor" si la primera es mayor en orden alfabético.
"Segunda mayor" si la segunda es mayor en orden alfabético.
'''

def menu_compare_strings():
    print("MENU Comparar strings")
    str1 = input("Ingrese su primera cadena")
    str2 = input("Ingrese su segunda cadena")

    str1 = str1.lower()
    str2 = str2.lower()
    if str1 > str2:
        return "Primera mayor"
    elif str1 < str2:
        return "Segunda mayor"
    else:
        return "Iguales"


def show_main_menu():
    print("================================")
    print("|        MENÚ PRINCIPAL        |")
    print("Seleccione uan opción: ")
    print("1. Número dentro de rango")
    print("2. Comparar con cero")
    print("3. Clasificación de temperatura")
    print("4. Determinar número mayor de tres")
    print("5. Categoría de edad")
    print("6. Nota en letra")
    print("6.1 Nota en letra (sin returns)")
    print("7. Año bisiesto")
    print("8. Descuento en tienda")
    print("9. Identificar vocal o consonante")
    print("10. Comparar dos cadenas")
    print("11. Salir")
    print("================================")

    option = input("Ingrese su elección: ")
    print('')
    print("================================")


    match option:
        case "1":
            print(menu_is_inside_range())
        case "2":
            print(menu_compare_to_cero())
        case "3":
            print(menu_classify_temperature())
        case "4":
            print(menu_determine_larger())
        case "5":
            print(menu_categorize_age())
        case "6":
            print(menu_convert_grade_to_letter())
        case "6.1":
            print(menu_convert_grade_to_letter_v2())
        case "7":
            print(menu_is_leap_year())
        case "8":
            print(menu_calculate_discount())
        case "9":
            print(menu_identify_letter())
        case "10":
            print(menu_compare_strings())
        case "11":
            return print("Saliendo...")
        case _:
            print("Ingrese una opción válida")


    show_main_menu()

show_main_menu()
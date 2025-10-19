def is_adult(age):
    if age >= 18:
        return True
    return False

def is_able_for_rollercoaster(age, height):
    if is_adult(age) and height >= 160 and height < 220:
        return True
    return False

def determine_triangle_type(side1, side2, side3):
    if side1 == side2 and side2 == side3:
        return "Equielatero"
    elif side1 != side2 and side1 != side3 and side2 != side3:
        return "Escaleno"
    else:
        return "Isóceles"

def menu_is_adult():
    print("------ Es adulto ------")
    edad = input("Digite la edad: ")

    if not edad.isnumeric():
        print("Error! Debe ingresar un número válido")

    else:
        edad_numerica = float(edad)
        if is_adult(edad_numerica):
            print("La persona es mayor de edad")
        else:
            print("Es menor de edad")

def menu_rollercoaster():
    print("------ ¿Puede subir a la montaña rusa? ------")
    age = input("Digite su edad: ")
    
    if not age.isnumeric():
        print("La edad debe ser numérico")
    else:
        height = input("Digite su estatura en cm: ")
        if not height.isnumeric():
            print("La estatura debe ser numérica")
        else:
            age_num = float(age)
            height_num = float(height)
            if is_able_for_rollercoaster(age_num, height_num):
                print("Sí puede subir a la montaña rusa")
            else:
                print("No puede entrar a la montañá rusa")

def menu_triangle():
    print("------ Qué triángulo es ------")

    # lado 1
    side1 = input("Ingrese el lado 1: ")
    if not side1.isnumeric():
        print("El lado 1 debe ser numérico")
        return
    else:
        side1_num = float(side1)
        if side1_num <= 0:
            print("El lado 1 debe ser un número positivo")
            return
        # lado 2
        side2 = input("Ingrese el lado 2: ")
        if not side2.isnumeric():
            print("El lado 2 debe ser numérico")
            return
        else:
            side2_num = float(side2)
            if side2_num <= 0:
                print("El lado 2 debe ser un número positivo")
                return
            else:
                # lado 3
                side3 = input("Ingrese el lado 3: ")
                if not side3.isnumeric():
                    print("El lado 3 debe ser numérico")
                else:
                    side3_num = float(side3)
                    if side3_num <= 0:
                        print("El lado 3 debe ser un número positivo")
                        return
                    else:
                        triangle_type = determine_triangle_type(side1_num, side2_num, side3_num)

                        print(f"Un triángulo con lados {side1}, {side2}, {side3} es de tipo {triangle_type}")


def menu():
    print()
    print("______------- MENÚ -------______")
    print("|       1. Es adulto           |")
    print("|       2. Puede subir?        |")
    print("|       3. Tipo de triángulo   |")
    print("|       4. Salir               |")
    print("|==============================|")
    print("")
    
    opcion = input("Seleccione una opción: ")

    if opcion == '1':
        menu_is_adult()
    elif opcion == '2':
        menu_rollercoaster()
    elif opcion == '3':
        menu_triangle()
    elif opcion == '4':
        print("Saliendo...")
        return

    else:
        print("Elija una opción válida")

    menu()

menu()
# variables
clients = []


# commons

def save_clients():
    global clients

    with open ("clientes.txt", "w") as archivo:
        archivo.write(str(clients))
    
    print("Archivo clientes.txt guardado con éxito")
    return

def load_clients():
    global clients
    try:
        with open("clientes.txt", "r") as file:
            clients = eval(file.read())
    except:
        clients = []

# validations
def validate_option():
    opt = input("Seleccione una opción: ")
    if opt == '':
        print("Debe ingresar una opción.")
        return validate_option()
    if not opt.isnumeric():
        print("Debe ingresar un número.")
        return validate_option()
    opt = int(opt)
    if not 1 <= opt <= 7:
        print("Debe ingresar una opción del 1 al 7.")
        return validate_option()
    return opt

def validate_name(insert = False):
    global clients

    name = input("Ingrese el nombre: ")
    if name == '':
        print("No puede dejar el campo del nombre vacío")
        return validate_name()


    if not clients == [] and insert == True:
        for client in clients:
            if client['nombre'] == name:
                print("No se pueden repetir los nombre de los clientes.")
                return validate_name()
    
    return name

def validate_salary():
    salary = input("Ingrese el salario: ")
    if not salary.isnumeric():
        print("Valor de salario no válido")
        return validate_salary()
    salary = float(salary)
    if salary < 0:
        print("El valor no puede ser positivo")
        return validate_salary()
    return salary

def validate_credits():
    credit = input("Ingrese los créditos: ")
    if not credit.isnumeric():
        print("Valor de créditos no válido")
        return validate_credits()
    credit = float(credit)
    if credit < 0:
        print("Los valores agregados no pueden ser negativos")
        return validate_credits()
    return credit

def validate_children():

    c_name = input("Ingrese el nombre de el hijo: ")
    if c_name == "":
        print("No puede dejarse el espacio en blanco")
        return validate_children()
    c_age = input("Ingrese la edad de el hijo: ")
    if not c_age.isnumeric():
        print("Valor de edad no válido") 
        return validate_children()
    c_age = int(c_age)
    if c_age < 0:
        print("Valor de edad no válido")
        return validate_children()
    
    return {"nombre": c_name, "edad": c_age}

def ask_children(children):
    child = input("¿Desea ingresar un hijo? (s/n)")
    if child.lower() == 's':
        children.append(validate_children())
        return ask_children(children)
    return children

def validate_age():
    age = input("Ingrese la edad: ")
    if not age.isnumeric():
        print("Valor de edad no válido")
        return validate_age()
    age = int(age)
    if age < 0:
        print("El valor no puede ser negativo")
        return validate_age()
    return age


# funcitions

def insert_client(): # función 1
    global clients

    new_client = {
        "nombre": validate_name(True),
        "salario": validate_salary(),
        "credito": validate_credits(),
        "hijos": ask_children([])
    }

    clients.append(new_client)

    print("Cliente insertado con éxito")
    save_clients()
    return show_menu()


def search_client(): # función 2
    global clients

    name = validate_name()

    for client in clients:
        if client['nombre'].lower() == name.lower():
            print(f"Nombre: {client['nombre']}\nSalario: {client['salario']}\nCréditos: {client['credito']}\nHijos: {client['hijos']}")

        print("Cliente mostrado con éxito")
        save_clients()
        return show_menu()


def modify_client(): # función 3
    global clients

    name = validate_name()

    for client in clients:
        if client['nombre'].lower() == name.lower():
            client['salario'] = validate_salary()
            client['credito'] = validate_credits()
            client['hijos'] = ask_children([])

    print("Cliente modificado con éxito")
    save_clients()
    return show_menu()


def delete_client(): # función 4
    global clients

    name = validate_name()
    new_list = []

    for client in clients:
        if not client['nombre'].lower() == name.lower():
            new_list.append(client)
    
    clients = new_list

    print("Cliente eliminado con éxito")
    save_clients()
    return show_menu()


def print_client(): # función 5
    global clients


    for client in clients:
        print(f"Nombre: {client['nombre']}\nSalario: {client['salario']}\nCréditos: {client['credito']}\nHijos: {client['hijos']}\n")

    print("Cliente mostrado con éxito")
    save_clients()
    return show_menu()


def consult_children(): # función 6
    global clients

    age = validate_age()
    for client in clients:
        for child in client['hijos']:
            if int(child['edad']) > age:
                print(f"Nombre: {client['nombre']}\nSalario: {client['salario']}\nCréditos: {client['credito']}\nHijos: {client['hijos']}\n")
                break

    print("Consulta realizada con éxito")
    save_clients()
    return show_menu()


def close_program(): # función 7
    return print("Muchas gracias\nCerrando programa...")


def show_menu():
    load_clients()

    print("================ Menú ================\n")
    print(
        "1. Insertar cliente.\n"
        "2. Buscar cliente.\n"
        "3. Modificar cliente.\n"
        "4. Eliminar cliente.\n"
        "5. Imprimir clientes.\n"
        "6. Consultar clientes por edad de hijos.\n"
        "7. Salir.\n"
    )

    option = validate_option()

    match option:
        case 1:
            insert_client()
        case 2:
            search_client()
        case 3:
            modify_client()
        case 4:
            delete_client()
        case 5:
            print_client()
        case 6:
            consult_children()
        case 7:
            close_program()
    return


show_menu()
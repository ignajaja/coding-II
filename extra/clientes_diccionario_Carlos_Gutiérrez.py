# manejo de datos de clientes, diccionarios
# procederé a programar la solución en inglés para acostumbrar esta buena práctica,
# aunque no en todo el código

client = []

def save_client():
    global client
    
    with open("client.txt", "w") as file:
        file.write(str(client))

def load_client():
    global client
    try:
        with open("client.txt", "r") as file:
            client = eval(file.read())
    except:
        client = []

#E: 
#S: inserta el cliente en un diccionario en la lista de client
#R:  su nombre no debe estar en la lista de diccionarios, su salario y créditos deben ser > 0
def insert_client():
    global client
    name = input("Ingrese el nombre del cliente: ")
    for c in client:
        if c["nombre"].lower() == name.lower():  
            print("Error: el cliente ya existe")
            return
    
    salary = float(input("Ingrese el salario del cliente: "))
    if salary < 0:
        print("Error: Debe ingresar un salario mayor o igual a cero")
        return
    
    credits_var = float(input("Ingrese los créditos del cliente: "))
    if credits_var < 0:
        print("Error: Debe ingresar un número de créditos mayor o igual a cero")
        return 
    new_client = {
        "nombre": name,        
        "salario": salary,    
        "creditos": credits_var,
        "hijos": []          
    }

    while True:         #manejo de los hijos
        opcion = input("¿Agregar hijo?(s/n): ")
        if opcion.lower() == "s":
            child_name = input("Ingrese el nombre del hijo: ")
            age = int(input("Ingrese la edad del hijo: "))
            new_client["hijos"].append({"nombre": child_name, "edad": age})
        elif opcion.lower() == "n":
            client.append(new_client)
            save_client()
            print("Cliente insertado con éxito y guardado en client.txt")
            return ""
        else:
            print("Opción no válida. Responda con 's' o 'n'.")

#E:
#S: busca y retorna el cliente en base a su nombre
#R: 
def search_client():
    global client
    name = input("Ingrese el nombre del cliente que desea buscar: ")
    
    for cliente in client:
        if cliente["nombre"].lower() == name.lower():
            print("Cliente encontrado:")
            print(f"Nombre: {cliente['nombre']}")
            print(f"Salario: {cliente['salario']}")
            print(f"Créditos: {cliente['creditos']}")
            print(f"Hijos: {cliente['hijos']}")
            return cliente
    
    print("Cliente no encontrado")
    return ""
#E:
#S: modifica los datos a escojer de un cliente determinado por su nombre
#R:
def modify_client():
    global client
    name = input("Ingrese el nombre del cliente que desea modificar: ")
    
    for cliente in client:
        if cliente["nombre"].lower() == name.lower():
            print("\n¿Qué aspecto desea modificar?")
            print("1. Nombre")
            print("2. Salario") 
            print("3. Créditos")
            print("4. Hijos")
            
            opcion = input("Seleccione una opción (1-4): ")
            
            if opcion == "1":
                nuevo_nombre = input("Ingrese el nuevo nombre: ")

                for c in client:
                    if c["nombre"].lower() == nuevo_nombre.lower() and c != cliente:
                        print("Error: Ya existe un cliente con ese nombre")
                        return
                cliente["nombre"] = nuevo_nombre
                print("Nombre modificado con éxito")
                
            elif opcion == "2":
                nuevo_salario = float(input("Ingrese el nuevo salario: "))
                if nuevo_salario < 0:
                    print("Error: El salario debe ser mayor o igual a cero")
                    return
                cliente["salario"] = nuevo_salario
                print("Salario modificado con éxito")
                
            elif opcion == "3":
                nuevos_creditos = float(input("Ingrese los nuevos créditos: "))
                if nuevos_creditos < 0:
                    print("Error: Los créditos deben ser mayor o igual a cero")
                    return
                cliente["creditos"] = nuevos_creditos
                print("Créditos modificados con éxito")
                
            elif opcion == "4":
                print("\nGestión de hijos:")
                print("1. Agregar hijo")
                print("2. Eliminar hijo")
                print("3. Modificar hijo")
                
                opcion_hijos = input("Seleccione una opción (1-3): ")
                
                if opcion_hijos == "1":
                    child_name = input("Ingrese el nombre del hijo: ")
                    age = int(input("Ingrese la edad del hijo: "))
                    if age < 0:
                        print("Error: La edad debe ser mayor o igual a cero")
                        return
                    cliente["hijos"].append({"nombre": child_name, "edad": age})
                    print("Hijo agregado con éxito")
                    
                elif opcion_hijos == "2":
                    if not cliente["hijos"]:
                        print("El cliente no tiene hijos")
                        return
                    
                    print("Hijos del cliente:")
                    for i, hijo in enumerate(cliente["hijos"]):
                        print(f"{i+1}. {hijo['nombre']} ({hijo['edad']} años)")
                    
                    try:
                        indice = int(input("Seleccione el número del hijo a eliminar: ")) - 1
                        if 0 <= indice < len(cliente["hijos"]):
                            hijo_eliminado = cliente["hijos"].pop(indice)
                            print(f"Hijo {hijo_eliminado['nombre']} eliminado")
                        else:
                            print("Número inválido")
                    except:
                        print("Entrada inválida")
                        
                elif opcion_hijos == "3":
                    if not cliente["hijos"]:
                        print("El cliente no tiene hijos")
                        return
                    
                    print("Hijos del cliente:")
                    for i, hijo in enumerate(cliente["hijos"]):
                        print(f"{i+1}. {hijo['nombre']} ({hijo['edad']} años)")
                    
                    try:
                        indice = int(input("Seleccione el número del hijo a modificar: ")) - 1
                        if 0 <= indice < len(cliente["hijos"]):
                            nuevo_nombre = input("Ingrese el nuevo nombre del hijo: ")
                            nueva_edad = int(input("Ingrese la nueva edad del hijo: "))
                            if nueva_edad < 0:
                                print("Error: La edad debe ser mayor o igual a cero")
                                return
                            cliente["hijos"][indice]["nombre"] = nuevo_nombre
                            cliente["hijos"][indice]["edad"] = nueva_edad
                            print("Hijo modificado con éxito")
                        else:
                            print("Número inválido")
                    except:
                        print("Entrada inválida")
                else:
                    print("Opción inválida")
                    return
            else:
                print("Opción inválida")
                return
                
            save_client()
            print("Cambios guardados correctamente")
            return
    
    print("Cliente no encontrado")

#E:
#S: borra un cliente en base a su nombre, al finalizar, lo retorna
#R:
def delete_client():
    global client
    name = input("Ingrese el nombre del cliente que desea eliminar: ")
    
    for i, cliente in enumerate(client):
        if cliente["nombre"].lower() == name.lower():
            print(f"Cliente encontrado: {cliente['nombre']}")
            confirmar = input("¿Está seguro de eliminar este cliente? (s/n): ")
            if confirmar.lower() == "s":
                cliente_eliminado = client.pop(i)
                save_client()
                print(f"Cliente {cliente_eliminado['nombre']} eliminado con éxito")
            else:
                print("Eliminación cancelada")
            return
    
    print("Cliente no encontrado")

#E:
#S: retorna todos los clientes disponibles al momento
#R: 
def print_clients():
    global client
    if not client:
        print("No hay clientes registrados")
        return
    
    print(f"\n{'='*50}")
    print("LISTA DE CLIENTES")
    print(f"{'='*50}")
    
    for i, cliente in enumerate(client, 1):
        print(f"\nCliente {i}:")
        print(f"  Nombre: {cliente['nombre']}")
        print(f"  Salario: {cliente['salario']}")
        print(f"  Créditos: {cliente['creditos']}")
        print(f"  Hijos: {len(cliente['hijos'])}")
        for hijo in cliente['hijos']:
            print(f"    - {hijo['nombre']} ({hijo['edad']} años)")
#E:
#S: filtra los clientes con hijos mayores a una edad determinada y los retorna
#R:
def consulta_hijos_mayores():
    global client
    try:
        edad_minima = int(input("Ingrese la edad mínima para filtrar hijos: "))
    except:
        print("Error: Debe ingresar un número válido")
        return
    
    clientes_encontrados = []
    
    for cliente in client:
        hijos_mayores = []
        for hijo in cliente["hijos"]:
            if hijo["edad"] > edad_minima:
                hijos_mayores.append(hijo)
        
        if hijos_mayores:
            clientes_encontrados.append({
                "cliente": cliente,
                "hijos_mayores": hijos_mayores
            })
    
    if not clientes_encontrados:
        print(f"No hay clientes con hijos mayores de {edad_minima} años")
        return
    
    print(f"\n{'='*60}")
    print(f"CLIENTES CON HIJOS MAYORES DE {edad_minima} AÑOS")
    print(f"{'='*60}")
    
    for item in clientes_encontrados:
        cliente = item["cliente"]
        hijos_mayores = item["hijos_mayores"]
        
        print("\nCliente: {cliente['nombre']}")
        print("Hijos mayores de {edad_minima} años:")
        for hijo in hijos_mayores:
            print(f"  - {hijo['nombre']} ({hijo['edad']} años)")

def menu():
    load_client() #cargamos los datos del archivo
    
    while True:
        print("\n" + "="*40)
        print("       SISTEMA DE GESTIÓN DE CLIENTES")
        print("="*40)
        print("1. Insertar cliente")
        print("2. Buscar cliente")
        print("3. Modificar cliente")
        print("4. Eliminar cliente")
        print("5. Imprimir todos los clientes")
        print("6. Consultar clientes con hijos mayores de X años")
        print("7. Salir")
        print("="*40)
        
        opcion = input("Seleccione una opción (1-7): ")
        
        if opcion == "1":
            insert_client()
        elif opcion == "2":
            search_client()
        elif opcion == "3":
            modify_client()
        elif opcion == "4":
            delete_client()
        elif opcion == "5":
            print_clients()
        elif opcion == "6":
            consulta_hijos_mayores()
        elif opcion == "7":
            print("Ha salido")
            break
        else:
            print("Opción inválida. Por favor seleccione 1-7")


if __name__ == "__main__":
    menu()    




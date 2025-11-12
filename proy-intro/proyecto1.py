import tkinter as tk
import random, json

# lista de vuelos [[código, origen, destino, preocio, matriz de asientos, vendidos],[...],[...]]
vuelos = []

root = None
entrada_origen = entrada_destino = entrada_precio = entrada_filas = entrada_columnas = entrada_codigo = entrada_orden =  entrada_buscar_fila = entrada_buscar_colu = entrada_porcentaje = None
entrada_fila_asiento_1 = entrada_fila_asiento_2 = entrada_colu_asiento_1 = entrada_colu_asiento_2 = None
tamano_botones = (20, 2)


# por hacer 
# 10.	Reservar	varios	asientos	consecutivos	
# 11.	Simular	venta	masiva	


# errores y confirmaciones

def construir_error(msg):
    global root
    win = tk.Toplevel(root)
    win.geometry("400x150")
    win.title("Error")

    contenedor = tk.Frame(win)
    contenedor.pack(fill='both', expand=False, padx=10, pady=10)
    panel = tk.Frame(contenedor)
    panel.pack(fill='y', padx=(0,10))

    tk.Label(panel, text = msg, font = ("Arial", 12, "bold")).pack(anchor="se", pady=10)

    tk.Button(panel, text="Cerrar", command=win.destroy, font=("Arial", 10, "bold"), fg="white", bg="#ff0000").pack(anchor='se', pady=20)

    return

def construir_confirmacion(msg):
    global root
    win = tk.Toplevel(root)
    win.geometry("400x150")
    win.title("Éxito")

    contenedor = tk.Frame(win)
    contenedor.pack(fill='both', expand=False, padx=10, pady=10)
    panel = tk.Frame(contenedor)
    panel.pack(fill='y', padx=(0,10))

    tk.Label(panel, text = msg, font = ("Arial", 12, "bold")).pack(anchor="se", pady=10)

    tk.Button(panel, text="Cerrar", command=win.destroy, font=("Arial", 10, "bold"), fg="white", bg="#ff0000").pack(anchor='se', pady=20)

# guardar y cargar datos
def guardar_vuelo():
    global vuelos

    try:
        with open("vuelos.txt", "w") as archivo:
            json.dump(vuelos, archivo) # se usa el formato json.dump para guardar los datos en el .txt, esto hace que se carguen de manera mucho más sencilla
            # aprendido en https://stackoverflow.com/questions/27745500/how-to-save-a-list-to-a-file-and-read-it-as-a-list-type
    except Exception:
        True
    return

def cargar_vuelos():
    global vuelos

    try:
        with open("vuelos.txt", "r", encoding="utf-8") as archivo:
            vuelos = json.load(archivo)
    except Exception:
        True
    return

# commons
def asientos_disponibles(codigo):
    global vuelos

    total = 0
    cont = 0
    
    for i, vuelo in enumerate(vuelos):
        if vuelo[0] == codigo:
            for fila in vuelo[4]:
                for asiento in fila:
                    if asiento == 1:
                        cont += 1
                    total += 1
    return total - cont

def asientos_ocupados(codigo):
    global vuelos

    cont = 0
    
    for i, vuelo in enumerate(vuelos):
        if vuelo[0] == codigo:
            for fila in vuelo[4]:
                for asiento in fila:
                    if asiento == 1:
                        cont += 1
    return cont

def asientos_totales(codigo):
    global vuelos

    total = 0
    
    for i, vuelo in enumerate(vuelos):
        if vuelo[0] == codigo:
            for fila in vuelo[4]:
                for asiento in fila:
                    total += 1
    return total

def asiento_a_numeros(f, c):
    num_fila = ord(f)
    num_fila -= 65
    num_colu = c-1
    return (num_fila, num_colu)

def asiento_a_letras(f, c):
    num_fila = chr(f + 65)
    num_colu = c+1

    return (num_fila, num_colu)


# funciones del programa

def crear_vuelo():
    global vuelos, entrada_precio, entrada_columnas, entrada_filas, entrada_origen, entrada_destino

    cod_l1 = random.randint(65,90)
    cod_l2 = random.randint(65,90)
    cod_nu = random.randint(100, 999)
    codigo = f"{chr(cod_l1)}{chr(cod_l2)}{cod_nu}"


    try:
        fil = int(entrada_filas.get())
        col = int(entrada_columnas.get())
        matriz_asientos = []

    

        for i in range(fil):
            matriz_asientos.append([])
            for j in range(col):
                matriz_asientos[i].append(0)

        vuelos.append([codigo, [], [], 0, matriz_asientos, 0])

        construir_confirmacion("Se ha añadido el vuelo de manera exitosa")
    except:
        return construir_error("Ha ocurrido un error, ingrese un número válido")

    guardar_vuelo()
    return 

def asignar_vuelo():
    global vuelos, entrada_origen, entrada_destino, entrada_precio, entrada_codigo, entrada_orden

    orden = entrada_orden.get()

    origen = entrada_origen.get()
    destino = entrada_destino.get()
    precio = int(entrada_precio.get())

    flag_encontrar_codigo = False

    
    for i, vuelo in enumerate(vuelos):
        if str(i+1) == orden:
            vuelo[1] = origen
            vuelo[2] = destino
            vuelo[3] = precio
            flag_encontrar_codigo = True

    if flag_encontrar_codigo == False:
        return construir_error("No se ha encontrado un vuelo que coincida")
    construir_confirmacion("Se ha asignado la información del vuelo")
    guardar_vuelo()
    return


def reservar_asiento():
    global vuelos, entrada_buscar_fila, entrada_buscar_colu, entrada_orden

    orden = entrada_orden.get()
    fila_e = entrada_buscar_fila.get()
    colu_e = int(entrada_buscar_colu.get())

    fila, colu = asiento_a_numeros(fila_e, colu_e)

    flag_entontrar_asiento = False

    for index, vuelo in enumerate(vuelos):
        if str(index+1) == orden:
            try:
                for i, filas in enumerate(vuelo[4]):
                    if fila == i:
                        for j, columnas in enumerate(filas):
                            if colu == j:
                                if vuelo[4][i][j] == 1:
                                    return construir_error("Este asiento ya está ocupado")
                                vuelo[4][i][j] = 1
                                flag_entontrar_asiento = True
                                guardar_vuelo()
            except:
                construir_error("Este vuelo no contiene el asiento buscado")

    if flag_entontrar_asiento == True:
        return construir_confirmacion(f"Se ha asignado el asiento {asiento_a_letras(fila, colu)[0]}{asiento_a_letras(fila, colu)[1]}")
    return construir_error("No se ha encontrado el asiento buscado")


def cancelar_reserva():
    global vuelos, entrada_buscar_fila, entrada_buscar_colu, entrada_orden

    orden = entrada_orden.get()
    fila_e = entrada_buscar_fila.get()
    colu_e = int(entrada_buscar_colu.get())

    fila, colu = asiento_a_numeros(fila_e, colu_e)
    
    flag_entontrar_asiento = False

    for index, vuelo in enumerate(vuelos):
        if str(index+1) == orden:
            try:
                for i, filas in enumerate(vuelo[4]):
                    if fila == i:
                        for j, columnas in enumerate(filas):
                            if colu == j:
                                if vuelo[4][i][j] == 0:
                                    return construir_error("Este asiento no está ocupado")
                                vuelo[4][i][j] = 0
                                flag_entontrar_asiento = True
                                guardar_vuelo()
            except:
                construir_error("Este vuelo no contiene el asiento buscado")

    if flag_entontrar_asiento == True:
        return construir_confirmacion(f"Se ha cancelado la reserva del asiento {asiento_a_letras(fila, colu)[0]}{asiento_a_letras(fila, colu)[1]}")
    return construir_error("No se ha encontrado el asiento buscado")


def mostrar_estadisticas_ocupacion():
    global vuelos, entrada_orden

    orden = entrada_orden.get()

    for index, vuelo in enumerate(vuelos):
        if str(index+1) == orden:
            try:
                total = asientos_totales(vuelo[0])
                cont = asientos_ocupados(vuelo[0])
                        
                porc = 100/(total/cont)

                return f"Vuelo {orden} - {vuelo[0]}, {vuelo[1]} → {vuelo[2]}\nAsientos totales: {total}\nReservados: {cont}\nPorcentaje de ocupación: {porc}%"
                        
            except:
                construir_error("Este vuelo no contiene el asiento buscado")

def mostrar_estadisticas_recaudacion():
    global vuelos, entrada_orden

    orden = entrada_orden.get()

    for index, vuelo in enumerate(vuelos):
        if str(index+1) == orden:
            try:
                cont = asientos_ocupados(vuelo[0])
                total = asientos_totales(vuelo[0])
                        
                recaudacion = cont*vuelo[3]
                return f"Vuelo {orden} - {vuelo[0]}, {vuelo[1]} → {vuelo[2]}\nAsientos totales: {total}\nReservados: {cont}\nCantidad recaudada: ${recaudacion}"
                        
            except:
                construir_error("Este vuelo no contiene el asiento buscado")

def generar_texto_vuelos():
    global vuelos

    texto = '--- Vuelos Disponibles ---\n'

    for i, vuelo in enumerate(vuelos):
        texto += f"Vuelo {i+1} - {vuelo[0]}. {vuelo[1]} → {vuelo[2]}\nPrecio: {vuelo[3]}\nAsiento disponibles: {asientos_disponibles(vuelo[0])}\n\n"

    return texto


def venta_consecutiva():
    global vuelos, entrada_orden, entrada_buscar_fila, entrada_buscar_colu, entrada_asiento_1, entrada_asiento_2

    orden = entrada_orden.get()
    asiento_fila_1 = entrada_fila_asiento_1.get()
    asiento_fila_2 = entrada_fila_asiento_2.get()
    asiento_colu_1 = int(entrada_colu_asiento_1.get())
    asiento_colu_2 = int(entrada_colu_asiento_2.get())

    asiento_fila_1, asiento_colu_1 = asiento_a_numeros(asiento_fila_1, asiento_colu_1)
    asiento_fila_2, asiento_colu_2 = asiento_a_numeros(asiento_fila_2, asiento_colu_2)

    activar_reserva = False

    for index, vuelo in enumerate(vuelos):
        if str(index+1) == orden:
            try:
                for i, fila in enumerate(vuelo[4]):
                    for j, colu in enumerate(vuelo[4][0]):
                        if ((i,j) == (asiento_fila_1, asiento_colu_1)) or activar_reserva == True:
                            activar_reserva = True
                            vuelo[4][i][j] = 1
                        if (i,j) == (asiento_fila_2, asiento_colu_2):
                            construir_confirmacion("Se han guardado los asiento con éxito")
                            guardar_vuelo()
                            return
            except:
                return construir_error("No se han encontrado los asientos buscados")
    return construir_error("No se ha encontrado el vuelo")


def simular_venta_masiva():
    global vuelos, entrada_porcentaje

    porcentaje = int(entrada_porcentaje.get())

    for index, vuelo in enumerate(vuelos):
        a_totales = asientos_totales(vuelo[0])
        a_ocupados = asientos_ocupados(vuelo[0])

        a_requeridos = (a_totales*porcentaje)/100
        meta = a_requeridos - a_ocupados

        for i in range(len(vuelo[4])):
            for j in range(len(vuelo[4][0])):
                if meta >= 0:
                    if vuelo[4][i][j] == 0:
                        vuelo[4][i][j] = 1
                        meta -= 1
    
    construir_confirmacion("Se ha hecho la venta con éxito")
    guardar_vuelo()

    
def reiniciar_vuelos():
    global vuelos

    vuelos = []
    guardar_vuelo()

    construir_confirmacion("Se han reestablecido los vuelos")


cargar_vuelos()


# cargar datos

# construir IU
def construir_crear_vuelo():
    global root, entrada_filas, entrada_columnas
    win = tk.Toplevel(root)
    win.geometry("400x300")
    win.title("Menú crear vuelo")

    contenedor = tk.Frame(win)
    contenedor.pack(fill="both", expand=False, padx=10, pady=10)
    panel = tk.Frame(contenedor)
    panel.pack(fill="y", padx=(0,10))

    tk.Label(panel, text="Ingrese la cantidad de filas del avión").pack(anchor="w", pady=10)
    entrada_filas = tk.Entry(panel, width=25); entrada_filas.pack(anchor="w", pady=10)
    tk.Label(panel, text="Ingrese la cantidad de columnas del avión").pack(anchor="w", pady=10)
    entrada_columnas = tk.Entry(panel, width=25); entrada_columnas.pack(anchor="w", pady=10)


    tk.Button(panel, text="Aceptar", command=crear_vuelo, font=("Arial", 10, "bold"), fg="black", bg="#ffffff").pack(anchor='se')
    tk.Button(panel, text="Cerrar", command=win.destroy, font=("Arial", 10, "bold"), fg="white", bg="#ff0000").pack(anchor='se', pady=20)


def construir_asignar_vuelo():
    global root, entrada_precio, entrada_destino, entrada_origen, entrada_codigo, entrada_orden
    win = tk.Toplevel(root)
    win.geometry("400x500")
    win.title("Menú asignar vuelo")

    contenedor = tk.Frame(win)
    contenedor.pack(fill="both", expand=False, padx=10, pady=10)
    panel = tk.Frame(contenedor)
    panel.pack(fill="y", padx=(0,10))

    tk.Label(panel, text="Ingrese el número del vuelo que quiera asignar valores").pack(anchor="w", pady=10)
    entrada_orden = tk.Entry(panel, width=25); entrada_orden.pack(anchor="w", pady=10)
    tk.Label(panel, text="Ingrese el precio de los boletos del avión").pack(anchor="w", pady=10)
    entrada_precio = tk.Entry(panel, width=25); entrada_precio.pack(anchor="w", pady=10)
    tk.Label(panel, text="Ingrese el punto de origen del vuelo").pack(anchor="w", pady=10)
    entrada_origen = tk.Entry(panel, width=25); entrada_origen.pack(anchor="w", pady=10)
    tk.Label(panel, text="Ingrese el punto de destino del vuelo").pack(anchor="w", pady=10)
    entrada_destino = tk.Entry(panel, width=25); entrada_destino.pack(anchor="w", pady=10)

    tk.Button(panel, text="Aceptar", command=asignar_vuelo, font=("Arial", 10, "bold"), fg="black", bg="#ffffff").pack(anchor='se')
    tk.Button(panel, text="Cerrar", command=win.destroy, font=("Arial", 10, "bold"), fg="white", bg="#ff0000").pack(anchor='se', pady=20)

def construir_mostrar_vuelo():
    global root, entrada_orden, vuelos
    win = tk.Toplevel(root)
    win.title("Menú mostrar vuelo")

    contenedor = tk.Frame(win)
    contenedor.pack(fill="both", expand=False, padx=10, pady=10)
    panel = tk.Frame(contenedor)
    panel.pack(fill="y", padx=(0,10))

    orden = entrada_orden.get()

    flag_encontrar_orden = False
    lista_ocupados = []
    character = 65

    for index, vuelo in enumerate(vuelos):
        if str(index+1) == orden:
            flag_encontrar_orden = True
            codigo = vuelo[0]
            fila_pack =[]
            tk.Label(panel, text=f"Código del vuelo: {vuelo[0]}", font=("Arial", 11)).pack(anchor='w', pady=8)

            for i, fila in enumerate(vuelo[4]):
                fila_pack = [chr(character)]
                for j, elemento in enumerate(fila):
                    if elemento == 1:
                        fila_pack.append("⦿")
                        lista_ocupados.append(asiento_a_letras(i,j))
                    else:
                        fila_pack.append("◯")
                character+=1
                tk.Label(panel, text=fila_pack, font=("Arial", 11)).pack(anchor='w', pady=2)

    if flag_encontrar_orden == False:
            tk.Label(panel, text=f"No se han encontrado vuelos en la posición {orden}\nVerifiaca tu entrada y prueba con otra", font=("Arial", 11)).pack(anchor='w', pady=8)
    else:
        a_totales = asientos_totales(codigo)
        a_ocupados = asientos_ocupados(codigo)
        tk.Label(panel, text=f"Asientos totales: {a_totales}\nAsientos ocupados: {a_ocupados}\nPorcentaje de ocupación: {(a_ocupados*100)/a_totales}", font=("Arial", 11)).pack(anchor='w', pady=8)

        # if not lista_ocupados == []:
            # tk.Label(panel, text=f"Asientos ocupados: {[elem for elem in lista_ocupados]}", font=("Arial", 11)).pack(anchor='w', pady=8)

    tk.Button(panel, text="Cerrar", command=win.destroy, font=("Arial", 10, "bold"), fg="white", bg="#ff0000").pack(anchor='se', pady=20)


def construir_elegir_mostrar():
    global root, entrada_orden
    win = tk.Toplevel(root)
    win.geometry("400x200")
    win.title("Menú elegir vuelo")

    contenedor = tk.Frame(win)
    contenedor.pack(fill="both", expand=False, padx=10, pady=10)
    panel = tk.Frame(contenedor)
    panel.pack(fill="y", padx=(0,10))

    tk.Label(panel, text="Ingrese el número del vuelo que quiera consultar").pack(anchor="w", pady=10)
    entrada_orden = tk.Entry(panel, width=25); entrada_orden.pack(anchor="w", pady=10)

    tk.Button(panel, text="Aceptar", command=construir_mostrar_vuelo, font=("Arial", 10, "bold"), fg="black", bg="#ffffff").pack(anchor='se')
    tk.Button(panel, text="Cerrar", command=win.destroy, font=("Arial", 10, "bold"), fg="white", bg="#ff0000").pack(anchor='se', pady=20)


def construir_reservar_asiento():
    global root, entrada_orden, entrada_buscar_colu, entrada_buscar_fila
    win = tk.Toplevel(root)
    win.title("Menú reservar asiento")

    contenedor = tk.Frame(win)
    contenedor.pack(fill="both", expand=False, padx=10, pady=10)
    panel = tk.Frame(contenedor)
    panel.pack(fill="y", padx=(0,10))

    tk.Label(panel, text="Ingrese el número del vuelo que quiera abordar").pack(anchor="w", pady=10)
    entrada_orden = tk.Entry(panel, width=25); entrada_orden.pack(anchor="w", pady=10)
    tk.Label(panel, text="Ingrese el número de la fila del asiento").pack(anchor="w", pady=10)
    entrada_buscar_fila = tk.Entry(panel, width=25); entrada_buscar_fila.pack(anchor="w", pady=10);entrada_buscar_fila.insert(0, 'A')
    tk.Label(panel, text="Ingrese el número de la columna del asiento").pack(anchor="w", pady=10)
    entrada_buscar_colu = tk.Entry(panel, width=25); entrada_buscar_colu.pack(anchor="w", pady=10);entrada_buscar_colu.insert(0, '1')

    tk.Button(panel, text="Aceptar", command=reservar_asiento, font=("Arial", 10, "bold"), fg="black", bg="#ffffff").pack(anchor='se')
    tk.Button(panel, text="Cerrar", command=win.destroy, font=("Arial", 10, "bold"), fg="white", bg="#ff0000").pack(anchor='se', pady=20)

def construir_cancelar_reservar():
    global root, entrada_orden, entrada_buscar_colu, entrada_buscar_fila
    win = tk.Toplevel(root)
    win.title("Menú cancelar reserva")

    contenedor = tk.Frame(win)
    contenedor.pack(fill="both", expand=False, padx=10, pady=10)
    panel = tk.Frame(contenedor)
    panel.pack(fill="y", padx=(0,10))

    tk.Label(panel, text="Ingrese el número del vuelo que quiera cancelar la reserva\nSiga el ejemplo").pack(anchor="w", pady=10)
    entrada_orden = tk.Entry(panel, width=25); entrada_orden.pack(anchor="w", pady=10)
    tk.Label(panel, text="Ingrese la letra de la fila del asiento").pack(anchor="w", pady=10)
    entrada_buscar_fila = tk.Entry(panel, width=25); entrada_buscar_fila.pack(anchor="w", pady=10);entrada_buscar_fila.insert(0, 'A')
    tk.Label(panel, text="Ingrese el número de la columna del asiento").pack(anchor="w", pady=10)
    entrada_buscar_colu = tk.Entry(panel, width=25); entrada_buscar_colu.pack(anchor="w", pady=10);entrada_buscar_colu.insert(0, '1')

    tk.Button(panel, text="Aceptar", command=cancelar_reserva, font=("Arial", 10, "bold"), fg="black", bg="#ffffff").pack(anchor='se')
    tk.Button(panel, text="Cerrar", command=win.destroy, font=("Arial", 10, "bold"), fg="white", bg="#ff0000").pack(anchor='se', pady=20)


def construir_mostrar_estadisticas_ocupacion():
    global root
    win = tk.Toplevel(root)
    win.title("Mostrar estadísticas ocupación")

    contenedor = tk.Frame(win)
    contenedor.pack(fill="both", expand=False, padx=10, pady=10)
    panel = tk.Frame(contenedor)
    panel.pack(fill="y", padx=(0,10))

    texto = mostrar_estadisticas_ocupacion()
    tk.Label(panel, text=texto, font=("Arial", 11)).pack(anchor="w", padx=60, pady=10)

    tk.Button(panel, text="Cerrar", command=win.destroy, font=("Arial", 10, "bold"), fg="white", bg="#ff0000").pack(anchor='se', pady=20)


def construir_estadísticas_ocupacion():
    global root, entrada_orden
    win = tk.Toplevel(root)
    win.title("Menú estadísticas ocupación")

    contenedor = tk.Frame(win)
    contenedor.pack(fill="both", expand=False, padx=10, pady=10)
    panel = tk.Frame(contenedor)
    panel.pack(fill="y", padx=(0,10))

    tk.Label(panel, text='Ingrese el número del vuelo del que quiera saber su estadística de ocupación', font=("Arial", 11)).pack(anchor="w", pady=10)
    entrada_orden = tk.Entry(panel, width=25); entrada_orden.pack(anchor="w", pady=10)

    tk.Button(panel, text="Aceptar", command=construir_mostrar_estadisticas_ocupacion, font=("Arial", 10, "bold"), fg="black", bg="#ffffff").pack(anchor='se')

    tk.Button(panel, text="Cerrar", command=win.destroy, font=("Arial", 10, "bold"), fg="white", bg="#ff0000").pack(anchor='se', pady=20)

def construir_mostrar_estadisticas_recaudacion():
    global root
    win = tk.Toplevel(root)
    win.title("Mostrar estadísticas recaudación")

    contenedor = tk.Frame(win)
    contenedor.pack(fill="both", expand=False, padx=10, pady=10)
    panel = tk.Frame(contenedor)
    panel.pack(fill="y", padx=(0,10))

    texto = mostrar_estadisticas_recaudacion()
    tk.Label(panel, text=texto, font=("Arial", 11)).pack(anchor="w", padx=60, pady=10)

    tk.Button(panel, text="Cerrar", command=win.destroy, font=("Arial", 10, "bold"), fg="white", bg="#ff0000").pack(anchor='se', pady=20)

def construir_estadísticas_recaudación():
    global root, entrada_orden
    win = tk.Toplevel(root)
    win.title("Menú estadísticas recaudación")

    contenedor = tk.Frame(win)
    contenedor.pack(fill="both", expand=False, padx=10, pady=10)
    panel = tk.Frame(contenedor)
    panel.pack(fill="y", padx=(0,10))

    tk.Label(panel, text='Ingrese el número del vuelo del que quiera saber su estadística de recaudacino', font=("Arial", 11)).pack(anchor="w", pady=10)
    entrada_orden = tk.Entry(panel, width=25); entrada_orden.pack(anchor="w", pady=10)
    tk.Button(panel, text="Aceptar", command=construir_mostrar_estadisticas_recaudacion, font=("Arial", 10, "bold"), fg="black", bg="#ffffff").pack(anchor='se')


    tk.Button(panel, text="Cerrar", command=win.destroy, font=("Arial", 10, "bold"), fg="white", bg="#ff0000").pack(anchor='se', pady=20)



def construir_mostrar_por_destino():
    global root, vuelos, entrada_destino
    win = tk.Toplevel(root)
    win.title("Mostrar vuelos por destino")

    contenedor = tk.Frame(win)
    contenedor.pack(fill="both", expand=False, padx=10, pady=10)
    panel = tk.Frame(contenedor)
    panel.pack(fill="y", padx=(0,10))

    destino = entrada_destino.get()
    texto = ''
    total = 0
    cont = 0

    for i, vuelo in enumerate(vuelos):
        if vuelo[2] == destino:

            for fila in vuelo[4]:
                for asiento in fila:
                    if asiento == 1:
                        cont += 1
                    total += 1

            texto += f"- Vuelo: {i+1} (asientos disponibles {total - cont})\n"

    if texto == '':
        texto = "No se han encontado vuelos que coincidan con este destino"


    tk.Label(panel, text=texto, font=("Arial", 11)).pack(anchor="w", padx=60, pady=10)

    tk.Button(panel, text="Cerrar", command=win.destroy, font=("Arial", 10, "bold"), fg="white", bg="#ff0000").pack(anchor='se', pady=20)

def construir_buscar_por_destino():
    global root, entrada_destino
    win = tk.Toplevel(root)
    win.title("Menú vuelos por destino")

    contenedor = tk.Frame(win)
    contenedor.pack(fill="both", expand=False, padx=10, pady=10)
    panel = tk.Frame(contenedor)
    panel.pack(fill="y", padx=(0,10))

    tk.Label(panel, text='Ingrese el número del vuelo del que quiera saber su estadística de recaudacino', font=("Arial", 11)).pack(anchor="w", pady=10)
    entrada_destino = tk.Entry(panel, width=25); entrada_destino.pack(anchor="w", pady=10)
    tk.Button(panel, text="Aceptar", command=construir_mostrar_por_destino, font=("Arial", 10, "bold"), fg="black", bg="#ffffff").pack(anchor='se')

    tk.Button(panel, text="Cerrar", command=win.destroy, font=("Arial", 10, "bold"), fg="white", bg="#ff0000").pack(anchor='w', pady=20)


def construir_mostrar_vuelos_disponibles():
    global root
    win = tk.Toplevel(root)
    win.title("Mostrar vuelos disponibles")

    contenedor = tk.Frame(win)
    contenedor.pack(fill="both", expand=False, padx=10, pady=10)
    
    panel_izq = tk.Frame(contenedor)
    panel_izq.pack(side='left', fill="both", padx=(0,10))
    panel_der = tk.Frame(contenedor)
    panel_der.pack(side='right', fill="both", padx=(0,10))
    
    texto = ''

    for i, vuelo in enumerate(vuelos):
        if not vuelo[3] == 0:
            panel = panel_izq if i % 2 == 0 else panel_der
            texto = f"Vuelo {i+1} - {vuelo[0]}. {vuelo[1]} → {vuelo[2]}\nPrecio: {vuelo[3]}\nAsiento disponibles: {asientos_disponibles(vuelo[0])}\n\n"
        
            tk.Label(panel, text=texto, justify="left", font=("Arial", 10)).pack(anchor='w', pady=5)
    
    tk.Button(panel_der, text="Cerrar", command=win.destroy, font=("Arial", 10, "bold"), fg="white", bg="#ff0000").pack(anchor='se', pady=10)


def construir_reservar_varios():
    global root, entrada_orden, entrada_fila_asiento_1, entrada_colu_asiento_1, entrada_fila_asiento_2, entrada_colu_asiento_2
    win = tk.Toplevel(root)
    win.title("Menú reservar asientos consecutivos")

    contenedor = tk.Frame(win)
    contenedor.pack(fill="both", expand=False, padx=10, pady=10)
    panel = tk.Frame(contenedor)
    panel.pack(fill="y", padx=(0,10))

    tk.Label(panel, text='Ingrese el vuelo y las letras y números de los\nasientos consecutivos que desea reservar, siga el ejemplo', font=("Arial", 11)).pack(anchor="w", pady=10)
    entrada_orden = tk.Entry(panel, width=25); entrada_orden.pack(anchor="w", pady=10); entrada_orden.insert(0, '2')
    entrada_fila_asiento_1 = tk.Entry(panel, width=25); entrada_fila_asiento_1.pack(anchor="w", pady=10); entrada_fila_asiento_1.insert(0, 'A')
    entrada_colu_asiento_1 = tk.Entry(panel, width=25); entrada_colu_asiento_1.pack(anchor="w", pady=10); entrada_colu_asiento_1.insert(0, '1')
    entrada_fila_asiento_2 = tk.Entry(panel, width=25); entrada_fila_asiento_2.pack(anchor="w", pady=10); entrada_fila_asiento_2.insert(0, 'B')
    entrada_colu_asiento_2 = tk.Entry(panel, width=25); entrada_colu_asiento_2.pack(anchor="w", pady=10); entrada_colu_asiento_2.insert(0, '4')

    tk.Button(panel, text="Aceptar", command=venta_consecutiva, font=("Arial", 10, "bold"), fg="black", bg="#ffffff").pack(anchor='se')

    tk.Button(panel, text="Cerrar", command=win.destroy, font=("Arial", 10, "bold"), fg="white", bg="#ff0000").pack(anchor='w', pady=20)


def construir_venta_masiva():
    global root, entrada_porcentaje
    win = tk.Toplevel(root)
    win.title("Menú venta masiva")

    contenedor = tk.Frame(win)
    contenedor.pack(fill="both", expand=False, padx=10, pady=10)
    panel = tk.Frame(contenedor)
    panel.pack(fill="y", padx=(0,10))

    tk.Label(panel, text='Ingrese el porcentaje de asientos que quiera reservar', font=("Arial", 11)).pack(anchor="w", pady=10)
    entrada_porcentaje = tk.Entry(panel, width=25); entrada_porcentaje.pack(anchor="w", pady=10)

    tk.Button(panel, text="Aceptar", command=simular_venta_masiva, font=("Arial", 10, "bold"), fg="black", bg="#ffffff").pack(anchor='se')

    tk.Button(panel, text="Cerrar", command=win.destroy, font=("Arial", 10, "bold"), fg="white", bg="#ff0000").pack(anchor='se', pady=20)



def construir_menu():
    global root
    
    root = tk.Tk()
    # root.geometry("400x560")
    root.title("Menú de opciones")
    
    contenedor = tk.Frame(root)
    contenedor.pack(fill="both", expand=True)
    panel = tk.Label(contenedor, font=("Arial", 20, "bold"))
    panel.pack(fill="x", padx=10, pady=20), 
    panel_izq = tk.Frame(contenedor)
    panel_izq.pack(side="left", fill="both", padx=(0,10))
    panel_der = tk.Frame(contenedor)
    panel_der.pack(side="left", fill="both", padx=(0,10))
    
    
    tk.Label(panel, text='Bienvenid@ al sistema\nde reservas de vuelos', font=("Arial", 16, "bold")).pack(anchor='w')
    tk.Label(panel, text='Seleccione su opción:', font=("Arial", 13, "bold")).pack(anchor='w')
    tk.Button(panel_izq,text='Crear nuevo vuelo', command=construir_crear_vuelo, width=tamano_botones[0], height=tamano_botones[1], bg="#badaff").pack(anchor='w', padx=10, pady=10)
    tk.Button(panel_der,text='Asignar vuelo', command=construir_asignar_vuelo, width=tamano_botones[0], height=tamano_botones[1], bg="#badaff").pack(anchor='w', padx=10, pady=10)
    tk.Button(panel_izq,text='Mostrar vuelo', command=construir_elegir_mostrar, width=tamano_botones[0], height=tamano_botones[1], bg="#ff9eea").pack(anchor='w', padx=10, pady=10)
    tk.Button(panel_der,text='Reservar asiento', command=construir_reservar_asiento, width=tamano_botones[0], height=tamano_botones[1], bg="#e7aaff").pack(anchor='w', padx=10, pady=10)
    tk.Button(panel_izq,text='Estadísticas de ocupación', command=construir_estadísticas_ocupacion, width=tamano_botones[0], height=tamano_botones[1], bg="#ffd4a2").pack(anchor='w', padx=10, pady=10)
    tk.Button(panel_izq,text='Estadísticas de recaudacion', command=construir_estadísticas_recaudación, width=tamano_botones[0], height=tamano_botones[1], bg="#ffd4a2").pack(anchor='w', padx=10, pady=10)
    tk.Button(panel_der,text='Cancelar reserva', command=construir_cancelar_reservar, width=tamano_botones[0], height=tamano_botones[1], bg="#e7aaff").pack(anchor='w', padx=10, pady=10)
    tk.Button(panel_der,text='Buscar por destino', command=construir_buscar_por_destino, width=tamano_botones[0], height=tamano_botones[1], bg="#fffd9e").pack(anchor='w', padx=10, pady=10)
    tk.Button(panel_izq,text='Mostrar vuelos disponibles', command=construir_mostrar_vuelos_disponibles, width=tamano_botones[0], height=tamano_botones[1], bg="#fffd9e").pack(anchor='w', padx=10, pady=10)
    tk.Button(panel_der,text='Reservar varios\nasientos consecutivos', command=construir_reservar_varios, width=tamano_botones[0], height=tamano_botones[1], bg="#afff8f").pack(anchor='w', padx=10, pady=10)
    tk.Button(panel_izq,text='Simular venta masiva', command=construir_venta_masiva, width=tamano_botones[0], height=tamano_botones[1], bg="#afff8f").pack(anchor='w', padx=10, pady=10)
    tk.Button(panel_der,text='Reiniciar vuelos', command=reiniciar_vuelos, width=tamano_botones[0], height=tamano_botones[1], bg="#ff8282", font=("Arial", 9, "bold")).pack(anchor='w', padx=10, pady=10)

    tk.Button(panel_der, text="Cerrar programa", command=root.destroy, font=("Arial", 10, "bold"), fg="white", bg="#ff0000", padx=10, pady=6).pack(anchor='se', pady=10)

    root.mainloop()
    
# activa la ventana principal (menú)
if __name__ == "__main__":
    construir_menu()

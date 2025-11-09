import tkinter as tk
import random, json

# lista de vuelos [[código, origen, destino, preocio, matriz de asientos, vendidos],[...],[...]]
vuelos = []

root = None
entrada_origen = entrada_destino = entrada_precio = entrada_filas = entrada_columnas = entrada_codigo = entrada_orden =  entrada_buscar_fila = entrada_buscar_colu = None
tamano_botones = (20, 2)

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



# funciones del programa

def crear_vuelo():
    global vuelos, entrada_precio, entrada_columnas, entrada_filas, entrada_origen, entrada_destino

    cod_l1 = random.randint(65,90)
    cod_l2 = random.randint(65,90)
    cod_nu = random.randint(0, 999)
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
    precio = entrada_precio.get()

    flag_encontrar_codigo = False

    for i, vuelo in enumerate(vuelos):
        if str(i+1) == orden:
            vuelo[1].append(origen)
            vuelo[2].append(destino)
            vuelo[3] = precio
            flag_encontrar_codigo = True


    if flag_encontrar_codigo == True:
        construir_confirmacion("Se ha asignado la información del vuelo")
        guardar_vuelo()
    else:
        construir_error("No se ha encontrado un vuelo que coincida")
    return


def reservar_asiento():
    global vuelos, entrada_buscar_fila, entrada_buscar_colu, entrada_orden

    orden = entrada_orden.get()
    fila = entrada_buscar_fila.get()
    colu = entrada_buscar_colu.get()

    for index, vuelo in enumerate(vuelos):
        if str(index+1) == orden:
            try:
                for i, filas in enumerate(vuelo[4]):
                    if fila == str(i+1):
                        for j, columnas in enumerate(filas):
                            if colu == str(j+1):
                                vuelo[4][i][j] = 1
                                guardar_vuelo()
            except:
                construir_error("Este vuelo no contiene el asiento buscado")


def cancelar_reserva():
    global vuelos, entrada_buscar_fila, entrada_buscar_colu, entrada_orden

    orden = entrada_orden.get()
    fila = entrada_buscar_fila.get()
    colu = entrada_buscar_colu.get()

    for index, vuelo in enumerate(vuelos):
        if str(index+1) == orden:
            try:
                for i, filas in enumerate(vuelo[4]):
                    if fila == str(i+1):
                        for j, columnas in enumerate(filas):
                            if colu == str(j+1):
                                vuelo[4][i][j] = 0
                                guardar_vuelo()
            except:
                construir_error("Este vuelo no contiene el asiento buscado")


def mostrar_estadisticas():
    global vuelos, entrada_orden

    orden = entrada_orden.get()
    total = 0
    cont = 0

    for index, vuelo in enumerate(vuelos):
        if str(index+1) == orden:
            try:
                for filas in vuelo[4]:
                    for elem in filas:
                        if not elem == 0:
                            cont += 1
                        total += 1
                        

                porc = 100//(total//cont)

                return f"Vuelo {orden} - {vuelo[0]}, {vuelo[1]} → {vuelo[2]}\nAsientos totales: {total}\nReservados: {cont}\nPorcentaje de ocupación: {porc}%"
                        
            except:
                construir_error("Este vuelo no contiene el asiento buscado")

    

cargar_vuelos()


# cargar datos

# construir IU
def construir_crear_vuelo():
    global root, entrada_filas, entrada_columnas
    win = tk.Toplevel(root)
    win.geometry("400x300")
    win.title("Menú pricipal")

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
    win.title("Menú pricipal")

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
    # win.geometry("400x300")
    win.title("Menú pricipal")

    contenedor = tk.Frame(win)
    contenedor.pack(fill="both", expand=False, padx=10, pady=10)
    panel = tk.Frame(contenedor)
    panel.pack(fill="y", padx=(0,10))

    orden = entrada_orden.get()

    flag_encontrar_orden = False

    for i, vuelo in enumerate(vuelos):
        if str(i+1) == orden:
            flag_encontrar_orden = True
            tk.Label(panel, text=f"Código del vuelo: {vuelo[0]}", font=("Arial", 11)).pack(anchor='w', pady=8)
            for fila in vuelo[4]:
                fila_pack = []
                for elemento in fila:
                    if elemento == 1:
                        fila_pack.append("⦿")
                    else:
                        fila_pack.append("◯")
                tk.Label(panel, text=fila_pack, font=("Arial", 11)).pack(anchor='w', pady=2)

    if flag_encontrar_orden == False:
            tk.Label(panel, text=f"No se han encontrado vuelos en la posición {orden}\nVerifiaca tu entrada y prueba con otra", font=("Arial", 11)).pack(anchor='w', pady=8)
        

    tk.Button(panel, text="Cerrar", command=win.destroy, font=("Arial", 10, "bold"), fg="white", bg="#ff0000").pack(anchor='se', pady=20)


def construir_elegir_mostrar():
    global root, entrada_orden
    win = tk.Toplevel(root)
    win.geometry("400x200")
    win.title("Mostrar vuelo")

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
    win.title("Mostrar vuelo")

    contenedor = tk.Frame(win)
    contenedor.pack(fill="both", expand=False, padx=10, pady=10)
    panel = tk.Frame(contenedor)
    panel.pack(fill="y", padx=(0,10))

    tk.Label(panel, text="Ingrese el número del vuelo que quiera abordar").pack(anchor="w", pady=10)
    entrada_orden = tk.Entry(panel, width=25); entrada_orden.pack(anchor="w", pady=10)
    tk.Label(panel, text="Ingrese el número de la fila del asiento").pack(anchor="w", pady=10)
    entrada_buscar_fila = tk.Entry(panel, width=25); entrada_buscar_fila.pack(anchor="w", pady=10)
    tk.Label(panel, text="Ingrese el número de la columna del asiento").pack(anchor="w", pady=10)
    entrada_buscar_colu = tk.Entry(panel, width=25); entrada_buscar_colu.pack(anchor="w", pady=10)

    tk.Button(panel, text="Aceptar", command=reservar_asiento, font=("Arial", 10, "bold"), fg="black", bg="#ffffff").pack(anchor='se')
    tk.Button(panel, text="Cerrar", command=win.destroy, font=("Arial", 10, "bold"), fg="white", bg="#ff0000").pack(anchor='se', pady=20)

def construir_cancelar_reservar():
    global root, entrada_orden, entrada_buscar_colu, entrada_buscar_fila
    win = tk.Toplevel(root)
    win.title("Mostrar vuelo")

    contenedor = tk.Frame(win)
    contenedor.pack(fill="both", expand=False, padx=10, pady=10)
    panel = tk.Frame(contenedor)
    panel.pack(fill="y", padx=(0,10))

    tk.Label(panel, text="Ingrese el número del vuelo que quiera cancelar la reserva").pack(anchor="w", pady=10)
    entrada_orden = tk.Entry(panel, width=25); entrada_orden.pack(anchor="w", pady=10)
    tk.Label(panel, text="Ingrese el número de la fila del asiento").pack(anchor="w", pady=10)
    entrada_buscar_fila = tk.Entry(panel, width=25); entrada_buscar_fila.pack(anchor="w", pady=10)
    tk.Label(panel, text="Ingrese el número de la columna del asiento").pack(anchor="w", pady=10)
    entrada_buscar_colu = tk.Entry(panel, width=25); entrada_buscar_colu.pack(anchor="w", pady=10)

    tk.Button(panel, text="Aceptar", command=cancelar_reserva, font=("Arial", 10, "bold"), fg="black", bg="#ffffff").pack(anchor='se')
    tk.Button(panel, text="Cerrar", command=win.destroy, font=("Arial", 10, "bold"), fg="white", bg="#ff0000").pack(anchor='se', pady=20)


def construir_mostrar_estadisticas():
    global root
    win = tk.Toplevel(root)
    win.title("Mostrar vuelo")

    contenedor = tk.Frame(win)
    contenedor.pack(fill="both", expand=False, padx=10, pady=10)
    panel = tk.Frame(contenedor)
    panel.pack(fill="y", padx=(0,10))

    texto = mostrar_estadisticas()
    tk.Label(panel, text=texto, font=("Arial", 11)).pack(anchor="w", padx=60, pady=10)

    tk.Button(panel, text="Cerrar", command=win.destroy, font=("Arial", 10, "bold"), fg="white", bg="#ff0000").pack(anchor='se', pady=20)


def construir_estadísticas_ocupacion():
    global root, entrada_orden
    win = tk.Toplevel(root)
    win.title("Mostrar vuelo")

    contenedor = tk.Frame(win)
    contenedor.pack(fill="both", expand=False, padx=10, pady=10)
    panel = tk.Frame(contenedor)
    panel.pack(fill="y", padx=(0,10))

    tk.Label(panel, text='Ingrese el número del vuelo del que quiera saber su estadística de ocupación', font=("Arial", 11)).pack(anchor="w", pady=10)
    entrada_orden = tk.Entry(panel, width=25); entrada_orden.pack(anchor="w", pady=10)
    tk.Button(panel, text="Aceptar", command=construir_mostrar_estadisticas, font=("Arial", 10, "bold"), fg="black", bg="#ffffff").pack(anchor='se')


    tk.Button(panel, text="Cerrar", command=win.destroy, font=("Arial", 10, "bold"), fg="white", bg="#ff0000").pack(anchor='se', pady=20)


def construir_menu():
    global root
    
    root = tk.Tk()
    root.geometry("400x560")
    root.title("Menu de opciones")
    
    contenedor = tk.Frame(root)
    contenedor.pack(fill="both", expand=True)
    panel = tk.Label(contenedor, font=("Arial", 20, "bold"))
    panel.pack(fill="x", padx=10, pady=20), 
    panel_izq = tk.Frame(contenedor)
    panel_izq.pack(side="left", fill="both", padx=(0,10))
    panel_der = tk.Frame(contenedor)
    panel_der.pack(side="left", fill="both", padx=(0,10))
    
    
    tk.Label(panel, text='Seleccione su opción:', font=("Arial", 16, "bold")).pack(anchor='w', pady=12,)
    tk.Button(panel_izq,text='Crear nuevo vuelo', command=construir_crear_vuelo, width=tamano_botones[0], height=tamano_botones[1], bg="#badaff").pack(anchor='w', padx=10, pady=10)
    tk.Button(panel_der,text='Asignar vuelo', command=construir_asignar_vuelo, width=tamano_botones[0], height=tamano_botones[1], bg="#badaff").pack(anchor='w', padx=10, pady=10)
    tk.Button(panel_izq,text='Mostrar vuelo', command=construir_elegir_mostrar, width=tamano_botones[0], height=tamano_botones[1], bg="#badaff").pack(anchor='w', padx=10, pady=10)
    tk.Button(panel_der,text='Reservar asiento', command=construir_reservar_asiento, width=tamano_botones[0], height=tamano_botones[1], bg="#badaff").pack(anchor='w', padx=10, pady=10)
    tk.Button(panel_izq,text='Estadísticas de ocupación', command=construir_estadísticas_ocupacion, width=tamano_botones[0], height=tamano_botones[1], bg="#badaff").pack(anchor='w', padx=10, pady=10)
    tk.Button(panel_der,text='Cancelar reserva', command=construir_cancelar_reservar, width=tamano_botones[0], height=tamano_botones[1], bg="#badaff").pack(anchor='w', padx=10, pady=10)

    tk.Button(panel_der, text="Cerrar", command=root.destroy, font=("Arial", 10, "bold"), fg="white", bg="#ff0000").pack(anchor='se', pady=20)

    root.mainloop()
    
# activa la ventana principal (menú)
if __name__ == "__main__":
    construir_menu()

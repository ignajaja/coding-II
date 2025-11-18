# imports
import threading, queue, random, time, json, os, datetime, uuid
import tkinter as tk
from tkinter import ttk, messagebox


# cargar las configuraciones del archivo
def load_config():
    try:
        with open("config.json", "r") as configs:
            config = json.load(configs)
            return config
    except:
        # -error añadir construir error
        return
    

config = load_config()

# clases
class Pedido:
    def __init__(self, cliente, direccion, peso, tracking = None):
        self.tracking = tracking if tracking else str(uuid.uuid4())
        self.fecha_recibido = datetime.datetime.now()
        self.cliente = cliente
        self.direccion = direccion
        self.peso = peso
        self.estado = "Pendiente"
        self.tiempo_prep = None
        self.dron = None
        self.tiempo_entraga = None
        self.tiempo_preparacion_inicio = None
        self.tiempo_preparacion_final = None
        self.tiempo_entrega_inicio = None
        self.tiempo_entrega_final = None
        self.bitacora = []

    def log(self, evento):
        self.bitacora.append(f"{datetime.datetime.now()} {evento}")


class Direccion:
    def __init__(self, calle, avenida, edificio, piso, apartamento):
        self.calle = calle
        self.avenida = avenida
        self.edificio = edificio
        self.piso = piso
        self.apartamento = apartamento
        
    def __str__(self):
        return f"Calle {self.calle+1}, avenida {self.avenida+1}, edificio {self.edificio+1}, piso {self.piso+1}, apartamento {self.apartamento+1}"


class Ciudad:
    def __init__(self, calles, avenidas): # calles son filas y avenidas son columnas como dice en el archivo
        self.calles = calles
        self.avenidas = avenidas
        self.cuadras = []
        
        for i in range(avenidas):
            cuadra = []
            for j in range(calles):
                tamano_cuadra = random.randint(config["tamano_cuadra_min"], config["tamano_cuadra_max"])*2
                edificios = []
                for k in range(tamano_cuadra):
                    pisos = random.randint(1, config["pisos_max"])
                    edificios.append(pisos)
                cuadra.append(edificios)
            self.cuadras.append(cuadra)

    def get_building_floor(self, calle, avenida, edificio):
        try:
            return self.cuadras[avenida][calle][edificio]
        except:
            messagebox.showerror("Error", "Los datos dados no coinciden con la ciudad")
            return False

ciudad = Ciudad(config["ciudad_calles"], config["ciudad_avenidas"])


pedidos_queue = queue.Queue()
preparados_queue = queue.Queue()

lista_pedidos = []

lock = threading.Lock()

def tiempo_de_preparacion_peso(peso):
    for limite in config["tiempo_prep"].items():
        if peso <= int(limite[0]):
            return limite[1]

class RobotPreparador(threading.Thread):
    def __init__(self, id):
        super().__init__(daemon=True)
        self.id = id
    
    def run(self):
        while True:
            pedido = pedidos_queue.get()
            pedido.estado = "preparando"
            pedido.robot = self.id
            pedido.tiempo_preparacion_inicio = datetime.datetime.now()
            pedido.log("Ininciando preparación")
            tiempo_preparacion = tiempo_de_preparacion_peso(pedido.peso)
            time.sleep(tiempo_preparacion)
            pedido.tiempo_preparacion_final = datetime.datetime.now()
            pedido.tiempo_prep = tiempo_preparacion
            pedido.estado = 'listo'
            pedido.log(f"Pedido listo en {tiempo_preparacion} seg.")
            preparados_queue.put(pedido)
            pedidos_queue.task_done()

robots = [RobotPreparador(i+1) for i in range(config["num_robots"])]

for robot in robots:
    robot.start()

drones = []
drones_libres = queue.Queue()

# la id es la id de cada dron
class Dron(threading.Thread):
    def __init__(self, id):
        super().__init__(daemon=True)
        self.id = id
        self.bateria = 100
        self.pedido_actual = None
        self.funcionando = True
        self.posicion_actual = (1,3)
        self.ruta = []

    def calcular_ruta(self, des_calle, des_aveni):
        ruta = []
        calle_actual, avenida_actual = self.posicion_actual

        while avenida_actual != des_aveni:
            if avenida_actual < des_aveni:
                avenida_actual += 1
            else:
                avenida_actual -= 1
            ruta.append((calle_actual, avenida_actual))

        while calle_actual != des_calle:
            if calle_actual < des_calle:
                calle_actual += 1
            else:
                calle_actual -= 1
            ruta.append((calle_actual, avenida_actual))

        return ruta

    def run(self):
        while self.funcionando:
            pedido = preparados_queue.get()
            pedido.estado = "entregando"
            pedido.dron = self.id
            pedido.tiempo_entrega_inicio = datetime.datetime.now()
            pedido.log(f"Dron entregando")

            direccion = pedido.direccion
            self.ruta = self.calcular_ruta(direccion.calle, direccion.avenida)
            tiempo_ruta = (
                abs(direccion.calle - self.posicion_actual[0]) * config['tiempo_calle'] + abs(direccion.avenida - self.posicion_actual[1]) * config['tiempo_calle']
            )
            pisos = ciudad.get_building_floor(direccion.calle, direccion.avenida, direccion.edificio)
            if pisos == False:
                pedido.log("No se puede entregar el pedido")
                continue

            tiempo_aire = abs(direccion.piso) * config['tiempo_piso']
            tiempo_entrega = tiempo_ruta + tiempo_aire + config['tiempo_puerta']

            if self.bateria < tiempo_entrega:
                pedido.log(f"Dron #{self.id} no tiene batería suficiente")
                self.bateria = 100 # -error corregir método de recarga de dron, revisar documento
                pedido.log(f"Dron #{self.id} recargado")
                preparados_queue.put(pedido)
                preparados_queue.task_done()
                continue
            
            self.pedido_actual = pedido
            tiempo_paso = tiempo_ruta/len(self.ruta) if self.ruta else 0
            for paso in self.ruta:
                self.posicion_actual = paso
                time.sleep(abs(tiempo_paso))
            time.sleep(tiempo_aire + config['tiempo_puerta'])
            self.bateria -= tiempo_entrega # simulando que se descarga 1% por cada segundo
            pedido.tiempo_entrega_final = datetime.datetime.now()
            pedido.tiempo_entrega = tiempo_entrega
            pedido.estado = 'entregado'
            pedido.log(f"Pedido entregado: Dron #{self.id}. Batería inicial{self.bateria+tiempo_entrega}%. Batería final {self.bateria}%")

            self.ruta = self.calcular_ruta(1,3)
            for paso in self.ruta:
                self.posicion_actual = paso
                time.sleep(abs(tiempo_paso))
            self.pedido_actual = None
            self.ruta = []
            preparados_queue.task_done()
            drones_libres.put(self)

            # with lock:
            #     if pedido in lista_pedidos:
            #         lista_pedidos.remove(pedido)

for i in range(config['num_drones']):
    dron = Dron(i+1)
    drones.append(dron)
    drones_libres.put(dron)
    dron.start()



### muy importante, pedidos por archivo
def load_pedido_archivo():

    tiempo = datetime.datetime.now()
    print(tiempo.second)
    if tiempo.second %10 != 0:
        return
    print('intento')
    folder = "./pedidos"

    if not os.path.exists(folder):
        os.makedirs(folder)
    
    historial = set()
    error = False

    
    archivos = [f for f in os.listdir(folder)]
    for archivo in archivos:
        path = os.path.join(folder,archivo)
        if path in historial:
            continue
        try:
            with open(path, 'r') as a:
                try:
                # datos = json.load(a) if archivo.endswith('.json') else eval(a.read())
                    datos = json.load(a)
                    
                except:
                    return
                
            if (datos['avenida'] < 0 or datos['avenida'] >= config['ciudad_avenidas']) or (datos['calle'] < 0 or datos['calle'] >= config['ciudad_calles']):
                    # return messagebox.showerror("Error", "Calles y avenidas ingreseadas son incorrectas") 
                    raise KeyError

            direccion = Direccion(datos["calle"]-1, datos['avenida']-1, datos['edificio']-1, datos['piso']-1, datos['apartamento']-1)
            pedido = Pedido(
                cliente = datos['cliente'],
                direccion = direccion,
                peso = datos['peso'],
                tracking = datos.get('tracking', None)
            )
            with lock:
                lista_pedidos.append(pedido)

            pedidos_queue.put(pedido)
            historial.add(path)

            messagebox.showinfo("Cargando", "Preparando y entregando pedido desde archivo")
            with open(path, "w") as b:
                b.write("")
        except:
            messagebox.showerror("Error", f"Error leyendo pedido de {archivo}")
            error = True
    if error == True:
        return

# threading.Thread(target=load_pedido_archivo, daemon=True).start()

class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Entrega de encargos")
        self.create_widgets()
        self.refrescar_gui()
        
    def create_widgets(self):
        self.mapa_canvas = tk.Canvas(self, width=950, height=600, bg="#cccccc")
        self.mapa_canvas.grid(row=0, column=0, rowspan=6, padx=10, pady=10)

        # Lista de pedidos
        self.tree_orders = ttk.Treeview(self, columns=("Tracking", "Estado", "Cliente", "Direccion"), show='headings')
        self.tree_orders.heading("Tracking", text="Tracking")
        self.tree_orders.heading("Estado", text="Estado")
        self.tree_orders.heading("Cliente", text="Cliente")
        self.tree_orders.heading("Direccion", text="Direccion")
        self.tree_orders.column("Tracking", width=100)
        self.tree_orders.column("Estado", width=100)
        self.tree_orders.column("Cliente", width=100)
        self.tree_orders.column("Direccion", width=200)
        self.tree_orders.grid(row=0, column=1, padx=10, pady=10, sticky="nsew")

        # Drones info
        self.drones_frame = tk.Frame(self, bg="white", relief="solid", borderwidth=1)
        self.drones_frame.grid(row=1, column=1, sticky="nw", padx=10, pady=5)
        tk.Label(self.drones_frame, text=f"Estado de drones", font=("Arial", 10, "bold"), bg="white").pack(pady=1)

        self.drones_labels = []

        for i in range(config["num_drones"]):
            lbl = tk.Label(self.drones_frame, text=f"Dron {i+1}: {dron.bateria}", bg="white", anchor="w")
            lbl.pack(anchor="w", padx=10)
            self.drones_labels.append(lbl)

        # Pedido tracker (detalles por pedido seleccionado)
        tracker_frame = tk.Frame(self, bg="white")
        tracker_frame.grid(row=2, column=1)
        self.tracker_label = tk.Label(self, text="Tracker / Bitácora Pedido", anchor="w", bg="white", fg="blue", justify="left")
        self.tracker_label.grid(row=2, column=1, sticky="nw", padx=10, pady=5)

        self.tree_orders.bind("<<TreeviewSelect>>", self.seleccionar_orden)

        # Orden manual
        self.btn_add_order = tk.Button(self, text="Crear pedido manual", command=self.crear_orden_dialogo)
        self.btn_add_order.grid(row=3, column=1, padx=10, pady=2)

    def refrescar_gui(self):
        # Actualiza mapa ciudad
        self.mapa_canvas.delete("all")
        espacio_calle = 20
        alto = 25* config["ciudad_calles"]
        largo = 15* config["ciudad_avenidas"]

        for i in range(config["ciudad_avenidas"]):
            for j in range(config["ciudad_calles"]):
                x = espacio_calle + i *(largo + espacio_calle)
                y = espacio_calle + j *(alto + espacio_calle)

                if j == 1 and i == 3:
                    self.mapa_canvas.create_rectangle(x, y, x+largo, y+alto, fill="#ff5454")
                    self.mapa_canvas.create_text(x+largo//2, y+alto//2, text="Unidad de\nentregas", font=("Arial", 9, "bold"), fill='white')
                    continue

                edificios = ciudad.cuadras[i][j]
                ancho_edif = largo // len(edificios)
                for idx, pisos in enumerate(edificios):
                    x1 = x + idx * ancho_edif
                    y1 = y
                    x2 = x1 + ancho_edif -2
                    y2 = y1 +alto -2
                    self.mapa_canvas.create_rectangle(x1, y1, x2, y2, fill="#b8b8b8")
                    self.mapa_canvas.create_text((x1+x2)//2, y1+10, text=f"{pisos}F", font=("Arial", 7))

        for dron in drones:
            if dron.pedido_actual:
                x = espacio_calle + (dron.posicion_actual[1] * (largo + espacio_calle)) + largo//2
                y = espacio_calle + (dron.posicion_actual[0] * (alto + espacio_calle)) + alto//2

                if dron.ruta:
                    for k in range(len(dron.ruta)-1):
                        calle1, avenida1 = dron.ruta[k]
                        calle2, avenida2 = dron.ruta[k+1]

                        x1 = espacio_calle + avenida1 * (largo + espacio_calle) + largo//2
                        x2 = espacio_calle + avenida2 * (largo + espacio_calle) + largo//2
                        y1 = espacio_calle + calle1 * (alto + espacio_calle) + alto//2
                        y2 = espacio_calle + calle2 * (alto + espacio_calle) + alto//2

                        # self.mapa_canvas.create_line(x1,y1,x2,y2, fill="red", width=2)

                calle, avenida = dron.posicion_actual
                x = espacio_calle + avenida * (largo + espacio_calle) + largo//2
                y = espacio_calle + calle * (alto + espacio_calle) + alto//2

                self.mapa_canvas.create_oval(x-6,y-6,x+6,y+6, fill='white', outline="black", width=2)
                self.mapa_canvas.create_text(x,y, text=str(dron.id), fill='white', font=("Arial", 8, "bold"))

                dir_pedido = dron.pedido_actual.direccion
                x_destino = espacio_calle + dir_pedido.avenida * (largo + espacio_calle) + largo//2
                y_destino = espacio_calle + dir_pedido.calle * (alto + espacio_calle) + alto//2
                self.mapa_canvas.create_line(x_destino-5, y_destino-5, x_destino+5, y_destino+5, fill="black", width=2)
                self.mapa_canvas.create_line(x_destino-5, y_destino+5,x_destino+5, y_destino-5, fill="black", width=2)

        for i in self.tree_orders.get_children():
            self.tree_orders.delete(i)

        with lock:
            for pedido in lista_pedidos:
                self.tree_orders.insert("", "end", values=(pedido.tracking, pedido.estado, pedido.cliente, str(pedido.direccion)))

        for ide, dron in enumerate(drones):
            self.drones_labels[ide].config(text=f"Dron {dron.id}: {dron.bateria}%")

        self.after(1000, self.refrescar_gui)
        load_pedido_archivo()


    def seleccionar_orden(self, event = None):
        seleccionado = self.tree_orders.selection()
        if not seleccionado:
            return
        item = self.tree_orders.item(seleccionado[0])
        trac = item["values"][0]

        with lock:
            pedido = next((p for p in lista_pedidos if p.tracking == trac), None)

        if pedido:
            txt = f"Tracking: {pedido.tracking}\nCliente: {pedido.cliente}\nDireccion: {pedido.direccion}\n Estado: {pedido.estado}\n"
            txt += "Bitácora:\n" + "\n".join(pedido.bitacora)
            self.tracker_label.config(text=txt)
        else:
            self.tracker_label.config(text='')

    def crear_orden_dialogo(self):
        win = tk.Toplevel(self)
        win.title("Nuevo Pedido Simulado")
        win.geometry("300x350")
        tk.Label(win, text="Cliente:").pack()
        entry_cliente = tk.Entry(win)
        entry_cliente.pack()
        tk.Label(win, text=f"Calle horizontal (0-{config['ciudad_calles']}):").pack()
        entry_calle = tk.Entry(win)
        entry_calle.pack()
        tk.Label(win, text=f"Avenida vertical (0-{config['ciudad_avenidas']}):").pack()
        entry_avenida = tk.Entry(win)
        entry_avenida.pack()
        tk.Label(win, text="Edificio:").pack()
        entry_edificio = tk.Entry(win)
        entry_edificio.pack()
        tk.Label(win, text="Piso:").pack()
        entry_piso = tk.Entry(win)
        entry_piso.pack()
        tk.Label(win, text="Peso:").pack()
        entry_peso = tk.Entry(win)
        entry_peso.pack()
        tk.Label(win, text="Apartamento:").pack()
        entry_apartamento = tk.Entry(win)
        entry_apartamento.pack()

        def crear():
            try:
                cliente = entry_cliente.get()
                avenida = int(entry_avenida.get()) -1
                calle = int(entry_calle.get()) -1
                edificio = int(entry_edificio.get()) -1
                piso = int(entry_piso.get()) -1
                apartamento = int(entry_apartamento.get()) -1
                peso = int(entry_peso.get())

                if (avenida < 0 or avenida >= config['ciudad_avenidas']) or (calle < 0 or calle >= config['ciudad_calles']):
                    return messagebox.showerror("Error", "Calles y avenidas ingreseadas son incorrectas") 
                
                direccion = Direccion(calle, avenida, edificio, piso, apartamento)
                pedido = Pedido(cliente, direccion, peso)
                with lock:
                    lista_pedidos.append(pedido)
                pedidos_queue.put(pedido)
                win.destroy()
            except:
                messagebox.showerror("Error", "Error al cargar los datos del pedido")
        tk.Button(win, text="Crear pedido", command=crear).pack(pady=20)


if __name__ == "__main__":
    app = App()
    app.mainloop()

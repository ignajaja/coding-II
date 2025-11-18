




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
        self.estado = "pending"
        self.tiempo_prep = None
        self.dron = None
        self.tiempo_entraga = None
        self.tiempo_preparacion_inicio = None
        self.tiempo_preparacion_final = None
        self.tiempo_entrega_inicio = None
        self.tiempo_entrega_final = None
        self.bitacora = []

    def log(self, evento):
        self.bitacora.append(f"{datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')} - {evento}")


class Direccion:
    def __init__(self, calle, avenida, edificio, piso, apartamento):
        self.calle = calle
        self.avenida = avenida
        self.edificio = edificio
        self.piso = piso
        self.apartamento = apartamento
    
    def __str__(self):
        return f"Calle {self.calle}, Av {self.avenida}, Edif {self.edificio}, Piso {self.piso}, Apt {self.apartamento}"


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
        return self.cuadras[avenida][calle][edificio]

ciudad = Ciudad(config["ciudad_calles"], config["ciudad_avenidas"])


pedidos_queue = queue.Queue()
preparados_queue = queue.Queue()

lista_pedidos = []

lock = threading.Lock()

def tiempo_de_preparacion_peso(peso):
    for limite in config["tiempo_prep"].items():
        if peso <= int(limite[0]):
            return limite[1]
    return config["tiempo_prep"]["100"]  # Default para pesos mayores

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
            pedido.log(f"Iniciando preparación con Robot #{self.id}")
            tiempo_preparacion = tiempo_de_preparacion_peso(pedido.peso)
            time.sleep(tiempo_preparacion)
            pedido.tiempo_preparacion_final = datetime.datetime.now()
            pedido.tiempo_prep = tiempo_preparacion
            pedido.estado = 'listo'
            pedido.log(f"Pedido listo en {tiempo_preparacion}s con Robot #{self.id}")
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
        self.posicion_actual = (3, 1)  # Posición inicial en la unidad de entregas (calle 3, avenida 1)
        self.ruta = []  # Lista de posiciones (calle, avenida) para el recorrido

    def calcular_ruta(self, destino_calle, destino_avenida):
        """Calcula la ruta desde la posición actual hasta el destino"""
        ruta = []
        calle_actual, avenida_actual = self.posicion_actual
        
        # Primero moverse en avenidas (horizontal)
        while avenida_actual != destino_avenida:
            if avenida_actual < destino_avenida:
                avenida_actual += 1
            else:
                avenida_actual -= 1
            ruta.append((calle_actual, avenida_actual))
        
        # Luego moverse en calles (vertical)
        while calle_actual != destino_calle:
            if calle_actual < destino_calle:
                calle_actual += 1
            else:
                calle_actual -= 1
            ruta.append((calle_actual, avenida_actual))
        print(ruta)
        
        return ruta

    def run(self):
        while self.funcionando:
            pedido = preparados_queue.get()
            pedido.estado = "entregando"
            pedido.dron = self.id
            pedido.tiempo_entrega_inicio = datetime.datetime.now()
            pedido.log(f"Dron #{self.id} iniciando entrega")

            direccion = pedido.direccion
            
            # Calcular ruta
            self.ruta = self.calcular_ruta(direccion.calle, direccion.avenida)
            
            tiempo_ruta = (abs(direccion.calle - self.posicion_actual[0]) * config['tiempo_calle'] + 
                          abs(direccion.avenida - self.posicion_actual[1]) * config['tiempo_calle'])
            
            try:
                pisos = ciudad.get_building_floor(direccion.calle, direccion.avenida, direccion.edificio)
            except:
                pedido.log(f"Error: Edificio no encontrado en la dirección especificada")
                preparados_queue.task_done()
                continue
            
            tiempo_aire = abs(direccion.piso) * config['tiempo_piso']
            tiempo_entrega = tiempo_ruta + tiempo_aire + config['tiempo_puerta']

            if self.bateria < tiempo_entrega:
                pedido.log(f"Dron #{self.id} no tiene batería suficiente. Recargando...")
                self.bateria = 100
                pedido.log(f"Dron #{self.id} recargado al 100%")
                preparados_queue.put(pedido)
                preparados_queue.task_done()
                continue
            
            self.pedido_actual = pedido
            bateria_inicial = self.bateria
            
            # Simular movimiento paso a paso
            tiempo_por_paso = tiempo_ruta / len(self.ruta) if self.ruta else 0
            for paso in self.ruta:
                self.posicion_actual = paso
                time.sleep(tiempo_por_paso)
            
            # Subir pisos y entregar
            time.sleep(tiempo_aire + config['tiempo_puerta'])
            
            self.bateria -= tiempo_entrega
            pedido.tiempo_entrega_final = datetime.datetime.now()
            pedido.tiempo_entrega = tiempo_entrega
            pedido.estado = 'entregado'
            pedido.log(f"Pedido entregado por Dron #{self.id}. Batería inicial: {bateria_inicial}%. Batería final: {self.bateria}%.")
            
            # Regresar a la base
            self.ruta = self.calcular_ruta(3, 1)
            for paso in self.ruta:
                self.posicion_actual = paso
                time.sleep(tiempo_por_paso)
            
            self.pedido_actual = None
            self.ruta = []
            preparados_queue.task_done()
            drones_libres.put(self)

for i in range(config['num_drones']):
    dron = Dron(i+1)
    drones.append(dron)
    drones_libres.put(dron)
    dron.start()


### muy importante, pedidos por archivo
def load_pedido_archivo():
    folder = "./pedidos"

    if not os.path.exists(folder):
        os.makedirs(folder)
    
    historial = set()
    while True:
        archivos = [f for f in os.listdir(folder) if f.endswith(".txt") or f.endswith(".json")]
        for archivo in archivos:
            path = os.path.join(folder, archivo)
            if path in historial:
                continue
            try:
                with open(path, 'r') as a:
                    datos = json.load(a) if archivo.endswith('.json') else eval(a.read())
                direccion = Direccion(datos["calle"], datos['avenida'], datos['edificio'], datos['piso'], datos['apartamento'])
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
            except Exception as e:
                print(f"Error leyendo pedido de {archivo}: {e}")
        time.sleep(2)

threading.Thread(target=load_pedido_archivo, daemon=True).start()


class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Entrega de encargos - Drone Delivery Simulator")
        self.geometry("1400x700")
        self.create_widgets()
        self.refrescar_gui()
        
    def create_widgets(self):
        # Canvas para el mapa con más espacio
        self.mapa_canvas = tk.Canvas(self, width=900, height=600, bg="#f0f0f0")
        self.mapa_canvas.grid(row=0, column=0, rowspan=6, padx=10, pady=10)

        # Lista de pedidos
        self.tree_orders = ttk.Treeview(self, columns=("Tracking", "Estado", "Cliente", "Direccion"), show='headings', height=10)
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
        self.drones_frame.grid(row=1, column=1, sticky="nsew", padx=10, pady=5)
        
        tk.Label(self.drones_frame, text="Estado de Drones", font=("Arial", 10, "bold"), bg="white").pack(pady=5)
        
        self.drones_labels = []
        for i in range(config["num_drones"]):
            lbl = tk.Label(self.drones_frame, text=f"Dron {i+1}: ", bg="white", anchor="w", font=("Arial", 9))
            lbl.pack(anchor="w", padx=10)
            self.drones_labels.append(lbl)

        # Pedido tracker (detalles por pedido seleccionado)
        tracker_frame = tk.Frame(self, bg="white", relief="solid", borderwidth=1)
        tracker_frame.grid(row=2, column=1, sticky="nsew", padx=10, pady=5)
        
        tk.Label(tracker_frame, text="Bitácora del Pedido", font=("Arial", 10, "bold"), bg="white").pack(pady=5)
        
        self.tracker_label = tk.Label(tracker_frame, text="Seleccione un pedido para ver detalles", 
                                      anchor="nw", bg="white", justify="left", font=("Arial", 8))
        self.tracker_label.pack(fill="both", expand=True, padx=10, pady=5)

        self.tree_orders.bind("<<TreeviewSelect>>", self.seleccionar_orden)

        # Orden manual
        self.btn_add_order = tk.Button(self, text="Crear Pedido Manual", command=self.crear_orden_dialogo, 
                                       bg="#4CAF50", fg="white", font=("Arial", 10, "bold"))
        self.btn_add_order.grid(row=3, column=1, padx=10, pady=10)

    def refrescar_gui(self):
        # Actualiza mapa ciudad con espacios entre cuadras
        self.mapa_canvas.delete("all")
        
        # Tamaño de cada cuadra con espacio para calles
        espacio_calle = 20  # Espacio para simular calles/avenidas
        ancho_cuadra = (900 - (config["ciudad_avenidas"] + 1) * espacio_calle) // config["ciudad_avenidas"]
        alto_cuadra = (600 - (config["ciudad_calles"] + 1) * espacio_calle) // config["ciudad_calles"]
        
        for i in range(config["ciudad_calles"]):
            for j in range(config["ciudad_avenidas"]):
                # Posición con espacio para calles
                x_base = espacio_calle + j * (ancho_cuadra + espacio_calle)
                y_base = espacio_calle + i * (alto_cuadra + espacio_calle)
                
                # Unidad de entregas en posición específica (calle 3, avenida 1)
                if i == 3 and j == 1:
                    self.mapa_canvas.create_rectangle(x_base, y_base, 
                                                     x_base + ancho_cuadra, 
                                                     y_base + alto_cuadra, 
                                                     fill="#ff5454", outline="black", width=2)
                    self.mapa_canvas.create_text(x_base + ancho_cuadra//2, y_base + alto_cuadra//2, 
                                                text="Unidad de\nEntregas", 
                                                font=("Arial", 9, "bold"), fill='white')
                    continue

                edificios = ciudad.cuadras[j][i]
                ancho_edificio = ancho_cuadra // len(edificios)
                
                for idx, pisos in enumerate(edificios):
                    x1 = x_base + idx * ancho_edificio
                    y1 = y_base
                    x2 = x1 + ancho_edificio - 2
                    y2 = y1 + alto_cuadra - 2
                    
                    self.mapa_canvas.create_rectangle(x1, y1, x2, y2, fill="#b0c4de", outline="#5a5a5a")
                    self.mapa_canvas.create_text((x1+x2)//2, y1+10, text=f"{pisos}P", font=("Arial", 7, "bold"))

        # Dibujar drones y sus rutas
        for dron in drones:
            if dron.pedido_actual:
                # Dibujar la ruta completa
                if dron.ruta:
                    for idx in range(len(dron.ruta) - 1):
                        calle1, avenida1 = dron.ruta[idx]
                        calle2, avenida2 = dron.ruta[idx + 1]
                        
                        x1 = espacio_calle + avenida1 * (ancho_cuadra + espacio_calle) + ancho_cuadra//2
                        y1 = espacio_calle + calle1 * (alto_cuadra + espacio_calle) + alto_cuadra//2
                        x2 = espacio_calle + avenida2 * (ancho_cuadra + espacio_calle) + ancho_cuadra//2
                        y2 = espacio_calle + calle2 * (alto_cuadra + espacio_calle) + alto_cuadra//2
                        
                        self.mapa_canvas.create_line(x1, y1, x2, y2, fill="blue", width=2, dash=(5, 2))
                
                # Dibujar posición actual del dron
                calle, avenida = dron.posicion_actual
                x = espacio_calle + avenida * (ancho_cuadra + espacio_calle) + ancho_cuadra//2
                y = espacio_calle + calle * (alto_cuadra + espacio_calle) + alto_cuadra//2
                
                # Dron como círculo rojo
                self.mapa_canvas.create_oval(x-8, y-8, x+8, y+8, fill="red", outline="darkred", width=2)
                self.mapa_canvas.create_text(x, y, text=str(dron.id), fill="white", font=("Arial", 8, "bold"))
                
                # Destino como círculo verde
                dir_pedido = dron.pedido_actual.direccion
                x_dest = espacio_calle + dir_pedido.avenida * (ancho_cuadra + espacio_calle) + ancho_cuadra//2
                y_dest = espacio_calle + dir_pedido.calle * (alto_cuadra + espacio_calle) + alto_cuadra//2
                self.mapa_canvas.create_oval(x_dest-6, y_dest-6, x_dest+6, y_dest+6, 
                                            fill="green", outline="darkgreen", width=2)

        # Actualizar lista de pedidos
        for i in self.tree_orders.get_children():
            self.tree_orders.delete(i)

        with lock:
            for pedido in lista_pedidos:
                self.tree_orders.insert("", "end", values=(
                    pedido.tracking[:8] + "...", 
                    pedido.estado, 
                    pedido.cliente, 
                    str(pedido.direccion)
                ))

        # Actualizar estado de drones
        for ide, dron in enumerate(drones):
            estado = f"Dron #{dron.id} - Batería: {dron.bateria}%"
            if dron.pedido_actual:
                estado += f" - Entregando a {dron.pedido_actual.cliente}"
            else:
                estado += " - Disponible"
            self.drones_labels[ide].config(text=estado)

        self.after(500, self.refrescar_gui)  # Actualizar cada 500ms para mejor fluidez

    def seleccionar_orden(self, event=None):
        seleccionado = self.tree_orders.selection()
        if not seleccionado:
            return
        item = self.tree_orders.item(seleccionado[0])
        tracking_corto = item['values'][0]
        
        with lock:
            pedido = next((p for p in lista_pedidos if p.tracking.startswith(tracking_corto.replace("...", ""))), None)
        
        if pedido:
            txt = f"Tracking: {pedido.tracking}\n"
            txt += f"Cliente: {pedido.cliente}\n"
            txt += f"Dirección: {pedido.direccion}\n"
            txt += f"Peso: {pedido.peso} kg\n"
            txt += f"Estado: {pedido.estado}\n\n"
            txt += "Bitácora:\n" + "\n".join(pedido.bitacora)
            self.tracker_label.config(text=txt)
        else:
            self.tracker_label.config(text='Pedido no encontrado')

    def crear_orden_dialogo(self):
        win = tk.Toplevel(self)
        win.title("Nuevo Pedido Manual")
        win.geometry("350x450")
        
        tk.Label(win, text="Cliente:", font=("Arial", 10)).pack(pady=5)
        entry_cliente = tk.Entry(win, font=("Arial", 10))
        entry_cliente.pack()
        
        tk.Label(win, text=f"Calle (0-{config['ciudad_calles']-1}):", font=("Arial", 10)).pack(pady=5)
        entry_calle = tk.Entry(win, font=("Arial", 10))
        entry_calle.pack()
        
        tk.Label(win, text=f"Avenida (0-{config['ciudad_avenidas']-1}):", font=("Arial", 10)).pack(pady=5)
        entry_avenida = tk.Entry(win, font=("Arial", 10))
        entry_avenida.pack()
        
        tk.Label(win, text="Edificio (0-N):", font=("Arial", 10)).pack(pady=5)
        entry_edificio = tk.Entry(win, font=("Arial", 10))
        entry_edificio.pack()
        
        tk.Label(win, text="Piso:", font=("Arial", 10)).pack(pady=5)
        entry_piso = tk.Entry(win, font=("Arial", 10))
        entry_piso.pack()
        
        tk.Label(win, text="Apartamento:", font=("Arial", 10)).pack(pady=5)
        entry_apartamento = tk.Entry(win, font=("Arial", 10))
        entry_apartamento.pack()

        def crear():
            try:
                cliente = entry_cliente.get()
                calle = int(entry_calle.get())
                avenida = int(entry_avenida.get())
                edificio = int(entry_edificio.get())
                piso = int(entry_piso.get())
                apartamento = int(entry_apartamento.get())
                
                if calle < 0 or calle >= config['ciudad_calles']:
                    raise ValueError("Calle fuera de rango")
                if avenida < 0 or avenida >= config['ciudad_avenidas']:
                    raise ValueError("Avenida fuera de rango")
                
                direccion = Direccion(calle, avenida, edificio, piso, apartamento)
                peso = random.randint(1, 100)
                pedido = Pedido(cliente, direccion, peso)
                
                with lock:
                    lista_pedidos.append(pedido)
                pedidos_queue.put(pedido)
                
                messagebox.showinfo("Éxito", f"Pedido creado con tracking: {pedido.tracking[:8]}...")
                win.destroy()
            except ValueError as e:
                messagebox.showerror("Error", f"Datos inválidos: {str(e)}")
            except Exception as e:
                messagebox.showerror("Error", f"Error al crear el pedido: {str(e)}")
        
        tk.Button(win, text="Crear Pedido", command=crear, bg="#4CAF50", fg="white", 
                 font=("Arial", 10, "bold")).pack(pady=20)


if __name__ == "__main__":
    app = App()
    app.mainloop()
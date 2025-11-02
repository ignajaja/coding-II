import tkinter as tk
import json
from datetime import datetime


# ====================
# constantes globales
# ====================

# coordenadas y datos importantes para el mapa
ANCHO_MUNDO = 180 
ALTO_MUNDO = 90
ESCALA = 3
MARGEN = 30

# mapa que se muestra en el juego
MAPA = [
    [
        "Costa Rica", 100, 98000,
        [
            "Alajuela", [
                ["San Ramon", [[[-150, 0, 0],[25, 0, 0]], [[-120, 0, 0],[45, 0, 0]]]],
                ["San Mateo", [[[-160, 0, 0],[80, 0, 0]], [[-130, 0, 0],[48, 0, 0]]]]
            ]
        ],
        [
            "Cartago", [
                ["Alvarado", [[[-140, 0, 0],[10, 0, 0]], [[-110, 0, 0],[18, 0, 0]]]],
                ["El Guarco", [[[-165, 0, 0],[12, 0, 0]], [[-147, 0, 0],[-8, 0, 0]]]],
                ["Cental", [[[-135, 0, 0],[0, 0, 0]], [[-128, 0, 0],[-7, 0, 0]]]]
            ]
        ],
        [
            "San Jose", [
                ["Perez Zeledon", [[[-170, 0, 0],[-75, 0, 0]], [[-98, 0, 0],[-35, 0, 0]]]],
                ["Escazu", [[[-167, 0, 0],[-18, 0, 0]], [[-155, 0, 0],[-28, 0, 0]]]]
            ]
        ]
    ],
    [
        "Colombia", 100, 100000,
        [
            "Antioquia", [
                ["Medellin", [[[-30, 0, 0],[50, 0, 0]], [[-50, 0, 0],[70, 0, 0]]]],
                ["Bello", [[[-45, 0, 0],[48, 0, 0]], [[-20, 0, 0],[42, 0, 0]]]]
            ]
        ],
        [
            "Cundinamarca", [
                ["Bogota", [[[-50, 0, 0],[35, 0, 0]], [[-10, 0, 0],[15, 0, 0]]]],
                ["Soacha", [[[-20, 0, 0],[80, 0, 0]], [[-8, 0, 0],[60, 0, 0]]]]
            ]
        ],
        [
            "Valle del Cauca", [
                ["Cali", [[[-55, 0, 0],[67, 0, 0]], [[-70, 0, 0],[42, 0, 0]]]],
                ["Palmira", [[[-35, 0, 0],[-8, 0, 0]], [[-48, 0, 0],[-18, 0, 0]]]]
            ]
        ]
    ],
    [
        "Italia", 100, 110000,
        [
            "Lazio", [
                ["Roma", [[[60, 0, 0],[-80, 0, 0]], [[90, 0, 0],[-63, 0, 0]]]],
                ["Frosinone", [[[65, 0, 0],[-35, 0, 0]], [[95, 0, 0],[-25, 0, 0]]]]
            ]
        ],
        [
            "Toscana", [
                ["Florencia", [[[20, 0, 0],[-82, 0, 0]], [[0, 0, 0],[-62, 0, 0]]]],
                ["Pisa", [[[75, 0, 0],[-20, 0, 0]], [[85, 0, 0],[10, 0, 0]]]],
                ["Siena", [[[50, 0, 0],[-42, 0, 0]], [[36, 0, 0],[-72, 0, 0]]]]
            ]
        ],
        [
            "Lombardia", [  
                ["Milan", [[[80, 0, 0],[-56, 0, 0]], [[57, 0, 0],[-40, 0, 0]]]],
            ]
        ]
    ],
    [
        "Alemania", 100, 120000,
        [
            "Baviera", [
                ["Munich", [[[160, 0, 0],[55, 0, 0]], [[125, 0, 0],[40, 0, 0]]]],
                ["Núremberg", [[[118, 0, 0],[88, 0, 0]], [[80, 0, 0],[65, 0, 0]]]]
            ]
        ],
        [
            "Renania", [
                ["Colonia", [[[75, 0, 0],[80, 0, 0]], [[60, 0, 0],[60, 0, 0]]]],
                ["Dusseldorf", [[[148, 0, 0],[82, 0, 0]], [[179, 0, 0],[62, 0, 0]]]],
                ["Bonn", [[[140, 0, 0],[84, 0, 0]], [[120, 0, 0],[73, 0, 0]]]]
            ]
        ],
        [
            "Sajonia", [  
                ["Dresde", [[[45, 0, 0],[45, 0, 0]], [[55, 0, 0],[55, 0, 0]]]],
                ["Leipzig", [[[155, 0, 0],[15, 0, 0]], [[170, 0, 0],[35, 0, 0]]]]
            ]
        ]
    ],
    [
        "Australia", 100, 130000, 
        [
            "Nueva Gales del Sur", [
                ["Sidney", [[[135, 0, 0],[-20, 0, 0]], [[180, 0, 0],[-90, 0, 0]]]],
        ]
        ]
    ]
]


# =======================
# varialbes globales
# =======================

# lista de potencias, vida y territorios
potencias = []
vida_territorios = [[0]]
lista_registro = []

# para la IU
root = None
entrada_x = None
entrada_y = None
entrada_x1 = entrada_x2 = entrada_x3 = entrada_y1 = entrada_y2 = entrada_y3 = entrada_potencia = entrada_potencia_r = entrada_territorio= None
resultado_var = status_var = confirmacion_var = None
canvas = None
tamano_botones = (20, 2)
territorios_iniciados = False

# para disparos
ultimo_disparo = None


# ========================
# guargar y cargar
# ========================
# GYC lista y archivo de potencias
def guardar_potencias():
    global potencias
    try:
        with open("potencias.txt", "w") as archivo:
            json.dump(potencias, archivo) # se usa el formato json.dump para guardar los datos en el .txt, esto hace que se carguen de manera mucho más sencilla
            # aprendido en https://stackoverflow.com/questions/27745500/how-to-save-a-list-to-a-file-and-read-it-as-a-list-type
    except Exception:
        True
    return

def cargar_potencias():
    global potencias

    try:
        with open("potencias.txt", "r", encoding="utf-8") as archivo:
            potencias = json.load(archivo)
    except Exception:
        True
    return

# GYC lista y archivo de vida de los territorios
def guardar_vida_territorios():
    global vida_territorios

    vida_territorios[0] = 1
    
    try:
        with open("vida_territorios.txt", "w") as archivo:
            json.dump(vida_territorios, archivo) 
    except Exception:
        True
    return

def cargar_vida_territorios():
    global vida_territorios

    try:
        with open("vida_territorios.txt", "r", encoding="utf-8") as archivo:
            vida_territorios = json.load(archivo)
    except Exception:
        True
    return

# GYC lista y archivo de registro de actividades 
def guardar_registro():
    global lista_registro

    with open("registro.txt", "w") as archivo:
        json.dump(lista_registro, archivo)
    return

def cargar_registro():
    global lista_registro

    try:
        with open("registro.txt", "r", encoding="utf-8") as archivo:
            lista_registro = json.load(archivo)

    except Exception:
        True
    return

# limpia el registro cuando se reinicia el juego
def limpiar_registro():
    global lista_registro
    lista_registro = []
    with open("registro.txt", "w") as archivo:
        archivo.write("")

    return


#============================
# commons
#============================


# genera el tiempo actual, útil para el registro de actividades
def generar_tiempo():
    ahora = datetime.now() # importa el tiempom real
    timestamp = ahora.strftime("%Y-%m-%d %H:%M:%S")
    return str(timestamp)

# guardan las diferentes acciones hechas durante el juego
def actualizar_registro_ataque(potencia, territorio, coor):
    global lista_registro
    
    vida_ter = 0
    for ter in vida_territorios[1:]:
        if ter[0] == territorio:
            vida_ter = ter[1]
            break  

    tiempo = generar_tiempo()
    texto = [[tiempo],[0],[potencia],[coor],[territorio],[vida_ter]] # le da el formato al atacar
    lista_registro.append(texto) 
    guardar_registro()

def actualizar_registro_compra(potencia, cantidad):
    global lista_registro
    
    tiempo = generar_tiempo()
    texto = [[tiempo],[1],[potencia],[cantidad]]
    lista_registro.append(texto)
    guardar_registro()

def actualizar_registro_cambio(potencia, cambio):
    global lista_registro
    
    tiempo = generar_tiempo()
    texto = [[tiempo],[2],[potencia],["activa" if cambio == True else "inactiva"]] # le da el formato a el cambio de esdado de una potencia
    lista_registro.append(texto)
    guardar_registro()
    
def actualizar_registro_muerte(potencia):
    global lista_registro
   
    tiempo = generar_tiempo()
    texto = [[tiempo],[3],[potencia]]
    lista_registro.append(texto)
    guardar_registro()

def actualizar_registro_territorio(potencia):
    global lista_registro, potencias
    
    tiempo = generar_tiempo()
    for pot in potencias:
        if pot[0][0] == potencia:
            texto = [[4],[generar_tiempo()],[potencia],[pot[0][3]]]
            lista_registro.append(texto)

            guardar_registro([[tiempo],["TERRITORIO"],[potencia],[pot[0][3]]])


# coordenadas a xy solo recibe entradas de tipo entry
# convierte las coordenadas de grados, minutos y segundos a x, y para la lógica
def coordenadas_a_xy(e_x1, e_x2, e_x3, e_y1, e_y2, e_y3):
    try:
        x1 = float(e_x1.get()); x2 = float(e_x2.get()); x3 = float(e_x3.get())
        y1 = float(e_y1.get()); y2 = float(e_y2.get()); y3 = float(e_y3.get())
    except Exception as exc:
        raise ValueError("Entradas inválidas") from exc

    sign_x = -1 if x1 < 0 else 1 # ternario para saber si es negativo y no tener que hacer tantos if
    sign_y = -1 if y1 < 0 else 1

    cx = sign_x * (abs(x1) + x2 / 60 + x3 / 3600)
    cy = sign_y * (abs(y1) + y2 / 60 + y3 / 3600)
    
    return cx, cy

# convierte los x, y para escribir en el mapa
def convertir_a_xy_mapa(coord_x, coord_y):
    x1 = coord_x[0]; x2 = coord_x[1]; x3 = coord_x[2]
    y1 = coord_y[0]; y2 = coord_y[1]; y3 = coord_y[2]
    
    sign_x = -1 if x1 < 0 else 1
    sign_y = -1 if y1 < 0 else 1
    
    # convierte los grados a pixeles
    cx = sign_x * (abs(x1) + x2 / 6 + x3 / 360)
    cy = sign_y * (abs(y1) + y2 / 6 + y3 / 360)
    
    return cx, cy

# convierte las coordenadas del mundo al mapa para ser escritas
def mundo_a_canvas(xm, ym):
    # sumar el punto con el ancho y el alto del mundo multiplicados por la escala para que 0,0 est en el medio  
    ancho_canvas = MARGEN * 2 + (ANCHO_MUNDO * 2) * ESCALA
    alto_canvas = MARGEN * 2 + (ALTO_MUNDO * 2) * ESCALA
    cx_centro = ancho_canvas //2
    cy_centro = alto_canvas //2

    cx = cx_centro + xm * ESCALA
    cy = cy_centro - ym * ESCALA
    return cx, cy

def normalizar_rectangulo(p1, p2): # hace que todos los rectángulos se puedan acomodar de manera ordenada
    x1 = p1[0] 
    y1 = p1[1]
    x2 = p2[0] 
    y2 = p2[1]
    
    # no me funiconaba usar el min() y max(), entonces se hizo con if
    xmin = x1 if x1[0] < x2[0] else x2
    xmax = x1 if x1[0] > x2[0] else x2
    ymin = y1 if y1[0] < y2[0] else y2
    ymax = y1 if y1[0] > y2[0] else y2
    
    return xmin, xmax, ymin, ymax

def punto_en_rectangulo(x,y,rect):
    # dice si un pundo está dentro del rectángulo
    xmin,xmax,ymin,ymax = rect
    return ((xmin) <= x <= xmax) and (ymin <= y <= ymax) # true si le da a el rectángulo, false si no

# cuenta la extensión de cada territorio
def contar_extension(territorio):
    lista_resultado = [0, 0, 0]
    
    for pais in MAPA:
        for region in pais[3:]:
            for ciudad in region[1]:
                if ciudad[0] == territorio: 
                    t_contar = ciudad[1]
                    break
    
    rect = normalizar_rectangulo(t_contar[0], t_contar[1])

    lista_resultado[0] = (rect[1][0] - rect[0][0]) * (rect[3][0] - rect[2][0]) * 60000
    lista_resultado[1] = (rect[1][1] - rect[0][1]) * (rect[2][1] - rect[3][1]) * 1000
    lista_resultado[2] = (rect[1][2] - rect[0][2]) * (rect[2][2] - rect[3][2]) * 16.7

    return sum(lista_resultado)

# cuenta la extensión total que posee una potencia, juntando sus territorios
def contar_extension_potencia(nombre):
    global potencias
    contador = 0

    for pot in potencias:
        if pot[0][0] == nombre:
            for ter in pot[1:]:
                contador += contar_extension(ter[0])

    return contador

# inicializa la vida de los territorios
def asignar_vida_territorios():
    global potencias, vida_territorios
    vida_territorios = [[1]]

    for pais in MAPA:
        for region in pais[3:]:
            for ciudad in region[1]:
                vida_territorios.append([ciudad[0], 100])

    for pots in potencias:
        pots[0][3] = 100 # reinicia la vida las de potencias

    guardar_vida_territorios()
    guardar_potencias()

    return

# baja la vida de un territorio al ser disparado o al comprar misiles
def reducir_vida_territorio(territorio):
    global vida_territorios
    
    for pais in MAPA:
        for region in pais[3:]:
            for ciudad in region[1]:
                
                if ciudad[0] == territorio:
                    for ter in vida_territorios[1:]:
                        
                        if ter[0] == territorio:
                            ter[1] -= 10
    return

# verifica la vida de las potencias 
def verificar_vida_potencia():
    global potencias, vida_territorios

    for pots in potencias:
        territorios = pots[1] if len(pots) > 1 else []
        cantidad_territorios = 0

        for territorio in territorios:
            nombre_terr = territorio[0]
            for ter in vida_territorios[1:]:
                if ter[0] == nombre_terr:
                    cantidad_territorios += 1
                    break

        if cantidad_territorios == 0:
            pots[0][2] = False  # set indicador_pot to False (defeated)
            actualizar_registro_muerte(pots[0][0])

# verifica que los puntos de el mapa no se traslapen
def mapa_se_traslapa():
    global MAPA

    for pais in MAPA:
        for region in pais[3:]:
            for ciudad in region[1]:
                territorio = ciudad[1]
                rect = normalizar_rectangulo(territorio[0], territorio[1])
                for pais_j in MAPA:
                    for region_j in pais_j[3:]:
                        for ciudad_j in region_j[1]:
                            if ciudad_j[0] != ciudad[0]:  # evitar comparar el mismo territorio
                                territorio_j = ciudad_j[1]
                                rect_j = normalizar_rectangulo(territorio_j[0], territorio_j[1])
                                lista1 = [[[rect[0][0], rect[2][0]],[rect[0][0],rect[3][0]]],[[rect[1][0], rect[2][0]],[rect[1][0],rect[3][0]]]]
                                lista2 = [[[rect_j[0][0], rect_j[2][0]],[rect_j[0][0],rect_j[3][0]]],[[rect_j[1][0], rect_j[2][0]],[rect_j[1][0],rect_j[3][0]]]]

                                for r in lista1:
                                    for s in lista2:
                                        if (r[0][0]<= s[0][0] <= r[1][0] and r[0][1]<= s[0][1] <= r[1][1]) or (r[0][0]<= s[1][0] <= r[1][0] and r[0][1]<= s[1][1] <= r[1][1]):
                                            return False
    return True 



#============================
# lógica potencias
#============================

# está hasta arriba porque es necesario llamarlo antes de las demás construcciones de ventanas, por los casos de error
def construir_error(msg = "Ha ocurrido un error inesperado"):
    global root
    win = tk.Toplevel(root)
    win.geometry("400x200")
    
    contenedor = tk.Frame(win)
    contenedor.pack(fill='both', expand=False, padx=10, pady=10)
    panel = tk.Frame(contenedor)
    panel.pack(fill="y", padx=(0,10))

    tk.Label(panel, text=msg, font=("Arial", 12)).pack(anchor='w', pady=20)
    tk.Button(panel, text="Cerrar", command=win.destroy, font=("Arial", 10, "bold"), fg="white", bg="#ff0000").pack(anchor='se', pady=10)


# asigna el territorio a una potencia
def reclamar_territorio():
    global potencias, entrada_potencia_r, entrada_territorio

    flag_territorio_encontrado = False

    nombre = entrada_potencia_r.get()
    territorio = entrada_territorio.get()

    for pais in MAPA:
        for region in pais[3:]:
            for ciudad in region[1]:
                if ciudad[0] == territorio:
                    territorio = ciudad 
                    flag_territorio_encontrado = True

    if flag_territorio_encontrado == False:
        construir_error("Territorio no encontrado")
        return # confirma si el territorio fue encontrado

    for pots in potencias:
        if pots[0][1] == False:
            construir_error("La potencia está inactiva")
            continue # no se reclama si está inactiva
        for ter in pots[1:]:
            if ter[0] == territorio[0]:
                construir_error("Una potencia ya posee este territorio")
                return # si la potencia ya tiene el territorio, no se le asigna de nuevo
        if pots[0][0] == nombre: # se asigna cuando encuentra el nombre
            pots.append(territorio)
            pots[0][2] = True

    
    construir_confirmacion("Territorio reclamado con éxito")
    guardar_potencias()
    return


# añade una potencia nueva al juego
def anadir_potencias():
    global potencias, entrada_potencia

    nombre = entrada_potencia.get()
    
    for pot in potencias:
        if nombre == pot[0][0]:
            construir_error("Ya existe una potencia con ese nombre")
            return
    
    estado_pot = True # está activo
    indicador_pot = True # está vivo
    por_vida_pot = 100 # vida 
    can_misiles_pot = 1000 # misiles
    can_disparos_pot = 0 # disparos enviados
    can_recibidos_pot = 0 # disparos recibidos

    potencias.append([[nombre, estado_pot, indicador_pot, por_vida_pot, can_misiles_pot, can_disparos_pot, can_recibidos_pot]])

    construir_confirmacion("Potencia añadida con éxito")
    guardar_potencias()
    
    return


# genera el status de la potencia pedida
def generar_status_potencia():
    global potencias, status_var, entrada_potencia
      
    extension_territorios = 0
    flag_potencia_encontrada = False
    nombre = entrada_potencia.get()
    
    for pots in potencias:
        if pots[0][0] == nombre:
            flag_potencia_encontrada = True
            try:
                for territorio in pots[1:]:
                    extension_territorios += contar_extension(territorio[0])
            except:
                True

            if extension_territorios == 0:
                extension_territorios = "no tiene territorios"
            
            
            status_var.set(f"Nombre: {pots[0][0]}\nEstado: {'Activo' if pots[0][1] == True else 'Inactivo'}\nIndicador: {'Vivo' if pots[0][2] == True else 'Derrotada'}\nVida: {pots[0][3]}%\nMisiles: {pots[0][4]}\nDisparos tirados: {pots[0][5]}\nDisparos recibidos: {pots[0][6]}\nExtensión en km²: {extension_territorios}")
            
        
    if flag_potencia_encontrada == False:
        status_var.set("Potencia no encontrada")
                
    return 

# cambia el estado de actividad de la potencia
def cambiar_estado():
    global potencias

    nombre = entrada_potencia.get()
    
    for pots in potencias:
        if pots[0][0] == nombre:
            nuevo_estado = True if pots[0][1] == False else False
            pots[0][1] = nuevo_estado
            break
    
    construir_confirmacion("Estado cambiado con éxito")
    actualizar_registro_cambio(nombre, nuevo_estado)
    guardar_potencias()
    return

# cuenta la vida de los territorios, para saber cuánta le queda o saber si ya perdió
def contar_vida_territorios_potencia(nombre_potencia):
    global potencias, vida_territorios
    vida_total = 0
    cantidad_territorios = 0

    for pots in potencias:
        if pots[0][0] == nombre_potencia:
            for ter in pots[1:]:
                for vida_ter in vida_territorios[1:]:
                    if ter[0] == vida_ter[0]:
                        vida_total += vida_ter[1]
                        cantidad_territorios += 1

    if cantidad_territorios == 0:
        return 0

    vida_promedio = vida_total / cantidad_territorios
    return vida_promedio

# actualiza la vida de las potencias y territorios al ser disparados
def actualizar_vida_potencia(ciudad):
    global potencias, vida_territorios

    for pots in potencias:
        try:
            for territorios in pots[1:]:
                if territorios[0] == ciudad:
                    pots[0][3] = contar_vida_territorios_potencia(pots[0][0]) # actualizar vida de la potencia según la vida de sus territorios
                    pots[0][6] += 1 # aumentar disparos recibidos

                    actualizar_registro_territorio(pots[0][0])
                    
        except:
            continue
    guardar_potencias()
    return

# compra de misiles, aumenta la cantidad de misiles pero disminuye la vida de algún territorio
def comprar_misiles():
    global potencias, vida_territorios, entrada_potencia, entrada_cantidad_misiles

    nombre = entrada_potencia.get()
    cantidad = int(entrada_cantidad_misiles.get())

    if cantidad <= 0 or cantidad > 1000:
        construir_error("Cantidad inválida, debe ser positiva y menor o igual a 1000")
        return # cantidad es inválida
    if cantidad % 100 != 0:
        construir_error("Debe ser un número múltiplo de 100")
        return # no es múltiplo de 100
    
    for pots in potencias:
        if pots[0][0] == nombre:
            try:
                pots[0][4] += cantidad
                territorio = pots[1][0]
            except:
                construir_error("La potencia no posee territorios")
                return
    for ter in vida_territorios[1:]:
        if ter[0] == territorio:
            ter[1] -= (cantidad // 100) * 10
            actualizar_vida_potencia(territorio)

    construir_confirmacion("Misiles comprados con éxito")
    actualizar_registro_compra(nombre, cantidad)
    guardar_potencias()
    guardar_vida_territorios()
    return


#============================
# Rankings
#============================

# expone el ranking de cual potencia es la que tiene más extensión
def rank_extension():
    global potencias

    # lista_potencias = [[potencia[0][0], [territorio[0] for territorio in potencia[1:]]] for potencia in potencias]
    lista_potencias = [[potencia[0][0], contar_extension_potencia(potencia[0][0])] for potencia in potencias]
    lista_potencias.sort(key=lambda x: x[1], reverse=True)

    lista_rank = [nombre[0] for nombre in lista_potencias]
    return lista_rank

# expone el ranking de cual potencia es la que tiene más vida
def rank_porcentaje():
    global potencias

    lista_potencias = [[potencia[0][0], potencia[0][3]] for potencia in potencias]
    lista_potencias.sort(key=lambda x: x[1], reverse=True)

    lista_rank = [nombre[0] for nombre in lista_potencias]
    return lista_rank

# reinicia todo lo cargado en el juego
def reiniciar_juego():
    global potencias

    potencias = []
    guardar_potencias()
    asignar_vida_territorios()
    guardar_vida_territorios()
    cargar_vida_territorios()
    limpiar_registro()

    return


#============================
# lógica de disparo
#============================

# verifica si la potencia puede atacar y ser atacada
def verificar_potencia(nombre):
    global potencias
    for pots in potencias:
        if pots[0][0] == nombre and pots[0][2] == True and pots[0][1] == True:
            return True
            
    return False
        
# la función para atacar, manda un disparo que disminuye la vida de el territorio, su potencia, aumenta disparos recibidos y disparos lanzados del atacante
def disparar():
    global ultimo_disparo, resultado_var, entrada_potencia
    punto_x = punto_y = 0
    try:
        x, y = coordenadas_a_xy(entrada_x1, entrada_x2, entrada_x3, entrada_y1, entrada_y2, entrada_y3)
        coordenadas_para_registro = [entrada_x1.get(), entrada_x2.get(), entrada_x3.get()], [entrada_y1.get(), entrada_y2.get(), entrada_y3.get()]
    except ValueError:
        resultado_var.set("Ingrese un dato válido")
        return
    
    ultimo_disparo = (x, y)
    potencia = entrada_potencia.get()                
    if not verificar_potencia(potencia):
        resultado_var.set("Ingrese un nombre válido de una potencia activa")
        refrescar_canvas()
        return

    if not (-ANCHO_MUNDO <= x <= ANCHO_MUNDO and -ALTO_MUNDO <= y <= ALTO_MUNDO):
        resultado_var.set("Fuera del mapa")
        refrescar_canvas()
        return

    
    for pais in MAPA:
        for prov in pais[3:]:
            for ciud in prov[1]:
                rect = normalizar_rectangulo(ciud[1][0], ciud[1][1])
                xmin, xmax, ymin, ymax = rect

                xmin, xmax = convertir_a_xy_mapa(xmin, xmax)
                ymin, ymax = convertir_a_xy_mapa(ymin, ymax)
                x1_c, y1_c = mundo_a_canvas(xmin,ymin)
                x2_c, y2_c = mundo_a_canvas(xmax,ymax)
                x_min_c, x_max_c = min(x1_c, x2_c), max(x1_c, x2_c)
                y_min_c, y_max_c = min(y1_c, y2_c), max(y1_c, y2_c)
                rect = x_min_c, x_max_c, y_min_c, y_max_c
                punto_x, punto_y = mundo_a_canvas(x, y)
                
                if punto_en_rectangulo(punto_x, punto_y, rect):

                    for pots in potencias:
                        if pots[0][0] == potencia:
                            if pots[0][4] <= 0:
                                resultado_var.set("No hay misiles disponibles")
                                refrescar_canvas()
                                return
                            pots[0][5] += 1 # aumentar disparos tirados
                            pots[0][4] -= 1 # reducir misiles disponibles
                    

                    # Buscar el registro de vida correspondiente a la ciudad impactada
                    registro = None
                    for ter in vida_territorios[1:]:
                        if ter[0] == ciud[0]:
                            registro = ter
                            break

                    # Buscar la potencia propietaria (si existe) para poder incrementar disparos recibidos
                    propietario = None
                    for pots in potencias:
                        for t in pots[1:]:
                            if t[0] == ciud[0]:
                                propietario = pots
                                break
                        if propietario:
                            break

                    if registro is None:
                        # El territorio no está en la lista de vida (tal vez ya fue destruido)
                        resultado_var.set(f"Impacto en {(x, y)}. La ciudad de\n{pais[0]}, {prov[0]},\n{ciud[0]} no existe o ya fue destruida")
                    else:
                        # Si la vida está por debajo o igual al umbral, destruir
                        if registro[1] == 10:
                            reducir_vida_territorio(ciud[0])
                            # contar este impacto como recibido por la potencia propietaria
                            if propietario:
                                propietario[0][6] += 1

                            # recalcular vida de la potencia propietaria (si existe)
                            if propietario:
                                propietario[0][3] = contar_vida_territorios_potencia(propietario[0][0])
                                # si ya no tiene territorios, marcar indicador
                                if propietario[0][3] == 0:
                                    propietario[0][2] = False
                                    actualizar_registro_muerte(propietario[0][0])

                            resultado_var.set(f"Impacto en {(x, y)}. La ciudad de\n{pais[0]}, {prov[0]},\n{ciud[0]} ha sido destruida")
                        elif registro[1] > 10:
                            # Reducir vida y notificar; luego actualizar vida de la potencia
                            reducir_vida_territorio(ciud[0])
                            # obtener nueva vida del registro actualizado
                            nueva_vida = None
                            for ter2 in vida_territorios[1:]:
                                if ter2[0] == ciud[0]:
                                    nueva_vida = ter2[1]
                                    break

                            # aumentar disparos recibidos para la potencia propietaria
                            if propietario:
                                propietario[0][6] += 1

                            resultado_var.set(f"Impacto en {(x, y)}. A {pais[0]},\n {prov[0]}, {ciud[0]} y ahora \ntiene un {nueva_vida}% de vida!")
                            # recalcular vida de la potencia propietaria
                            if propietario:
                                propietario[0][3] = contar_vida_territorios_potencia(propietario[0][0])
                    
                    guardar_potencias()
                    guardar_vida_territorios()
                    refrescar_canvas()
                    actualizar_registro_ataque(potencia, ciud[0], coordenadas_para_registro)
                    return
        
    resultado_var.set("Impacto fallido")
    refrescar_canvas()


#============================
# dibujo
#============================

# dibuja los ejes verticales y horizontales de el mapa
def dibujar_ejes_y_cuadricula():
    x_left_c,  y_top_c = mundo_a_canvas(-ANCHO_MUNDO,  ALTO_MUNDO)
    x_right_c, y_bot_c = mundo_a_canvas( ANCHO_MUNDO, -ALTO_MUNDO)
    x0_c, y0_c = mundo_a_canvas(0, 0)

    canvas.create_line(x_left_c, y0_c, x_right_c, y0_c, width=2, fill="blue")
    canvas.create_line(x0_c, y_top_c, x0_c, y_bot_c, width=2, fill="blue")

    paso = 10
    for x in range(-ANCHO_MUNDO, ANCHO_MUNDO +1, paso):
        cx, _ = mundo_a_canvas(x, 0)
        canvas.create_line(cx, y_top_c, cx, y_bot_c, fill="#e0e0e0")
        canvas.create_text(cx, y0_c - 290, text=str(f"{x}°"), anchor="n", font=("Arial", 8))

    for y in range(-ALTO_MUNDO, ALTO_MUNDO +1, paso):
        _, cy = mundo_a_canvas(0, y)
        canvas.create_line(x_left_c, cy, x_right_c, cy, fill="#e0e0e0")
        canvas.create_text(x0_c -545, cy, text=str(f"{y}°"), anchor="e", font=("Arial", 8))

# dibuja el mapa en sí, cada uno de los territorios
def dibujar_mapa():
    for pais in MAPA:
        for provincia in pais[3:]:
            for ciudad in provincia[1]:
                
                # aqui tienen que ir los puntos de los territorios, y convertirlas a coordenadas XY
                rect = normalizar_rectangulo(ciudad[1][0], ciudad[1][1])
                xmin,xmax,ymin,ymax = rect
                xmin, ymin = convertir_a_xy_mapa(xmin, ymin)
                xmax, ymax = convertir_a_xy_mapa(xmax, ymax)
                x1_c, y1_c = mundo_a_canvas(xmin,ymin)
                x2_c, y2_c = mundo_a_canvas(xmax,ymax)
                x_min_c, x_max_c = min(x1_c, x2_c), max(x1_c, x2_c)
                y_min_c, y_max_c = min(y1_c, y2_c), max(y1_c, y2_c)

                canvas.create_rectangle(
                    x_min_c, y_min_c, x_max_c, y_max_c,
                    outline = "#1f77b4",
                    width = 2,
                    fill = "#cfe8ff"
                )
                cx = (x_min_c + x_max_c) /2
                cy = (y_min_c + y_max_c) /2
                canvas.create_text(cx,cy, text = ciudad[0], font=("Arial", 10, "bold"))

# dibuja el pundo rojo en donde se ataca en el mapa
def dibujar_disparo():
    if ultimo_disparo is None:
        return
    x, y = ultimo_disparo
    cx, cy = mundo_a_canvas(x, y)
    r = 4

    canvas.create_oval(cx - r, cy - r, cx + r, cy + r, fill = "red", outline = "")
    canvas.create_line(cx - 8, cy, cx + 8, cy, fill = 'red', width = '2')
    canvas.create_line(cx, cy - 8, cx, cy + 8, fill = 'red', width = '2')

# vuelve a cargar el mapa para actualizar cambios
def refrescar_canvas():
    canvas.delete("all")
    dibujar_ejes_y_cuadricula()
    dibujar_mapa()
    dibujar_disparo()


# ======================
# cargar 
# ======================

# llama todo lo que tiene que ser cargado para el funcionamiento del juego
mapa_se_traslapa()
if vida_territorios[0] == 0:
    asignar_vida_territorios()
cargar_potencias()
cargar_vida_territorios()
cargar_registro()


#============================
# IU
#============================

# construye cuando hay que dar feedback de una confirmación al usuario
def construir_confirmacion(msj="Ha ocurrido un tarea realizada con éxito"):
    global root
    win = tk.Toplevel(root)
    win.geometry("400x200")
    win.title("Confirmación")
    
    contenedor = tk.Frame(win)
    contenedor.pack(fill='both', expand=False, padx=10, pady=10)
    panel = tk.Frame(contenedor)
    panel.pack(fill="y", padx=(0,10))

    tk.Label(panel, text=msj, font=("Arial", 12)).pack(anchor='w', pady=20)
    tk.Button(panel, text="Cerrar", command=win.destroy, font=("Arial", 10, "bold"), fg="white", bg="#ff0000").pack(anchor='se', pady=10)

# ventana añadir potencia
def construir_anadir_potencia():
    global root, entrada_potencia
    win = tk.Toplevel(root)
    win.geometry("400x200")
    win.title("Añadir nueva potencia")

    contenedor = tk.Frame(win)
    contenedor.pack(fill='both', expand=False, padx=10, pady=10)
    panel = tk.Frame(contenedor)
    panel.pack(fill='y', padx=(0,10))

    tk.Label(panel, text="Ingrese el nombre de la nueva potencia", font=("Arial", 10)).pack(anchor="se", pady=10)
    entrada_potencia = tk.Entry(panel, width=25); entrada_potencia.pack(anchor='w', pady=10)
    tk.Button(panel, text="Aceptar", command=anadir_potencias, font=("Arial", 10)).pack(anchor="w", pady=10)
    tk.Button(panel, text="Cerrar", command=win.destroy, font=("Arial", 10, "bold"), fg="white", bg="#ff0000").pack(anchor='se', pady=10)

# ventana de reclamar territorio
def construir_reclamar_territorio():
    global root, entrada_potencia_r, entrada_territorio
    win = tk.Toplevel(root)
    win.geometry("600x300")
    win.title("Reclamar territorio")
    
    contenedor = tk.Frame(win)
    contenedor.pack(fill='both', expand=False, padx=10, pady=10)
    panel = tk.Frame(contenedor)
    panel.pack(fill="y", padx=(0,10))

    tk.Label(panel, text="Ingrese el nombre de la potencia y la ciudad que reclama", font=("Arial", 12)).pack(anchor='w', pady=20)
    entrada_potencia_r = tk.Entry(panel, width=25); entrada_potencia_r.pack(anchor='w', pady=10)
    entrada_territorio = tk.Entry(panel, width=25); entrada_territorio.pack(anchor='w', pady=10)
    tk.Button(panel, text="Aceptar", font=("Arial", 10), command=reclamar_territorio).pack(anchor="w", pady=10)
    tk.Button(panel, text="Cerrar", command=win.destroy, font=("Arial", 10, "bold"), fg="white", bg="#ff0000").pack(anchor='se', pady=10)

# ventana para cambiar de estado a la potencia
def construir_cambiar_estado():
    global root, entrada_potencia

    win = tk.Toplevel(root)
    win.geometry("450x250")
    win.title("Cambiar estado")

    contenedor = tk.Frame(win)
    contenedor.pack(fill='both', expand=False, padx=10, pady=10)
    panel = tk.Frame(contenedor)
    panel.pack(fill="y", padx=(0,10))

    tk.Label(panel, text="Ingrese la potencia que cambia de estado", font=("Arial", 12)).pack(anchor='w', pady=20)
    entrada_potencia = tk.Entry(panel, width=25); entrada_potencia.pack(anchor='w', pady=10)
    tk.Button(panel, text="Aceptar", font=("Arial", 10), command=cambiar_estado).pack(anchor="w", pady=10)

    tk.Button(panel, text="Cerrar", command=win.destroy, font=("Arial", 10, "bold"), fg="white", bg="#ff0000").pack(anchor='se', pady=10)

# ventana para mostrar las potencias
def construir_mostrar_potencias():
    global root
    win = tk.Toplevel(root)
    win.title("Estado de las potencias")
    # win.geometry("400x400")
    
    contenedor = tk.Frame(win)
    contenedor.pack(fill='both', expand=False, padx=10, pady=10)
    panel = tk.Frame(contenedor)
    panel.pack(fill="y", padx=(0,10))

    tk.Label(panel, text="Estado de las potencias:", font=("Arial", 12, "bold")).pack(anchor='w', pady=20)

    if not potencias:
        tk.Label(panel, text="No hay potencias registradas", font=("Arial", 10)).pack(anchor='w', pady=10)
        tk.Button(panel, text="Cerrar", command=win.destroy, font=("Arial", 10, "bold"), fg="white", bg="#ff0000").pack(anchor='se', pady=10)

        return
    
    for pots in potencias:
        nombre = pots[0][0]
        estado = "Activo" if pots[0][1] else "Inactivo"
        indicador = "Vivo" if pots[0][2] else "Derrotada"
        
        info_text = (f"Nombre: {nombre}\n"
                     f"Estado: {estado}\n"
                     f"Indicador: {indicador}\n"
        )
        
        tk.Label(panel, text=info_text, justify="left", font=("Arial", 10)).pack(anchor='w', pady=10)
    
    tk.Button(panel, text="Cerrar", command=win.destroy, font=("Arial", 10, "bold"), fg="white", bg="#ff0000").pack(anchor='se', pady=10)

# ventana de la inicialización de la vida de los territorios
def construir_inicializar_vida_territorios():
    global root, territorios_iniciados
    win = tk.Toplevel(root)
    win.geometry("400x200")
    win.title("Inicializar territorios")

    territorios_iniciados = True
    asignar_vida_territorios()
    
    contenedor = tk.Frame(win)
    contenedor.pack(fill='both', expand=False, padx=10, pady=10)
    panel = tk.Frame(contenedor)
    panel.pack(fill="y", padx=(0,10))

    tk.Label(panel, text="Territorios inicializados con éxito", font=("Arial", 12)).pack(anchor='w', pady=20)
    tk.Button(panel, text="Cerrar", command=win.destroy, font=("Arial", 10, "bold"), fg="white", bg="#ff0000").pack(anchor='se', pady=10)

# ventada que muestra la vida de los territorios
def construir_mostrar_vida_territorios():
    global root, vida_territorios
    win = tk.Toplevel(root)
    win.title("Vida de los territorios")
    
    contenedor = tk.Frame(win)
    contenedor.pack(fill='both', expand=False, padx=10, pady=10)

    panel_izq = tk.Frame(contenedor)
    panel_izq.pack(side='left', fill="both", padx=(0,10))
    panel_der = tk.Frame(contenedor)
    panel_der.pack(side='right', fill="both", padx=(0,10))
        
    for i, ter in enumerate(vida_territorios[1:]):
        panel = panel_izq if i % 2 == 0 else panel_der
        nombre = ter[0]
        vida = ter[1]
        
        info_text = f"Nombre: {nombre} - Vida: {vida}%"
        
        tk.Label(panel, text=info_text, justify="left", font=("Arial", 10)).pack(anchor='w', pady=5)
    
    tk.Button(panel, text="Cerrar", command=win.destroy, font=("Arial", 10, "bold"), fg="white", bg="#ff0000").pack(anchor='se', pady=10)

# ventana del status de una potencia
def construir_status_potencia():
    global root, entrada_potencia, status_var
    win = tk.Toplevel(root)
    win.geometry("400x380")
    win.title("Estado de la potencia")

    contenedor = tk.Frame(win)
    contenedor.pack(fill='both', expand=False, padx=10, pady=10)
    panel = tk.Frame(contenedor)
    panel.pack(fill='y', padx=(0,10))

    tk.Label(panel, text="Ingrese el nombre de la potencia", font=("Arial", 10)).pack(anchor="se", pady=10)
    entrada_potencia = tk.Entry(panel, width=25); entrada_potencia.pack(anchor='w', pady=10)
    tk.Button(panel, text="Aceptar", command=generar_status_potencia, font=("Arial", 10)).pack(anchor="w", pady=10)
    tk.Button(panel, text="Cerrar", command=win.destroy, font=("Arial", 10, "bold"), fg="white", bg="#ff0000").pack(anchor='se', pady=10)
    status_var = tk.StringVar(master=root, value="")
    tk.Label(panel, textvariable=status_var, font=("Arial", 11, "bold")).pack(anchor="n", pady=(4,0))

# ventana para la compra de misiles
def construir_comprar_misiles():
    global root, entrada_potencia, entrada_cantidad_misiles
    win = tk.Toplevel(root)
    win.geometry("400x300")
    win.title("Menú comprar misiles")

    contenedor = tk.Frame(win)
    contenedor.pack(fill='both', expand=False, padx=10, pady=10)
    panel = tk.Frame(contenedor)
    panel.pack(fill='y', padx=(0,10))

    tk.Label(panel, text="Ingrese el nombre de la potencia", font=("Arial", 10)).pack(anchor="se", pady=10)
    entrada_potencia = tk.Entry(panel, width=25); entrada_potencia.pack(anchor='w', pady=10)
    tk.Label(panel, text="Ingrese la cantidad de misiles a comprar", font=("Arial", 10)).pack(anchor="se", pady=10)
    entrada_cantidad_misiles = tk.Entry(panel, width=25); entrada_cantidad_misiles.pack(anchor='w', pady=10)
    tk.Button(panel, text="Aceptar", command=comprar_misiles, font=("Arial", 10)).pack(anchor="w", pady=10)
    tk.Button(panel, text="Cerrar", command=win.destroy, font=("Arial", 10, "bold"), fg="white", bg="#ff0000").pack(anchor='se', pady=10)

# ventana de el rank por territorio
def construir_ranking_territorio():
    global root

    win = tk.Toplevel(root)
    win.geometry("400x400")
    win.title("Menú comprar misiles")

    contenedor = tk.Frame(win)
    contenedor.pack(fill='both', expand=False, padx=10, pady=10)
    panel = tk.Frame(contenedor)
    panel.pack(fill='y', padx=(0,10))

    lista_rank = rank_extension()

    for i, potencia in enumerate(lista_rank):
        tk.Label(panel, text=f"{i+1}. {potencia.capitalize()}", justify="left", font=("Arial", 10)).pack(anchor='w', pady=5)
        
    tk.Button(panel, text="Cerrar", command=win.destroy, font=("Arial", 10, "bold"), fg="white", bg="#ff0000").pack(anchor='se', pady=10)

# ventana de el rank por vida
def construir_ranking_porcentaje():
    global root

    win = tk.Toplevel(root)
    win.geometry("400x400")
    win.title("Menú comprar misiles")

    contenedor = tk.Frame(win)
    contenedor.pack(fill='both', expand=False, padx=10, pady=10)
    panel = tk.Frame(contenedor)
    panel.pack(fill='y', padx=(0,10))

    lista_rank = rank_porcentaje()

    for i, potencia in enumerate(lista_rank):
        tk.Label(panel, text=f"{i+1}. {potencia.capitalize()}", justify="left", font=("Arial", 10)).pack(anchor='w', pady=5)
        
    tk.Button(panel, text="Cerrar", command=win.destroy, font=("Arial", 10, "bold"), fg="white", bg="#ff0000").pack(anchor='se', pady=10)

# ventana para mostrar el registro de actividades
def construir_mostrar_registro():
    global root, lista_registro

    win = tk.Toplevel(root)
    # win.geometry('400x150')
    win.title("Registro de actividades")

    contenedor = tk.Frame(win)
    contenedor.pack(fill="both", expand=False, padx=10, pady=10)
    panel_izq = tk.Frame(contenedor)
    panel_izq.pack(side='left', fill="both", padx=(0,10))
    panel_der = tk.Frame(contenedor)
    panel_der.pack(side='right', fill="both", padx=(0,10))

    info_text = ''

    try:
        p = lista_registro[0]
        for i, reg in enumerate(lista_registro):
            panel = panel_izq if i % 2 == 0 else panel_der
            match reg[1][0]:
                case 0:
                    info_text = f"{reg[0][0]} - ATAQUE {reg[2][0]} en {reg[3][0]}, atinó a {reg[4][0]}, pasó a {reg[5][0]}%"
                case 1:
                    info_text = f"{reg[0][0]} - COMPRA {reg[2][0]} compró {reg[3][0]} misiles"
                case 2:
                    info_text = f"{reg[0][0]} - CAMBIO {reg[2][0]} cambió a {reg[3][0]}"
                case 3:
                    info_text = f"{reg[0][0]} - MUERTE {reg[2][0]}"
                case 4:
                    info_text = f"{reg[0][0]} - TERRITORIO {reg[2][0]} bajó a {reg[3][0]}"
            
            tk.Label(panel, text=info_text, justify="left", font=("Arial", 10)).pack(anchor='w', pady=5)
    except:
        tk.Label(panel_izq, text="No hay registro de actividades", justify="left", font=("Arial", 11, "bold")).pack(anchor='w', pady=15, padx=10)

    tk.Button(panel_der, text="Cerrar", command=win.destroy, font=("Arial", 10, "bold"), fg="white", bg="#ff0000").pack(anchor='se', pady=10)

# ventana para reiniciar el juego
def construir_reiniciar_juego():
    global root, potencias

    reiniciar_juego()
    
    win = tk.Toplevel(root)
    win.geometry("500x150")
    win.title("Reiniciar juego")
    
    contenedor = tk.Frame(win)
    contenedor.pack(fill='both', expand=False, padx=10, pady=10)
    panel = tk.Frame(contenedor)
    panel.pack(fill="y", padx=(0,10))

    tk.Label(panel, text="Las potencias han sido reiniciadas, la vida ha sido\nreestablecida y se ha limpiado el registro", font=("Arial", 12)).pack(anchor='w', pady=20)
    tk.Button(panel, text="Cerrar", command=win.destroy, font=("Arial", 10, "bold"), fg="white", bg="#ff0000").pack(anchor='se', pady=10)

# ventana que muesta el mapa del juego
def construir_mapa():
    global root, entrada_x, entrada_y, resultado_var, canvas, entrada_x1, entrada_x2, entrada_x3, entrada_y1, entrada_y2, entrada_y3, entrada_potencia, vida_territorios

    if mapa_se_traslapa() == False:
        construir_error("Error: Hay territorios que se traslapan en el mapa.")
        return


    win = tk.Toplevel(root)
    win.title("Mapa de territorios")

    contenedor = tk.Frame(win)
    contenedor.pack(fill='both', expand=True, padx=10, pady=10)
    panel_izq = tk.Frame(contenedor)
    panel_izq.pack(side="left", fill="y", padx=(0,10))

    fila_potencia = tk.Frame(panel_izq); fila_potencia.pack(anchor="w", pady=4)
    tk.Label(fila_potencia, text="Ingrese la potencia atacante", font=("Arial", 12, "bold")).pack(anchor="w", pady=(0,8))
    entrada_potencia = tk.Entry(fila_potencia, width=15); entrada_potencia.pack(anchor="w", side='left'); entrada_potencia.insert(0, "Potencia")

    tk.Label(panel_izq, text="Coordenadas del disparo", font=("Arial", 12, "bold")).pack(anchor="se", pady=(0,8))

    fila_x = tk.Frame(panel_izq); fila_x.pack(anchor="w", pady=4)
    tk.Label(fila_x, text="X: ").pack(side="left")
    # entrada_x = tk.Entry(fila_x, width=5); entrada_x.pack(side='left'); entrada_x.insert(0, "0")
    entrada_x1 = tk.Entry(fila_x, width=5); entrada_x1.pack(side='left'); entrada_x1.insert(0, "0")
    entrada_x2 = tk.Entry(fila_x, width=5); entrada_x2.pack(side='left'); entrada_x2.insert(0, "0")
    entrada_x3 = tk.Entry(fila_x, width=5); entrada_x3.pack(side='left'); entrada_x3.insert(0, "0")

    fila_y = tk.Frame(panel_izq); fila_y.pack(anchor="w", pady=4)
    tk.Label(fila_y, text='Y: ').pack(side="left")
    # entrada_y = tk.Entry(fila_y, width=5); entrada_y.pack(side='left'); entrada_y.insert(0, '0')
    entrada_y1 = tk.Entry(fila_y, width=5); entrada_y1.pack(side='left'); entrada_y1.insert(0, '0')
    entrada_y2 = tk.Entry(fila_y, width=5); entrada_y2.pack(side='left'); entrada_y2.insert(0, '0')
    entrada_y3 = tk.Entry(fila_y, width=5); entrada_y3.pack(side='left'); entrada_y3.insert(0, '0')

    # entrada_x, entrada_y = coordenadas_a_xy()

    tk.Button(panel_izq,text="Disparar", command=disparar).pack(anchor="w", pady=10)
    resultado_var = tk.StringVar(master=root, value="Listo para disparar en (0,0).")
    tk.Label(panel_izq, textvariable=resultado_var, fg='blue').pack(anchor="w", pady=(4,0))
    tk.Button(panel_izq, text="Cerrar", command=win.destroy, font=("Arial", 10, "bold"), fg="white", bg="#ff0000").pack(anchor="se", pady=20)


    panel_der = tk.Frame(contenedor)
    panel_der.pack(side="left", fill="both", expand=True)

    ancho_canvas = MARGEN *2 + (ANCHO_MUNDO *2) * ESCALA
    alto_canvas = MARGEN *2 + (ALTO_MUNDO *2) * ESCALA
    canvas_local = tk.Canvas(panel_der, width=ancho_canvas, height=alto_canvas, bg="white")
    canvas_local.pack(fill="both", expand=True)

    globals()["canvas"] = canvas_local
    refrescar_canvas()
    
# ventana que muesta el menú principal, este es el root
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
    tk.Button(panel_izq,text='Mostrar Mapa', command=construir_mapa, width=tamano_botones[0], height=tamano_botones[1], bg="#badaff").pack(anchor='w', padx=10, pady=10)
    tk.Button(panel_izq,text='Añadir potencia', command=construir_anadir_potencia, width=tamano_botones[0], height=tamano_botones[1], bg="#c5fffa").pack(anchor='w', padx=10, pady=10)
    tk.Button(panel_izq,text='Reclamar Territorio', command=construir_reclamar_territorio, width=tamano_botones[0], height=tamano_botones[1], bg="#c5fffa").pack(anchor='w', padx=10, pady=10)
    tk.Button(panel_izq,text='Comprar misiles', command=construir_comprar_misiles, width=tamano_botones[0], height=tamano_botones[1], bg="#c5fffa").pack(anchor='w', padx=10, pady=10)
    tk.Button(panel_izq,text='Cambiar estado', command=construir_cambiar_estado, width=tamano_botones[0], height=tamano_botones[1], bg="#c5fffa").pack(anchor='w', padx=10, pady=10)
    tk.Button(panel_izq,text='Reiniciar juego', command=construir_reiniciar_juego, font=("Arial",8, "bold"), width=tamano_botones[0], height=tamano_botones[1], bg="#ffb2b2").pack(anchor='w', padx=10, pady=10)
    tk.Button(panel_der,text='Ver Registro', command=construir_mostrar_registro, width=tamano_botones[0], height=tamano_botones[1], bg="#fffebf").pack(anchor='w', padx=10, pady=10)
    tk.Button(panel_der,text='Mostrar Potencias', command=construir_mostrar_potencias, width=tamano_botones[0], height=tamano_botones[1], bg="#b2ffab").pack(anchor='w', padx=10, pady=10)
    tk.Button(panel_der,text='Status Potencia', command=construir_status_potencia, width=tamano_botones[0], height=tamano_botones[1], bg="#b2ffab").pack(anchor='w', padx=10, pady=10)
    tk.Button(panel_der,text='Mostrar vida territorios', command=construir_mostrar_vida_territorios, width=tamano_botones[0], height=tamano_botones[1], bg="#b2ffab").pack(anchor='w', padx=10, pady=10)
    tk.Button(panel_der,text='Ranking territorio', command=construir_ranking_territorio, width=tamano_botones[0], height=tamano_botones[1], bg="#fbd1ff").pack(anchor='w', padx=10, pady=10)
    tk.Button(panel_der,text='Ranking porcentaje', command=construir_ranking_porcentaje, width=tamano_botones[0], height=tamano_botones[1], bg="#fbd1ff").pack(anchor='w', padx=10, pady=10)
    tk.Button(panel_der, text="Cerrar", command=root.destroy, font=("Arial", 10, "bold"), fg="white", bg="#ff0000").pack(anchor='se', pady=20)

    root.mainloop()
    

# activa la ventana principal (menú)
if __name__ == "__main__":
    construir_menu()

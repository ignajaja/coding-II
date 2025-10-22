import tkinter as tk
import json, os
import json, os


# BUSCAR -error PARA TERMINAR EL CODIGO


# ====================
# constantes globales
# ====================
"""
- ANCHO_MUNDO
- ALTO_MUNDO
- ESCALA
- MARGEN
- MAPA
"""

ANCHO_MUNDO = 180
ALTO_MUNDO = 90
ESCALA = 3
MARGEN = 30

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
                ["Perez Zeledón", [[[-170, 0, 0],[-75, 0, 0]], [[-98, 0, 0],[-35, 0, 0]]]],
                ["Escazu", [[[-167, 0, 0],[-18, 0, 0]], [[-155, 0, 0],[-28, 0, 0]]]]
            ]
        ]
    ],
    [
        "Colombia", 100, 100000,
        [
            "Antioquia", [
                ["Medellin", [[[-30, 0, 0],[50, 0, 0]], [[-50, 0, 0],[70, 0, 0]]]],
                ["Bello", [[[-45, 0, 0],[47, 0, 0]], [[-20, 0, 0],[42, 0, 0]]]]
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
                ["Milán", [[[80, 0, 0],[-56, 0, 0]], [[57, 0, 0],[-40, 0, 0]]]],
            ]
        ]
    ],
    [
        "Alemania", 100, 120000,
        [
            "Baviera", [
                ["Múnich", [[[160, 0, 0],[55, 0, 0]], [[125, 0, 0],[40, 0, 0]]]],
                ["Núremberg", [[[118, 0, 0],[88, 0, 0]], [[80, 0, 0],[65, 0, 0]]]]
            ]
        ],
        [
            "Renania", [
                ["Colonia", [[[75, 0, 0],[80, 0, 0]], [[60, 0, 0],[60, 0, 0]]]],
                ["Düsseldorf", [[[148, 0, 0],[82, 0, 0]], [[179, 0, 0],[62, 0, 0]]]],
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

# lista de potencias
potencias = []
vida_territorios = []

# para la IU
root = None
entrada_x = None
entrada_y = None
entrada_x1 = entrada_x2 = entrada_x3 = entrada_y1 = entrada_y2 = entrada_y3 = None
resultado_var = None
canvas = None

# para disparos
ultimo_disparo = None


#============================
# commons
#============================
"""
- coordenadas_a_xy
- convertir_a_xy_mapa
- mundo_a_canvas
- normalizar_rectangulo
- contar_extension
- reducir_vida_territorio
"""

# coordenadas a xy solo recibe entradas de tipo entry
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


def convertir_a_xy_mapa(coord_x, coord_y):
    x1 = coord_x[0]; x2 = coord_x[1]; x3 = coord_x[2]
    y1 = coord_y[0]; y2 = coord_y[1]; y3 = coord_y[2]
    
    sign_x = -1 if x1 < 0 else 1
    sign_y = -1 if y1 < 0 else 1
    
    cx = sign_x * (abs(x1) + x2 / 6 + x3 / 360)
    cy = sign_y * (abs(y1) + y2 / 6 + y3 / 360)
    
    return cx, cy


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
        
    xmin = x1 if x1[0] < x2[0] else x2
    xmax = x1 if x1[0] > x2[0] else x2
    ymin = y1 if y1[0] < y2[0] else y2
    ymax = y1 if y1[0] > y2[0] else y2
    
    return xmin, xmax, ymin, ymax

def punto_en_rectangulo(x,y,rect):
    # dice si un pundo está dentro del rectángulo
    xmin,xmax,ymin,ymax = rect
    return ((xmin) <= x <= xmax) and (ymin <= y <= ymax) # true si le da a el rectángulo, false si no


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


def asignar_vida_territorios():
    global potencias, vida_territorios

    for pais in MAPA:
        for region in pais[3:]:
            for ciudad in region[1]:
                vida_territorios.append([ciudad[0], 100])

    return


def destruir_territorio(nombre):
    global potencias, vida_territorios
    
    copia = []
    
    for ter in vida_territorios:
        if not ter[0] == nombre:
            copia.append(ter)
    
    vida_territorios = copia
    
    for pots in potencias:
        nueva_lista = []
        for ter in pots[1]:
            if not ter[0] == nombre:
                nueva_lista.append(ter)
        pots[1] = nueva_lista
        
    guardar_vida_territorios()
    guardar_potencias()
    return


def reducir_vida_territorio(territorio):
    global vida_territorios
    
    for pais in MAPA:
        for region in pais[3:]:
            for ciudad in region[1]:
                
                if ciudad[0] == territorio:
                    for ter in vida_territorios:
                        
                        if ter[0] == territorio:
                            ter[1] -= 10
                            # if ter[1] == 0:
                            #     destruir_territorio(ter[0])    
    
    return

def verificar_vida_potencia():
    global potencias, vida_territorios

    for pots in potencias:
        # pots expected shape: [meta, territories...] or [meta] if no territories
        territorios = pots[1] if len(pots) > 1 else []
        cantidad_territorios = 0

        for territorio in territorios:
            # territorio expected to be a list whose first element is the territory name
            nombre_terr = territorio[0]
            for ter in vida_territorios:
                if ter[0] == nombre_terr:
                    cantidad_territorios += 1
                    break

        if cantidad_territorios == 0:
            pots[0][2] = False  # set indicador_pot to False (defeated)
        # if cantidad_territorios == 0 -> skip (power has no surviving territories)

        
    
#============================
# lógica potencias
#============================
"""
- guardar_potencias
- cargar_potencias
- reclamar_territorio
- anadir_potencias
- generar_status_potencia
"""

# guardar a memoria
def guardar_potencias():
    global potencias
    try:
        with open("potencias.txt", "w") as f:
            json.dump(potencias, f) # 
    except Exception as exc:
        print("Error al guardar potencias:", exc)


# cargar de memoria
def cargar_potencias():
    global potencias

    try:
        with open("potencias.txt", "r", encoding="utf-8") as f:
            potencias = json.load(f)
    except Exception as exc:
        print("Error al cargar potencias:", exc)


# función para asignarle el territorio a una potencia
def reclamar_territorio(nombre, territorio):
    global potencias
    
    for pais in MAPA:
        for region in pais[3:]:
            for ciudad in region[1]:
                if ciudad[0] == territorio:
                    territorio = ciudad # busca el territorio por nombre

    
    for pots in potencias:
        if pots[0][0] == nombre: # si encuentra el nombre del territorio, se le asigna a la potencia
            pots.append(territorio)
    
    guardar_potencias()
    return


# función para añadir una potencia nueva al juego
def anadir_potencias(nombre):
    global potencias
    
    for pot in potencias:
        if nombre == pot[0][0]:
            # aqui salta -error cuando existe otra potencia con el mismo nombre
            return
    
    estado_pot = True # está activo o inactivo
    indicador_pot = True # está vivo o no
    por_vida_pot = 100 # vida restante
    can_misiles_pot = 1000
    can_disparos_pot = 0 # cantidad de ataques enviados
    can_recibidos_pot = 0 # cantidad de ataques recibidos

    potencias.append([[nombre, estado_pot, indicador_pot, por_vida_pot, can_misiles_pot, can_disparos_pot, can_recibidos_pot]])
    
    return


# genera el status de la potencia pedida
def generar_status_potencia(nombre):
    global potencias
    
    result = []
    
    extension_territorios = 0
    
    for pots in potencias:
        if pots[0][0] == nombre:
            
            # for territorio in pots[1]:
            try:
                for territorio in pots[1]:
                    extension_territorios += contar_extension(territorio)
            except:
                # aqui salta -error si no tiene territorios
                True
            # print(f"Nombre: {pots[0][0]}, Estado: {"Activo" if pots[0][1] == True else "Inactivo"}, Indicador: {"Vivo" if pots[0][2] == True else "Derrotada"}, Vida: {pots[0][3]}, Misiles: {pots[0][4]}, Disparos tirados: {pots[0][5]}, Disparos recibidos: {pots[0][6]}, Extensión en km^2: {extension_territorios}")
            
            # aqui va la ventana que muestra el status de la potencia -error
    
    return


def cambiar_estado(nombre, estado):
    global potencias
    
    for pots in potencias:
        if pots[0][0] == nombre:
            pots[0][1] = True if estado == "Activo" else False
            
    return

# def comprar_misiles(nombre, cantidad):
#     global potencias
    
#     for pots in potencias:
#         if pots[0][0] == nombre:


#============================
# lógica de disparo
#============================
"""
- disparar
- guardar_vida_territorios
- cargar_vida_territorios
"""

def guardar_vida_territorios():
    global vida_territorios
    
    try:
        with open("vida_territorios.txt", "w") as f:
            json.dump(vida_territorios, f) # 
    except Exception as exc:
        print("Error al guardar vida_territorios:", exc)
    return

# cargar de memoria
def cargar_vida_territorios():
    global vida_territorios

    try:
        with open("vida_territorios.txt", "r", encoding="utf-8") as f:
            vida_territorios = json.load(f)
    except Exception as exc:
        print("Error al cargar vida_territorios:", exc)
    return
        

    

def disparar():
    global ultimo_disparo
    punto_x = punto_y = 0
    try:
        x, y = coordenadas_a_xy(entrada_x1, entrada_x2,entrada_x3, entrada_y1, entrada_y2, entrada_y3)
        
    except ValueError:
        resultado_var.set("Ingrese un dato válido")
        return
    
    ultimo_disparo = (x, y)

    if not (-ANCHO_MUNDO <= x <= ANCHO_MUNDO and -ALTO_MUNDO <= y <= ALTO_MUNDO):
        resultado_var.set("Fuera del mapa")
        refrescar_canvas()
        return
    
    # for nombre, puntos in MAPA:
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
                    reducir_vida_territorio(ciud[0])
                    for territorio in vida_territorios:
                        if territorio[0] == ciud[0]:
                            resultado_var.set(f"Impacto a {pais[0]},\n {prov[0]}, {ciud[0]} y ahora \ntiene un {territorio[1]}% de vida!")
                        if territorio[1] == 0:
                            resultado_var.set(f"La ciudad de\n{pais[0]}, {prov[0]},\n{ciud[0]} ha sido destruida")
                            destruir_territorio(ciud[0])
                    
                    guardar_vida_territorios()
                    refrescar_canvas()
                    return
        
    resultado_var.set("Impacto fallido")
    refrescar_canvas()


#============================
# dibujo
#============================
"""
- dibujar_ejes_y_cuadricula
- dibujar_mapa
- dibujar_disparo
- refrescar_canvas
"""

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
        # if not x == 0:
        canvas.create_text(cx, y0_c - 290, text=str(f"{x}°"), anchor="n", font=("Arial", 8))

    for y in range(-ALTO_MUNDO, ALTO_MUNDO +1, paso):
        _, cy = mundo_a_canvas(0, y)
        canvas.create_line(x_left_c, cy, x_right_c, cy, fill="#e0e0e0")
        # if not y == 0:
        canvas.create_text(x0_c -545, cy, text=str(f"{y}°"), anchor="e", font=("Arial", 8))


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


def dibujar_disparo():
    if ultimo_disparo is None:
        return
    x, y = ultimo_disparo
    cx, cy = mundo_a_canvas(x, y)
    r = 4

    canvas.create_oval(cx - r, cy - r, cx + r, cy + r, fill = "red", outline = "")
    canvas.create_line(cx - 8, cy, cx + 8, cy, fill = 'red', width = '2')
    canvas.create_line(cx, cy - 8, cx, cy + 8, fill = 'red', width = '2')


def refrescar_canvas():
    canvas.delete("all")
    dibujar_ejes_y_cuadricula()
    dibujar_mapa()
    dibujar_disparo()


# ======================
# cargar 
# ======================


cargar_potencias()
asignar_vida_territorios()
cargar_vida_territorios()
# reducir_vida_territorio("Roma")
# destruir_territorio("Pisa")

# print(vida_territorios)
#============================
# IU
#============================
"""
- construir_iu
"""

def construir_iu():
    global root, entrada_x, entrada_y, resultado_var, canvas, entrada_x1, entrada_x2, entrada_x3, entrada_y1, entrada_y2, entrada_y3
    root = tk.Tk()
    root.title("Mapa cartesiano (cuadricula 18x9)")

    contenedor = tk.Frame(root)
    contenedor.pack(fill='both', expand=True, padx=10, pady=10)
    panel_izq = tk.Frame(contenedor)
    panel_izq.pack(side="left", fill="y", padx=(0,10))

    tk.Label(panel_izq, text="Coordenadas del disparo", font=("Arial", 12, "bold")).pack(anchor="w", pady=(0,8))

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
    resultado_var = tk.StringVar(value="Listo para disparar en (0,0).")
    tk.Label(panel_izq, textvariable=resultado_var, fg='blue').pack(anchor="w", pady=(4,0))

    panel_der = tk.Frame(contenedor)
    panel_der.pack(side="left", fill="both", expand=True)

    ancho_canvas = MARGEN *2 + (ANCHO_MUNDO *2) * ESCALA
    alto_canvas = MARGEN *2 + (ALTO_MUNDO *2) * ESCALA
    canvas_local = tk.Canvas(panel_der, width=ancho_canvas, height=alto_canvas, bg="white")
    canvas_local.pack(fill="both", expand=True)

    globals()["canvas"] = canvas_local
    refrescar_canvas()
    root.mainloop()

if __name__ == "__main__":
    construir_iu()


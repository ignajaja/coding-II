import tkinter as tk

# 180x90px
# ajustar 0,0 para que esté en el medio

# constantes globales
ANCHO_MUNDO = 180
ALTO_MUNDO = 90
ESCALA = 3
MARGEN = 30

# MAPA = [
#     ["Japón",       [[ 10,  60], [ 30,  40]]],
#     ["Costa Rica",  [[-60,  10], [-30,  30]]],
#     ["Kenia",       [[ 30, -40], [ 60, -20]]],
#     ["España",      [[-70, -60], [-40, -40]]],
#     ["Iceland",     [[-90,  70], [-60, 60]]], 
# ]


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
        "Italia", 120, 110000,
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
        "Alemania", 130, 120000,
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
        "Australia", 150, 130000, 
        [
            "Nueva Gales del Sur", [
                ["Sídney", [[[135, 0, 0],[-20, 0, 0]], [[180, 0, 0],[-90, 0, 0]]]],
        ]
        ]
    ]
]


# varialbes globales
# para la IU
root = None
entrada_x = None
entrada_y = None
entrada_x1 = entrada_x2 = entrada_x3 = entrada_y1 = entrada_y2 = entrada_y3 = None
resultado_var = None
canvas = None

# no para la IU
ultimo_disparo = None

# lista de potencias
potencias = []


# commons

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


# lógica potencias

def anadir_potencias(nombre):
    global potencias
    nombre_pot = nombre # nombre de la potencia
    estado_pot = True # está activo o inactivo
    indicador_pot = True # está vivo o no
    por_vida_pot = 100 # vida restante
    can_disparos_pot = 0 # cantidad de ataques enviados
    can_recibidos_pot = 0 # cantidad de ataques recibidos

    potencias.append([nombre_pot,estado_pot,indicador_pot,por_vida_pot,can_disparos_pot,can_recibidos_pot])

# dibujo

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



# lógica de disparo

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
                    resultado_var.set(f"Impacto a {pais[0]},\n {prov[0]}, {ciud[0]}!")
                    refrescar_canvas()
                    return
        
    resultado_var.set("Impacto fallido")
    refrescar_canvas()


# IU

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


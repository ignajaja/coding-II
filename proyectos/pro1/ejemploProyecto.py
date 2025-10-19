import tkinter as tk



# =========================
# Configuración del "mundo"
# =========================
ANCHO_MUNDO = 100   # ahora va de -100 a 100, múltiplos de 10 visibles, poner 180 por ejemplo
ALTO_MUNDO  = 100   #poner 90 por ej
ESCALA = 3          # píxeles por unidad del mundo. Tamaño de cuadro
MARGEN = 30

# =========================
# Mapa global (ejemplo)
# =========================
MAPA = [
    ["Japón",       [[ 10,  60], [ 30,  40]]],   # Cuadrante I
    ["Costa Rica",  [[-60,  10], [-30,  30]]],   # Cuadrante II
    ["Kenia",       [[ 30, -40], [ 60, -20]]],   # Cuadrante IV
    ["España",      [[-70, -60], [-40, -40]]],   # Cuadrante III
    ["Iceland",     [[-90,  90], [-60, 60]]],   # Cuadrante II
]

# =========================
# Variables globales UI
# =========================
root = None  #ventana
entrada_x = None #todo el entry
entrada_y = None
resultado_var = None  #el label azul
canvas = None  #todo el objeto canvas del dibujo

# no UI
ultimo_disparo = None #capturar los valores del ultimo disparo


# =========================
# Commons de coordenadas
# =========================
#como el eje de tkinter el 0,0 empieza arriba izquierda, hay que llevarlo al centro
def mundo_a_canvas(xm, ym):
    ancho_canvas = MARGEN * 2 + (ANCHO_MUNDO * 2) * ESCALA
    alto_canvas  = MARGEN * 2 + (ALTO_MUNDO  * 2) * ESCALA
    cx_centro = ancho_canvas // 2
    cy_centro = alto_canvas  // 2

    cx = cx_centro + xm * ESCALA
    cy = cy_centro - ym * ESCALA
    return cx, cy

#si importar los puntos que me den, arriba abajo, der.izq, se normalizan que siempre
#sean los mismos: izquierda-arriba, derecha-abajo
#E: dos puntos [x1,y1]  [x2,y2]
#S: dos puntos pero izquierda-arriba, derecha-abajo
def normalizar_rectangulo(p1, p2):
    x1, y1 = p1
    x2, y2 = p2
    xmin = min(x1, x2)
    xmax = max(x1, x2)
    ymin = min(y1, y2)
    ymax = max(y1, y2)
    return xmin, ymin, xmax, ymax

#verifica si el disparo está entre el punto
def punto_en_rectangulo(x, y, rect):
    xmin, ymin, xmax, ymax = rect
    return (xmin <= x <= xmax) and (ymin <= y <= ymax) #x4


# =========================
# Dibujo
# =========================punt
def dibujar_ejes_y_cuadricula():
    x_left_c,  y_top_c    = mundo_a_canvas(-ANCHO_MUNDO,  ALTO_MUNDO)
    x_right_c, y_bot_c    = mundo_a_canvas( ANCHO_MUNDO, -ALTO_MUNDO)
    x0_c, y0_c            = mundo_a_canvas(0, 0)

    # Ejes principales: eje x y eje y
    canvas.create_line(x_left_c, y0_c, x_right_c, y0_c, width=2, fill="blue")
    canvas.create_line(x0_c, y_top_c, x0_c, y_bot_c, width=2, fill= "blue")

    # Cuadrícula de 10 en 10
    paso = 10
    #para pintar las líneas verticales
    for x in range(-ANCHO_MUNDO, ANCHO_MUNDO + 1, paso):
        cx, _ = mundo_a_canvas(x, 0)
        canvas.create_line(cx, y_top_c, cx, y_bot_c, fill="#e8e8e8")
        if x != 0:
            canvas.create_text(cx, y0_c + 12, text=str(x), anchor="n", font=("Arial", 8))

    for y in range(-ALTO_MUNDO, ALTO_MUNDO + 1, paso):
        _, cy = mundo_a_canvas(0, y)
        canvas.create_line(x_left_c, cy, x_right_c, cy, fill="#e8e8e8")
        if y != 0:
            canvas.create_text(x0_c - 10, cy, text=str(y), anchor="e", font=("Arial", 8))

    # Cuadrantes
    canvas.create_text(x0_c + 40, y0_c - 20, text="I", font=("Arial", 10, "bold"), fill="black")
    canvas.create_text(x0_c - 40, y0_c - 20, text="II", font=("Arial", 10, "bold"), fill="black")
    canvas.create_text(x0_c - 40, y0_c + 20, text="III", font=("Arial", 10, "bold"), fill="black")
    canvas.create_text(x0_c + 40, y0_c + 20, text="IV", font=("Arial", 10, "bold"), fill="black")


#recorre la lista de países y va creando los cuadros.
#siempre debe normalizar cada par de puntos y usar mundo_a_canvas para
#ubicar el punto en la coordenada tkinter
def dibujar_mapa():
    for nombre, puntos in MAPA:
        rect = normalizar_rectangulo(puntos[0], puntos[1]) #normaliza los puntos
        xmin, ymin, xmax, ymax = rect 
        x1_c, y1_c = mundo_a_canvas(xmin, ymin) #determina los puntos en el grafico
        x2_c, y2_c = mundo_a_canvas(xmax, ymax) #determina los puntos en el gráfico
        x_min_c, x_max_c = min(x1_c, x2_c), max(x1_c, x2_c) #los normaliza para create_rectangle
        y_min_c, y_max_c = min(y1_c, y2_c), max(y1_c, y2_c) #los normaliza para create_rectangle
        #punta el rectangulo
        canvas.create_rectangle(x_min_c, y_min_c, x_max_c, y_max_c,
                                outline="#1f77b4", width=2, fill="#cfe8ff")
        #determina la mitad del rectangulo y pone el nombre
        cx = (x_min_c + x_max_c) / 2
        cy = (y_min_c + y_max_c) / 2
        canvas.create_text(cx, cy, text=nombre, font=("Arial", 10, "bold"))

#ultimo_disparo es una variable global
def dibujar_disparo():
    if ultimo_disparo is None:
        return
    x, y = ultimo_disparo
    cx, cy = mundo_a_canvas(x, y) #obtiene el x,y del gráfico
    r = 4 #es el radio para que se vea redondo
    #punta un circulo rojo y una cruz con dos líneas
    canvas.create_oval(cx - r, cy - r, cx + r, cy + r, fill="red", outline="")
    canvas.create_line(cx - 8, cy, cx + 8, cy, fill="red", width=2)
    canvas.create_line(cx, cy - 8, cx, cy + 8, fill="red", width=2)

#para eliminar todo lo que se dibujó, y dibujarlo de nuevo
def refrescar_canvas():
    canvas.delete("all")
    dibujar_ejes_y_cuadricula()
    dibujar_mapa()
    dibujar_disparo()


# =========================
# Lógica del disparo
# =========================
def disparar():
    global ultimo_disparo
    #obtiene el valor de los inputs, con try except valida que estén bien, sean numeros
    try:
        x = float(entrada_x.get())
        y = float(entrada_y.get())
    except ValueError:
        resultado_var.set("Ingresa números válidos para X e Y.")
        return

    #ultimo disparo es la tupla x,y
    ultimo_disparo = (x, y)

    #si está fuera de los bordes, fuera el plano
    if not (-ANCHO_MUNDO <= x <= ANCHO_MUNDO and -ALTO_MUNDO <= y <= ALTO_MUNDO):
        resultado_var.set("Fuera del mapa.")
        refrescar_canvas()
        return

    #recorre todo el mapa buscando si el disparo se encuentra entre alguno
    #de los rectángulos
    for nombre, puntos in MAPA:
        rect = normalizar_rectangulo(puntos[0], puntos[1])
        if punto_en_rectangulo(x, y, rect):
            resultado_var.set(f"¡Impacto en {nombre}!")
            refrescar_canvas()
            return
    #si nunca encontró que atinó, setea agua
    resultado_var.set("Agua.")
    refrescar_canvas() #limpia y dibuja el canvas


# =========================
# UI: hace la ventana y los componentes gráficos
# =========================



def construir_ui():
    #recordar que hay variables globales para esto
    global root, entrada_x, entrada_y, resultado_var, canvas
    root = tk.Tk() #crea ventana
    root.title("Mapa cartesiano (cuadrícula 10x10)")
    #frame es un contenedor, como una subdivisión que se puede colocar en la pantalla
    contenedor = tk.Frame(root)
    contenedor.pack(fill="both", expand=True, padx=10, pady=10)
    #Se hacen dos paneles
    #izquierdo para inputs y botones. Paneles son un contenedor, se le colocan componentes
    panel_izq = tk.Frame(contenedor)
    panel_izq.pack(side="left", fill="y", padx=(0, 10))
    #Label fija
    tk.Label(panel_izq, text="Coordenadas del disparo", font=("Arial", 12, "bold")).pack(anchor="w", pady=(0, 8))
    fila_x = tk.Frame(panel_izq); fila_x.pack(anchor="w", pady=4)
    # label fija X
    tk.Label(fila_x, text="X: ").pack(side="left")
    entrada_x = tk.Entry(fila_x, width=8); entrada_x.pack(side="left"); entrada_x.insert(0, "0")
    # label fija Y
    fila_y = tk.Frame(panel_izq); fila_y.pack(anchor="w", pady=4)
    tk.Label(fila_y, text="Y: ").pack(side="left")
    entrada_y = tk.Entry(fila_y, width=8); entrada_y.pack(side="left"); entrada_y.insert(0, "0")

    #Botón de disparar, tiene el command de la función disparar
    tk.Button(panel_izq, text="Disparar", command=disparar).pack(anchor="w", pady=10)
    resultado_var = tk.StringVar(value="Listo para disparar en (0,0).")
    tk.Label(panel_izq, textvariable=resultado_var, fg="blue").pack(anchor="w", pady=(4, 0))

    #se crea el otro panel, que va a la derecha y va el canvas
    panel_der = tk.Frame(contenedor)
    panel_der.pack(side="left", fill="both", expand=True)
    #se hace el canvas del tamaño de las constantes globales
    ancho_canvas = MARGEN * 2 + (ANCHO_MUNDO * 2) * ESCALA
    alto_canvas  = MARGEN * 2 + (ALTO_MUNDO  * 2) * ESCALA
    canvas_local = tk.Canvas(panel_der, width=ancho_canvas, height=alto_canvas, bg="white")
    canvas_local.pack(fill="both", expand=True)
    #al canvas global se le asigna el que acabamos de crear. Esto es tkinter
    globals()["canvas"] = canvas_local
    #se llama al metodo de limpiar y dibujar el canvas
    refrescar_canvas()
    root.mainloop()


if __name__ == "__main__":
    construir_ui()

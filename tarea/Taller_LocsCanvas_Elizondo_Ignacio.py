import tkinter as tk

# constantes
ANCHO = 600
ALTO = 400

# globales
zonas = {
   "Jaguar_Refugio": {"x1": 50, "y1": 60, "x2": 220, "y2": 150, "tipo": "hábitat", "color": "#2E86DE"},
   "Rio_Boscoso": {"x1": 300, "y1": 40, "x2": 500, "y2": 120, "tipo": "río", "color": "#1ABC9C"},
   "Zona_Protegida": {"x1": 120, "y1": 180, "x2": 480, "y2": 320, "tipo": "protección", "color": "#F1C40F"},
   "Mirador": {"x1": 400, "y1": 260, "x2": 350, "y2": 200, "tipo": "mirador", "color": "#E74C3C"},
   "Taller_Educativo": {"x1": 10, "y1": 330, "x2": 140, "y2": 390, "tipo": "servicio", "color": "#9B59B6"},
   "Zona_Fuera": {"x1": 580, "y1": 50, "x2": 700, "y2": 140, "tipo": "fuera", "color": "#7F8C8D"}
}

# ================
# funciones
# ================

def normalizar_rectangulo(info):
    x1, y1, x2, y2 = info["x1"], info["y1"], info["x2"], info["y2"]
    x1n = min(x1, x2)
    y1n = min(y1, y2)
    x2n = max(x1, x2)
    y2n = max(y1, y2)
    return (x1n, y1n, x2n, y2n)


def esta_en_rango(x1, y1, x2, y2, ancho, alto):
    if x2 < 0 or y2 < 0 or x1 > ancho or y1 > alto:
        return False
    return True


def construir_rectangulos(zonas, ancho, alto):
    rects = []
    for nombre, datos in zonas.items():
        x1n, y1n, x2n, y2n = normalizar_rectangulo(datos)

        if not esta_en_rango(x1n, y1n, x2n, y2n, ancho, alto):
            continue  # filtra los que están fuera

        color = datos.get("color", "#3498DB")
        tipo = datos.get("tipo", None)
        rects.append((nombre, x1n, y1n, x2n, y2n, color, tipo))

    return rects


def dibujar_mapa(canvas, rects):
    ids = []
    for dato in rects:
        nombre, x1, y1, x2, y2, color, tipo = dato
        rid = canvas.create_rectangle(x1, y1, x2, y2, outline='black', fill=color)
        cx, cy = (x1 + x2) // 2, (y1 + y2) // 2
        canvas.create_text(cx, cy, text=nombre, anchor='center')
        ids.append(rid)
    return ids


def resumen_por_tipo(rects):
    resumen = {}
    for nombre, x1, y1, x2, y2, color, tipo in rects:
        if tipo is None:
            continue
        area = (x2 - x1) * (y2 - y1)
        if tipo in resumen:
            resumen[tipo] += area
        else:
            resumen[tipo] = area
    return resumen


# ================
# canvas
# ================

if __name__ == "__main__":
    root = tk.Tk()
    root.title("Operación Jaguar - Mapa")

    canvas = tk.Canvas(root, width=ANCHO, height=ALTO, bg='white')
    canvas.pack()

    rects = construir_rectangulos(zonas, ANCHO, ALTO)
    ids = dibujar_mapa(canvas, rects)
    print("Resumen por tipo:", resumen_por_tipo(rects))

root.mainloop()

import threading, random, time
import tkinter as tk

class Vehiculo (threading.Thread): # herencia
    def __init__(self, canvas, color, y, nombre, meta, resultado, x, rect):
        self.canvas = canvas
        self.color = color
        self.y = y
        self.nombre = nombre
        self.meta = meta
        self.resultado = resultado
        self.x = x
        self.rect = self.canvas.create_rectangle(self.x, self.y, self.x+40, self.y+20, fill=self.color)

    def run(self):
        while self.x < self.meta:
            paso = random.ranint(5,15)
            time.sleep(random.uniform(0.05, 0.2))

            self.canvas.move(self.rect, paso, 0)
            self.x += paso

        self.serultado.append(self.nombre)

class CarreraApp:
    def __ini__ (self, root):
        self.root = root
        self.root.title("Carrera")
        self.canvas = tk.Canvas(self.root, width = 600, height = 200, bg="white")
        self.canvas.pack()
        self.btn_iniciar = tk.Button(root, text="Iniciar", command = self.iniciar_carrera)
        self.btn_iniciar.pack(pady=10)
        self.label_resultado = tk.Label(root, text='')
        self.label_resultado.pack()
        self.meta = 500
        self.resultado = []

        self.vehiculos = [
            Vehiculo(self.canvas, "red", 30, "Rojo", self.meta, self.resultado),
            Vehiculo(self.canvas, "blue", 30, "Azul", self.meta, self.resultado),
            Vehiculo(self.canvas, "yellow", 30, "Amarillo", self.meta, self.resultado),
            Vehiculo(self.canvas, "green", 30, "Verde", self.meta, self.resultado),
            Vehiculo(self.canvas, "pink", 30, "Rosado", self.meta, self.resultado),
            Vehiculo(self.canvas, "gray", 30, "Gris", self.meta, self.resultado),
        ]        

    
    def iniciar_carrera(self):
        self.resultado.clear()
        for v in self.vehiculos:
            thread = threading.Thread(target = self.corre_vehiculo, args=(v,))
            thread.start()
        self.root.after(100, self.verificar_resultado)

    def corre_vehiculo(self,vehiculo):
        vehiculo.run()

    def verificar_resultado(self):
        if len(self.resultado) == 3:
            texto = 'Podio:\n'
            for i, nombre in enumerate(self.resultado):
                texto += f"{i+1}.\t{nombre}\n"
            self.label_resultado.config(text=texto)


if __name__ == "__main__":
    root = tk.Tk()
    app = CarreraApp()
    root.mainloop()
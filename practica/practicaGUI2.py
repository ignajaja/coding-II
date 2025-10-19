import tkinter as tk

root = tk.Tk()

#canvas
canvas = tk.Canvas(
    root, 
    name="canvas", 
    bg = "white", 
    width=400, 
    height=350)
canvas.pack()

rectangle1 = canvas.create_rectangle(
    50, 50,
    150, 100,
    fill='blue',
    outline="red"
)
oval1 = canvas.create_oval(
    250, 50,
    350, 100,
    fill='red',

)
line1 = canvas.create_line(
    0,0,
    400,350,
    fill='green',
    width=3
)

canvas.create_text(
    200, 150,
    text="Hola mundo",
    fill="purple",
    font=("Arial", 24)
)

root.mainloop()
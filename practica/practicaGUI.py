from tkinter import *

# window root
root = Tk()
root.title("McTec")
root.geometry("600x500")


# functions
def calcular_precio():
    combo = 3000
    if agrandar_var.get():
        combo += 1000
    if papitas_var.get():
        combo += 700
    if postre_var.get():
        combo += 500
    precio_var.set(str(combo))
    return


# variables
combo_var = StringVar(value="")

agrandar_var = BooleanVar()
papitas_var = BooleanVar()
postre_var = BooleanVar()
precio_var = IntVar()

# label
label_combo = Label(root, text="Elige tu combo:", font=("Arial", 12, "bold"))
label_combo.place(x=100, y=40)


# radiobuttons
radio_hamburguesa = Radiobutton(
    root,
    text="Big mac",
    value="Hamburguesa",
    variable=combo_var,
    command=calcular_precio,
)
radio_sandwich = Radiobutton(
    root,
    text="Subway",
    value="Sandwich",
    variable=combo_var,
    command=calcular_precio,
)
radio_pizza = Radiobutton(
    root,
    text="Pizza hut",
    value="Pizza",
    variable=combo_var,
    command=calcular_precio,
)

radio_hamburguesa.place(x=100, y=80)
radio_sandwich.place(x=220, y=80)
radio_pizza.place(x=340, y=80)


# checkboxes
check_agrandar = Checkbutton(
    root, text="Agrandar combo", variable=agrandar_var, command=calcular_precio
)
check_papitas = Checkbutton(
    root, text="Papitas extra", variable=papitas_var, command=calcular_precio
)
check_postre = Checkbutton(
    root, text="Postre", variable=postre_var, command=calcular_precio
)

check_agrandar.place(x=100, y=120)
check_papitas.place(x=100, y=160)
check_postre.place(x=100, y=200)

root.mainloop()

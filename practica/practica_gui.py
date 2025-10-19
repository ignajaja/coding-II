from tkinter import *


# funciones comunes
def largo(n):
    res = 0
    n = abs(n)
    while n > 9:
        res += 1
        n //= 10
    return res + 1


# funciones
def comando_largo():
    valor = var_numero.get()
    if valor.isnumeric():
        numero = int(valor)
        respuesta = str(largo(numero))
        var_success.set("El número " + valor + " tiene " + respuesta + " digitos.")
        var_error.set("")
        var_numero.set("")
    else:
        var_success.set("")
        var_error.set("Error, debe ingresar un número")
    return


# ventana principal
root = Tk()
root.title("Mi ventana")
root.geometry("700x500")

# variables
var_numero = StringVar()
var_success = StringVar()
var_error = StringVar()

# componentes de la ventana
label_numero = Label(root, text="Ingrese un número", font=("Arial", 20, "bold"))
label_numero.place(x=20, y=20)

entry_numero = Entry(root, font=("Arial", 20, "bold"), textvariable=var_numero)
entry_numero.place(x=280, y=20)

button_largo = Button(root, text="Digits", command=comando_largo)
button_largo.place(x=260, y=80)

label_exito = Label(
    root,
    text="todo bien pa",
    fg="green",
    font=("Arial", 16, "bold"),
    textvariable=var_success,
)
label_exito.place(x=20, y=140)

label_error = Label(
    root,
    text="Error, debe ser un entero",
    fg="red",
    font=("Arial", 16, "bold"),
    textvariable=var_error,
)
label_error.place(x=20, y=140)


root.mainloop()

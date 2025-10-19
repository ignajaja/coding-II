from tkinter import *

#globales
flag_x = True

fila_x_0 = 0
fila_x_1 = 0
fila_x_2 = 0
columna_x_0 = 0
columna_x_1 = 0
columna_x_2 = 0

fila_o_0 = 0
fila_o_1 = 0
fila_o_2 = 0
columna_o_0 = 0
columna_o_1 = 0
columna_o_2 = 0

diagonal_x_1 = 0
diagonal_x_2 = 0
diagonal_o_1 = 0
diagonal_o_2 = 0

#funciones comunes
def set_char():
    global flag_x
    if flag_x:
        return "X"
    else:
        return "O"
    

#funciones
def try_winner(fila, columna, diagonal, flag_x):
    if flag_x == True:
        ganador = "X"
        perdedor = "O"
        global diagonal_x_1
        global diagonal_x_2
        diagonal1 = diagonal_x_1
        diagonal2 = diagonal_x_2
    else:
        ganador = "O"
        perdedor = "X"
        global diagonal_o_1
        global diagonal_o_2
        diagonal1 = diagonal_o_1
        diagonal2 = diagonal_o_2

    if fila == 3 or columna == 3 or diagonal == 3:
        var_won.set("El ganador es: " + ganador)
        var_lost.set("El perdedor es: " + perdedor)
    if diagonal == 4:
        if diagonal1 == 3 or diagonal2 == 3:
            var_won.set("El ganador es: " + ganador)
            var_lost.set("El perdedor es: " + perdedor)
    
def count_cells(fila, columna, diagonal, flag_x):
    global fila_x_0
    global fila_x_1
    global fila_x_2
    global columna_x_0
    global columna_x_1
    global columna_x_2
    global fila_o_0
    global fila_o_1
    global fila_o_2
    global columna_o_0
    global columna_o_1
    global columna_o_2
    global diagonal_x_1
    global diagonal_o_1
    global diagonal_x_2
    global diagonal_o_2


    if fila == "0" and flag_x == True:
        fila_x_0 += 1
    if fila == "1" and flag_x == True:
        fila_x_1 += 1
    if fila == "2" and flag_x == True: 
        fila_x_2 += 1   
    if fila == "0" and flag_x == False:
        fila_o_0 += 1
    if fila == "1" and flag_x == False:
        fila_o_1 += 1
    if fila == "2" and flag_x == False:
        fila_o_2 += 1

    if columna == "0" and flag_x == True:
        columna_x_0 += 1
    if columna == "1" and flag_x == True:
        columna_x_1 += 1
    if columna == "2" and flag_x == True: 
        columna_x_2 += 1   
    if columna == "0" and flag_x == False:
        columna_o_0 += 1
    if columna == "1" and flag_x == False:
        columna_o_1 += 1
    if columna == "2" and flag_x == False:
        columna_o_2 += 1

    if diagonal == "1" and flag_x == True:
        diagonal_x_1 += 1
    if diagonal == "1" and flag_x == False:
        diagonal_o_1 += 1
    if diagonal == "2" and flag_x == True:
        diagonal_o_1 += 1
    if diagonal == "2" and flag_x == False:
        diagonal_o_2 += 1
    if diagonal == "3" and flag_x == True:
        diagonal_x_1 += 1
        diagonal_x_2 += 1
    if diagonal == "3" and flag_x == False:
        diagonal_o_1 += 1
        diagonal_o_2 += 1




def activar_boton_00():
    global flag_x
    var_pos_00.set(set_char())
    count_cells("0", "0", "1", flag_x)
    if flag_x == True:
        try_winner(fila_x_0, columna_x_0, diagonal_x_1, flag_x)
    else:
        try_winner(fila_o_0, columna_o_0, diagonal_o_1, flag_x)
    flag_x = not flag_x


def activar_boton_01():
    global flag_x
    var_pos_01.set(set_char())
    count_cells("0", "1", "0", flag_x)
    if flag_x == True:
        try_winner(fila_x_0, columna_x_1, 0, flag_x)
    else:
        try_winner(fila_o_0, columna_o_1, 0, flag_x)
    flag_x = not flag_x


def activar_boton_02():
    global flag_x
    var_pos_02.set(set_char())
    count_cells("0", "2", " 2", flag_x)
    if flag_x == True:
        try_winner(fila_x_0, columna_x_2, diagonal_x_2, flag_x)
    else:
        try_winner(fila_o_0, columna_o_2,diagonal_o_2, flag_x)
    flag_x = not flag_x


def activar_boton_10():
    global flag_x
    var_pos_10.set(set_char())
    count_cells("1", "0", " 0", flag_x)
    if flag_x == True:
        try_winner(fila_x_1, columna_x_0, 0, flag_x)
    else:
        try_winner(fila_o_1, columna_o_0, 0, flag_x)
    flag_x = not flag_x


def activar_boton_11():
    global flag_x
    var_pos_11.set(set_char())
    count_cells("1", "1", "3", flag_x)
    if flag_x == True:
        try_winner(fila_x_1, columna_x_1, 4, flag_x)
    else:
        try_winner(fila_o_1, columna_o_1, 4, flag_x)
    flag_x = not flag_x


def activar_boton_12():
    global flag_x
    var_pos_12.set(set_char())
    count_cells("1", "2", "0", flag_x)
    if flag_x == True:
        try_winner(fila_x_1, columna_x_2, 0, flag_x)
    else:
        try_winner(fila_o_1, columna_o_2, 0, flag_x)
    flag_x = not flag_x


def activar_boton_20():
    global flag_x
    var_pos_20.set(set_char())
    count_cells("2", "0", "2", flag_x)
    if flag_x == True:
        try_winner(fila_x_2, columna_x_0, diagonal_x_2, flag_x)
    else:
        try_winner(fila_o_2, columna_o_0, diagonal_o_2, flag_x)
    flag_x = not flag_x

def activar_boton_21():
    global flag_x
    var_pos_21.set(set_char())
    count_cells("2", "1", "0", flag_x)
    if flag_x == True:
        try_winner(fila_x_2, columna_x_1, 0, flag_x)
    else:
        try_winner(fila_o_2, columna_o_1, 0, flag_x)
    flag_x = not flag_x


def activar_boton_22():
    global flag_x
    var_pos_22.set(set_char())
    count_cells("2", "2", "1", flag_x)
    if flag_x == True:
        try_winner(fila_x_2, columna_x_2, diagonal_x_1, flag_x)
    else:
        try_winner(fila_o_2, columna_o_2, diagonal_x_1, flag_x)
    flag_x = not flag_x



#ventana
root = Tk()
root.title("Juego gato")
root.geometry("800x900")

#variables
var_won = StringVar()
var_lost = StringVar()


var_pos_00 = StringVar()
var_pos_01 = StringVar()
var_pos_02 = StringVar()
var_pos_10 = StringVar()
var_pos_11 = StringVar()
var_pos_12 = StringVar()
var_pos_20 = StringVar()
var_pos_21 = StringVar()
var_pos_22 = StringVar()


#componentes 
label_titulo = Label(root, text="Juego de gato, presione un botón.", font=("Arial", 20, "bold"))
label_titulo.place(x=20, y=20)

label_numero1 = Label(root, text="", font=("Arial", 20, "bold"), textvariable=var_pos_00)
label_numero1.place(x=220, y=60)
label_numero2 = Label(root, text="", font=("Arial", 20, "bold"), textvariable=var_pos_01)
label_numero2.place(x=220, y=100)
label_numero3 = Label(root, text="", font=("Arial", 20, "bold"), textvariable=var_pos_02)
label_numero3.place(x=220 , y=140)
label_numero4 = Label(root, text="", font=("Arial", 20, "bold"), textvariable=var_pos_10)
label_numero4.place(x=260 , y=60)
label_numero5 = Label(root, text="", font=("Arial", 20, "bold"), textvariable=var_pos_11)
label_numero5.place(x=260 , y=100)
label_numero6 = Label(root, text="", font=("Arial", 20, "bold"), textvariable=var_pos_12)
label_numero6.place(x=260 , y=140)
label_numero7 = Label(root, text="", font=("Arial", 20, "bold"), textvariable=var_pos_20)
label_numero7.place(x=300 , y=60)
label_numero8 = Label(root, text="", font=("Arial", 20, "bold"), textvariable=var_pos_21)
label_numero8.place(x=300 , y=100)
label_numero9 = Label(root, text="", font=("Arial", 20, "bold"), textvariable=var_pos_22)
label_numero9.place(x=300 , y=140)

button_numero1 = Button(root, text="0,0", command=activar_boton_00)
button_numero1.place(x=20, y=60)
button_numero2 = Button(root, text="0,1", command=activar_boton_01)
button_numero2.place(x=20, y=100)
button_numero3 = Button(root, text="0,2", command=activar_boton_02)
button_numero3.place(x=20, y=140)
button_numero4 = Button(root, text="1,0", command=activar_boton_10)
button_numero4.place(x=80, y=60)
button_numero5 = Button(root, text="1,1", command=activar_boton_11)
button_numero5.place(x=80, y=100)
button_numero6 = Button(root, text="1,2", command=activar_boton_12)
button_numero6.place(x=80, y=140)
button_numero7 = Button(root, text="2,0", command=activar_boton_20)
button_numero7.place(x=140, y=60)
button_numero8 = Button(root, text="2,1", command=activar_boton_21)
button_numero8.place(x=140, y=100)
button_numero9 = Button(root, text="2,2", command=activar_boton_22)
button_numero9.place(x=140, y=140)

label_ganador = Label(root, text="Ganó", textvariable=var_won)
label_ganador.place(x=20, y=220)
label_perdedor = Label(root, text="Perdió", textvariable=var_lost)
label_perdedor.place(x=20, y=260)


root.mainloop()
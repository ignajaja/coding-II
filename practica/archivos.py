lista = ['linea 1\n', 'linea 2\n', 'linea 3\n']
file = open('holamundo.txt', 'a')
file.writelines(lista)
file.close()

with open('holamundo.txt', 'r') as archivo:

    texto = '.'
    while texto != '':
        texto = input("Escriba lo que quiere agregar: ")
        archivo.write(texto)

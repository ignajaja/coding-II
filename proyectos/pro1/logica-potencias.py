potencias = []

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
                ["Sídney", [[[135, 0, 0],[-20, 0, 0]], [[180, 0, 0],[-90, 0, 0]]]],
        ]
        ]
    ]
]

def normalizar_rectangulo(p1, p2): # hace que todos los rectángulos se puedan acomodar de manera ordenada
    x1 = p1[0] 
    y1 = p1[1]
    x2 = p2[0] 
    y2 = p2[1]
        
    xmin = x1 if x1[0] < x2[0] else x2
    xmax = x1 if x1[0] > x2[0] else x2
    ymin = y1 if y1[0] < y2[0] else y2
    ymax = y1 if y1[0] > y2[0] else y2
        
    return xmin,xmax,ymin,ymax

#-------------------
def reclamar_territorio(nombre, territorio):
    global potencias
    
    for pais in MAPA:
        for region in pais[3:]:
            for ciudad in region[1]:
                if ciudad[0] == territorio:
                    territorio = ciudad

    
    for pots in potencias:
        if pots[0][0] == nombre:
            pots.append(territorio)

#--------------------
def anadir_potencias(nombre):
    global potencias
    
    for pot in potencias:
        if nombre == pot[0][0]:
            # aqui salta error cuando existe otra potencia con el mismo nombre
            return
    
    estado_pot = True # está activo o inactivo
    indicador_pot = True # está vivo o no
    por_vida_pot = 100 # vida restante
    can_misiles_pot = 1000
    can_disparos_pot = 0 # cantidad de ataques enviados
    can_recibidos_pot = 0 # cantidad de ataques recibidos

    potencias.append([[nombre, estado_pot, indicador_pot, por_vida_pot, can_misiles_pot, can_disparos_pot, can_recibidos_pot]])
        
#-----------------
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
    
    
#============================

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
                # aqui salta error si no tiene territorios
                True
            print(f"Nombre: {pots[0][0]}, Estado: {"Activo" if pots[0][1] == True else "Inactivo"}, Indicador: {"Vivo" if pots[0][2] == True else "Derrotada"}, Vida: {pots[0][3]}, Misiles: {pots[0][4]}, Disparos tirados: {pots[0][5]}, Disparos recibidos: {pots[0][6]}, Extensión en km^2: {extension_territorios}")

    return

anadir_potencias("salma")
anadir_potencias("aaron")
anadir_potencias("nacho")
anadir_potencias("joseth")

reclamar_territorio("salma", "El Guarco")
reclamar_territorio("aaron", "Medellin")
reclamar_territorio("nacho", "Roma")
reclamar_territorio("joseth", "Sídney")

# print(potencias)

print(generar_status_potencia("nacho"))
print(contar_extension("Roma"))

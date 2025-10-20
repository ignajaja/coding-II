# def coordenadas_a_xy(x1, x2, x3, y1, y2, y3):
#     if x1 < 0:
#         c_x = (x1) - (x2*10)/600 - (x3*60)/36000
#     else:
#         c_x = (x1) + (x2*10)/600 + (x3*60)/36000
#     if y1 < 0:
#         c_x = (y1) - (y2*10)/600 - (y3*60)/36000
#     else:
#         c_y = (y1) + (y2*10)/600 + (y3*60)/36000
    
#     return c_x, c_y

# print(coordenadas_a_xy(60,30,30,90,30,30))
# print(coordenadas_a_xy(-60,30,30,90,30,30))

MAPA = [
    [
        "Costa Rica", 100, 98000,
        [
            "Alajuela", [
                ["San Ramon", [[[-10, 0, 3],[12,3,0]], [[8, 0, 0], [20, 59, 59]]]],
                ["SanMateo", [[[10, 50, 3],[-12,30,0]], [ [15, 30, 0], [11, 59,59]]]]
            ]
        ],
        [
            "Cartago", [
                ["Alvarado", [[[-1, 50, 3],[0, 30, 0]], [[5, 30, 0], [20, 59, 59]]]],
                ["El Guarco", [[[-3, 50, 3],[1, 30, 0]], [[35, 30, 0], [30, 59, 59]]]],
                ["Cental", [[[ 19, 5, 43],[-41,30,0]], [[-45, 30, 0], [-40, 9, 5]]]]
            ]
        ],
        [
            "San Jose", [
                ["Perez Zeledón", [[[-10, 50, 3],[12,30,0]], [[95, 30, 0], [20, 5, 59]]]],
                ["Escazu", [[[-13, 50, 3],[12,30,0]], [[35, 30, 0], [3, 59, 59]]]]
            ]
        ]
    ],
    [
        "Colombia", 100, 100000,
        [
            "Antioquia", [
                ["Medellin", [[[-10, 0, 3],[12,30,0]], [[8, 0, 0], [20, 59, 59]]]],
                ["Bello", [[[10, 50, 3],[-12,30,0]], [ [15, 30, 0], [11, 59,59]]]]
            ]
        ],
        [
            "Cundinamarca", [
                ["Bogota", [[[-1, 50, 3],[0, 30, 0]], [[5, 30, 0], [20, 59, 59]]]],
                ["Soacha", [[[-3, 50, 3],[1, 30, 0]], [[35, 30, 0], [30, 59, 59]]]],
                ["Chia", [[[ 19, 5, 43],[-41,30,0]], [[-45, 30, 0], [-40, 9, 5]]]]
            ]
            
        ],
        [
            "Valle del Cauca", [
                ["Cali", [[[-10, 50, 3],[12,30,0]], [[95, 30, 0], [20, 5, 59]]]],
                ["Palmira", [[[-13, 50, 3],[12,30,0]], [[35, 30, 0], [3, 59, 59]]]]
            ]
        
        ]
    ],
    [
        "Italia", 120, 110000,
        [
            "Lazio", [
                ["Roma", [[[-10, 0, 3],[12,30,0]], [[8, 0, 0], [20, 59, 59]]]],
                ["Frosinone", [[[10, 50, 3],[-12,30,0]], [ [15, 30, 0], [11, 59,59]]]]
            ]
        ],
        [
            "Toscana", [
                ["Florencia", [[[-1, 50, 3],[0, 30, 0]], [[5, 30, 0], [20, 59, 59]]]],
                ["Pisa", [[[-3, 50, 3],[1, 30, 0]], [[35, 30, 0], [30, 59, 59]]]],
                ["Siena", [[[ 19, 5, 43],[-41,30,0]], [[-45, 30, 0], [-40, 9, 5]]]]
            ]
        ],
        [
            "Lombardia", [  
                ["Milán", [[[-10, 50, 3],[12,30,0]], [[95, 30, 0], [20, 5, 59]]]],
                ["Bérgamo", [[[-13, 50, 3],[12,30,0]], [[35, 30, 0], [3, 59, 59]]]]
            ]
        ]
    ],
    [
        "Alemania", 130, 120000,
        [
            "Baviera", [
                ["Múnich", [[[-10, 0, 3],[12,30,0]], [[8, 0, 0], [20, 59, 59]]]],
                ["Núremberg", [[[10, 50, 3],[-12,30,0]], [ [15, 30, 0], [11, 59,59]]]]
            ]
        ],
        [
            "Renania", [
                ["Colonia", [[[-1, 50, 3],[0, 30, 0]], [[5, 30, 0], [20, 59, 59]]]],
                ["Düsseldorf", [[[-3, 50, 3],[1, 30, 0]], [[35, 30, 0], [30, 59, 59]]]],
                ["Bonn", [[[ 19, 5, 43],[-41,30,0]], [[-45, 30, 0], [-40, 9, 5]]]]
            ]
        ],
        [
            "Sajonia", [  
                ["Dresde", [[[-10, 50, 3],[12,30,0]], [[95, 30, 0], [20, 5, 59]]]],
                ["Leipzig", [[[-13, 50, 3],[12,30,0]], [[35, 30, 0], [3, 59, 59]]]]
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



def convertir_a_xy_mapa(coord_x, coord_y):
    x1 = coord_x[0]; x2 = coord_x[1]; x3 = coord_x[2]
    y1 = coord_y[0]; y2 = coord_y[1]; y3 = coord_y[2]
    
    sign_x = -1 if x1 < 0 else 1
    sign_y = -1 if y1 < 0 else 1
    
    cx = sign_x * (abs(x1) + x2 / 6 + x3 / 360)
    cy = sign_y * (abs(y1) + y2 / 6 + y3 / 360)
    
    return cx, cy

# dibujar territorios
def dibujar_territorios():
    for pais in MAPA:
        for prov in pais[3:]:
            for ciud in prov[1]:
                # print(f"x1: {ciud[1][0][0]}, y1: {ciud[1][0][1]}, x2: {ciud[1][1][0]}, y2: {ciud[1][1][1]}")
                rect = normalizar_rectangulo(ciud[1][0], ciud[1][1])
                xmin, xmax, ymin, ymax = rect
                # print(xmin, xmax, ymin, ymax)
                xmin, xmax = convertir_a_xy_mapa(xmin, xmax)
                ymin, ymax = convertir_a_xy_mapa(ymin, ymax)
                print(f"Ciudad: {ciud[0]}, Rectángulo normalizado y convertido a XY: ({xmin}, {ymin}), ({xmax}, {ymax})")
                 
                
dibujar_territorios()

# print(normalizar_rectangulo([[-13, 50, 3],[12,30,0]], [[35, 30, 0], [3, 59, 59]]))
# print(normalizar_rectangulo([[-13, 50, 3],[12,30,0]], [[35, 30, 0], [3, 59, 59]]))
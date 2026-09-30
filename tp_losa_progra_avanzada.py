import random
import string


def crear_matriz_teselacion(tam_matriz, pos_x_losa, pos_y_losa):
    matriz = []
    for i in range(tam_matriz):
        matriz.append([])
        for j in range(tam_matriz):
            matriz[i].append(0)
    matriz[pos_y_losa][pos_x_losa] = 'x'

    return matriz


def generar_pool_caracteres(cantidad_necesaria):
    letras_simples = [c for c in string.ascii_lowercase + string.ascii_uppercase
                       if c != 'x']

    if cantidad_necesaria <= len(letras_simples):
        pool = letras_simples
    else:
        pool = [a + b for a in letras_simples for b in letras_simples if a + b != 'x']

    random.shuffle(pool)
    return pool


pool_caracteres = []
indice_pool = [0]


def siguiente_caracter():
    c = pool_caracteres[indice_pool[0]]
    indice_pool[0] += 1
    return c


def crear_teselacion(matriz, pos_x_losa, pos_y_losa,
                      inicio_x=None, fin_x=None, inicio_y=None, fin_y=None):

    if inicio_x is None:
        inicio_x = 0
    if fin_x is None:
        fin_x = len(matriz[0])
    if inicio_y is None:
        inicio_y = 0
    if fin_y is None:
        fin_y = len(matriz)

    if not pool_caracteres:
        n = len(matriz)
        cantidad_trominos = (n * n - 1) // 3
        pool_caracteres.extend(generar_pool_caracteres(max(1, cantidad_trominos)))

    tam_matriz_x = fin_x - inicio_x
    tam_matriz_y = fin_y - inicio_y

    #==================================CODIGO DEL CASO BASE===============================================
    if tam_matriz_x == 1 and tam_matriz_y == 1: 
        return

    #==================================FIN CODIGO DEL CASO BASE===============================================

    #==================================CODIGO NECESARIO PARA LA DIVISION===============================================
    
    mid_x = inicio_x + tam_matriz_x // 2
    mid_y = inicio_y + tam_matriz_y // 2

    cuadrantes = {
        "NO": (inicio_x, mid_x, inicio_y, mid_y),
        "NE": (mid_x, fin_x, inicio_y, mid_y),
        "SO": (inicio_x, mid_x, mid_y, fin_y),
        "SE": (mid_x, fin_x, mid_y, fin_y),
    }

    centros = {
        "NO": (mid_x - 1, mid_y - 1),
        "NE": (mid_x,     mid_y - 1),
        "SO": (mid_x - 1, mid_y),
        "SE": (mid_x,     mid_y),
    }

    def cuadrante_de(x, y):
        if x < mid_x and y < mid_y:
            return "NO"
        elif x >= mid_x and y < mid_y:
            return "NE"
        elif x < mid_x and y >= mid_y:
            return "SO"
        else:
            return "SE"

    q = cuadrante_de(pos_x_losa, pos_y_losa)

    #==================================FIN CODIGO NECESARIO PARA LA DIVISION===============================================

    #====================================  CODIGO NECESARIO PARA LA "COMBINACION"=============================
    caracter_pieza = siguiente_caracter()
    for nombre, (cx, cy) in centros.items():
        if nombre != q:
            matriz[cy][cx] = caracter_pieza  
    #====================================FIN  CODIGO NECESARIO PARA LA "COMBINACION"=============================
    
    #===============================CODIGO NECESARIO PARA LA "CONQUISTA" DEL PROBLEMA======================================
    for nombre, (ix, fx, iy, fy) in cuadrantes.items():
        if nombre == q:
            sub_x, sub_y = pos_x_losa, pos_y_losa
        else:
            sub_x, sub_y = centros[nombre] # ACA SE DETERMINA ESAS "losas prohibidas inventadas" para esas otras porciones del tablero
    
    
        crear_teselacion(matriz, sub_x, sub_y, ix, fx, iy, fy) 
    #============================FIN CODIGO NECESARIO PARA LA "CONQUISTA" DEL PROBLEMA======================================
    
    return


matriz = crear_matriz_teselacion(16, 3, 3)

for i in matriz:
    print(i)


crear_teselacion(matriz, 3, 3)

print("===========================================")
for i in matriz:
    print(i)
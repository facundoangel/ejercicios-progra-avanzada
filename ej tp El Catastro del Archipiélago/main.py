M1 = [
	["1","1","1","1","0"],
	["1","1","0","1","0"],
	["1","1","0","0","0"],
	["0","0","0","0","0"]
]





def procesarMatriz(m):
    conjuntosVisitados = set([])
    arrayIslas = []

    for i,_ in enumerate(m):
        for j,_ in enumerate(m[i]):
            if(m[i][j] == "1" and not (j,i) in conjuntosVisitados):
                arrayIslas.append(contabilizarAdyacencias(j,i,conjuntosVisitados,m))


    return arrayIslas



def contabilizarAdyacencias(x,y,conjuntosVisitados,m):
    pilaProxElem = []
    pilaProxElem.append((x,y))
    contAdyacencias = 0

    while (len(pilaProxElem) > 0):
        actualElem = pilaProxElem.pop()
        conjuntosVisitados.add(actualElem)
        cordX = actualElem[0]
        cordY = actualElem[1]

        if(not coordenadaSaleDeMatriz(cordX,cordY-1,m) and m[cordY-1][cordX] == "1" and not (cordY,cordX) in conjuntosVisitados):
            pilaProxElem.append((cordX,cordY-1))
            conjuntosVisitados.add((cordX,cordY-1))
            contAdyacencias+=1

        if(not coordenadaSaleDeMatriz(cordX-1,cordY,m) and m[cordY][cordX-1] == "1" and not (cordY,cordX-1) in conjuntosVisitados):
            pilaProxElem.append((cordX-1,cordY))
            conjuntosVisitados.add((cordX-1,cordY))
            contAdyacencias+=1

        if(not coordenadaSaleDeMatriz(cordX,cordY+1,m) and m[cordY+1][cordX] == "1" and not (cordY,cordX) in conjuntosVisitados):
            pilaProxElem.append((cordX,cordY+1))
            conjuntosVisitados.add((cordX,cordY+1))
            contAdyacencias+=1

        if(not coordenadaSaleDeMatriz(cordX+1,cordY,m) and m[cordY][cordX+1] == "1" and not (cordY,cordX+1) in conjuntosVisitados):
            pilaProxElem.append((cordX+1,cordY))
            conjuntosVisitados.add((cordX+1,cordY))
            contAdyacencias+=1


        return contAdyacencias

def extraerAdyacencias (x,y,m):
    

'''
def coordenadaSaleDeMatriz(nuevoX, nuevoY, matriz):
    largoMatriz = len(matriz)

    if(largoMatriz==0):
        return True

    anchoMatriz = len(matriz[0])


    if(nuevoX < 0 or nuevoX > anchoMatriz):
        return True

    if(nuevoY < 0 or nuevoY > largoMatriz):
            return True

    return False
'''
def coordenadaSaleDeMatriz(x, y, m):
    if len(m) == 0:
        return True
    return x < 0 or x >= len(m[0]) or y < 0 or y >= len(m)

print(procesarMatriz(M1))
M1 = [
	["1","1","1","1","0"],
	["1","1","0","1","0"],
	["1","1","0","0","0"],
	["0","0","0","0","0"]
]


M2 = [
	["1","1","0","0","0"],
	["1","1","0","0","0"],
	["0","0","1","0","0"],
	["0","0","0","1","1"]
]




def procesarMatriz(m):
    conjuntosVisitados = set([])
    arrayIslas = []

    for i,_ in enumerate(m):
        for j,_ in enumerate(m[i]):
            if(m[i][j] == "1" and not (j,i) in conjuntosVisitados):
                arrayIslas.append(contabilizarAdyacencias(j,i,conjuntosVisitados,m))

    arrayIslas.sort(reverse=True)
    return arrayIslas


def contabilizarAdyacencias(x,y,conjuntosVisitados,m):
    pilaProxElem = []
    pilaProxElem.append((x,y))
    contAdyacencias = 0

    while (len(pilaProxElem) > 0):
        actualElem = pilaProxElem.pop()
        contAdyacencias+=1
        conjuntosVisitados.add(actualElem)
        cordX = actualElem[0]
        cordY = actualElem[1]

        if(not coordenadaSaleDeMatriz(cordX,cordY-1,m) and m[cordY-1][cordX] == "1" and not (cordX,cordY-1) in conjuntosVisitados and not (cordX,cordY-1) in pilaProxElem):
            pilaProxElem.append((cordX,cordY-1))
            

        if(not coordenadaSaleDeMatriz(cordX-1,cordY,m) and m[cordY][cordX-1] == "1" and not (cordX-1,cordY) in conjuntosVisitados and not (cordX-1,cordY) in pilaProxElem):
            pilaProxElem.append((cordX-1,cordY))
            

        if(not coordenadaSaleDeMatriz(cordX,cordY+1,m) and m[cordY+1][cordX] == "1" and not (cordX,cordY+1) in conjuntosVisitados and not (cordX,cordY+1) in pilaProxElem):
            pilaProxElem.append((cordX,cordY+1))
            

        if(not coordenadaSaleDeMatriz(cordX+1,cordY,m) and m[cordY][cordX+1] == "1" and not (cordX+1,cordY) in conjuntosVisitados and not (cordX+1,cordY) in pilaProxElem):
            pilaProxElem.append((cordX+1,cordY))
            


    return contAdyacencias

    


def coordenadaSaleDeMatriz(nuevoX, nuevoY, matriz):
    largoMatriz = len(matriz)

    if(largoMatriz==0):
        return True

    anchoMatriz = len(matriz[0])


    if(nuevoX < 0 or nuevoX >= anchoMatriz):
        return True

    if(nuevoY < 0 or nuevoY >= largoMatriz):
            return True

    return False


print(procesarMatriz(M1))
print(procesarMatriz(M2))
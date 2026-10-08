import heapq


senderos = [
    [1, 2, 3],
    [1, 3, 2],
    [2, 3, 4],
    [2, 6, 1],
    [3, 8, 1],
    [8, 6, 5],
    [4, 5, 2],
    [3, 4, 2],
    [3, 6, 2],
    [6, 9, 3]
]

pos_dragones = [8,5]

def resolverCaminoSeguro(c,cf,cm,dragones,senderos):
    #CONSTRUYO LISTA DE ADYACENCIA
    grafo = [None] * c
    for sendero in senderos:
        nodoActual, nodoVecino, peso = sendero

        if(grafo[nodoActual-1] == None):
            grafo[nodoActual-1]=[(peso,nodoVecino)]
        else:
             grafo[nodoActual-1].append((peso,nodoVecino))


        if(grafo[nodoVecino-1] == None):
            grafo[nodoVecino-1]=[(peso,nodoActual)]
        else:
                grafo[nodoVecino-1].append((peso,nodoActual))


    #calcular tiempos de llegada de los dragones
    dist_dragones = [float("inf")] * c
    cola_prox_nodo_dragon = []


    for pos in dragones:
        dist_dragones[pos-1] = 0
        heapq.heappush(cola_prox_nodo_dragon,(0,pos))

    while len(cola_prox_nodo_dragon) != 0:
        distancia, nodo = cola_prox_nodo_dragon.pop(0)



        for vecino in grafo[nodo-1]:
            distancia_vecino, nodoVecino = vecino
            if(distancia+distancia_vecino < dist_dragones[nodoVecino-1]):
                dist_dragones[nodoVecino-1] = distancia+distancia_vecino
                heapq.heappush(cola_prox_nodo_dragon,(distancia+distancia_vecino,nodoVecino))



    #calcular tiempos de llegada del principe al nodo de princesa
    dist_principe = [float("inf")] * c
    nodos_predecesor_cam_principe = [None] * c
    cola_prox_nodo_principe = []
    respuesta = "NO HAY CAMINO"


    if(not hayCaminoConexo(grafo,cm,cf)):
        return respuesta


    heapq.heappush(cola_prox_nodo_principe,(0,cm))
    dist_principe[cm-1]=0
    nodos_predecesor_cam_principe[cm-1]=cm

    while len(cola_prox_nodo_principe)!=0:
        distancia, nodo = cola_prox_nodo_principe.pop(0)

        for vecino in grafo[nodo-1]:
            distancia_vecino, nodoVecino = vecino
            nueva_distancia = distancia_vecino + distancia

            if(nueva_distancia < dist_principe[nodoVecino-1] and nueva_distancia < dist_dragones[nodoVecino-1]):
                dist_principe[nodoVecino-1] = nueva_distancia
                nodos_predecesor_cam_principe[nodoVecino-1] = nodo
                heapq.heappush(cola_prox_nodo_principe,(nueva_distancia,nodoVecino))


    if(dist_principe[cf-1] == float("inf")):
        respuesta = "INTERCEPTADO"
    elif(dist_principe[cf-1] != float("inf")):
        respuesta = []
        respuesta.insert(0,cf)
        nodoAnterior =  nodos_predecesor_cam_principe[cf-1]
        while(nodoAnterior!=cm):
            respuesta.insert(0,nodoAnterior)
            nodoAnterior = nodos_predecesor_cam_principe[nodoAnterior-1]
        respuesta.insert(0,cm)

    return respuesta

def hayCaminoConexo(grafo,cm,cf):

    proxNodo = []
    nodosVisitados = set([])
    proxNodo.append(cm)

    while(len(proxNodo)!=0):
        nodo = proxNodo.pop(0)
        nodosVisitados.add(nodo)

        for tuplaNodoVecino in grafo[nodo-1]:
            _, nodoVecino = tuplaNodoVecino

            if(nodoVecino not in nodosVisitados and nodoVecino not in proxNodo):
                if(nodoVecino == cf):
                    return True
                proxNodo.append(nodoVecino)
            



    
    
    return False

print(resolverCaminoSeguro(9,len(pos_dragones),9,1,pos_dragones,senderos))

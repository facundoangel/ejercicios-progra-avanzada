precios = [-2000,100,3,900,200,-1600,600,400,99]


def encontrar_mejor_combinacion (arr,izq,der):

    if (der-izq)==0:
        resultado={"menor":[],"mayor":[]}
        resultado["menor"]=[izq,arr[izq]]
        resultado["mayor"]=[izq,arr[izq]]
        return resultado

    if (der-izq)==1:

        resultado={"menor":[],"mayor":[]}

        if(arr[izq]<arr[izq+1]):
            resultado["menor"]=[izq,arr[izq]]
        else:
            resultado["menor"]=[izq+1,arr[izq+1]]

        if(resultado["menor"][0]==izq+1):
            resultado["mayor"]=[izq+1,arr[izq+1]]
        else:
            resultado["mayor"]= [izq,arr[izq]] if arr[izq] > arr[izq+1] else [izq+1,arr[izq+1]] 

        return resultado
    


    med = izq + (der - izq) // 2


    rama_izq = encontrar_mejor_combinacion(arr,izq,med)
    rama_der = encontrar_mejor_combinacion(arr,med+1,der)


    resultado={"menor":[],"mayor":[]}


    ganancia_1 = rama_izq["mayor"][1] - rama_izq["menor"][1]
    ganancia_2 = rama_der["mayor"][1] - rama_der["menor"][1]
    ganancia_3 = rama_der["mayor"][1] - rama_izq["menor"][1] 


    if(ganancia_1>ganancia_2):

        if(ganancia_1<ganancia_3):
            resultado["mayor"]=rama_der["mayor"]
            resultado["menor"]=rama_izq["menor"]
        else:
            resultado["mayor"]=rama_izq["mayor"]
            resultado["menor"]=rama_izq["menor"]
    else:
        if(ganancia_2<ganancia_3):
            resultado["mayor"]=rama_der["mayor"]
            resultado["menor"]=rama_izq["menor"]
        else:
            resultado["mayor"]=rama_der["mayor"]
            resultado["menor"]=rama_der["menor"]



    return resultado

def encontrar_maximo_subarray(arr, izq, der):

    if izq == der:
        return ([izq], arr[izq])

    med = izq + (der - izq) // 2

    rama_izq = encontrar_maximo_subarray(arr, izq, med)
    rama_der = encontrar_maximo_subarray(arr, med + 1, der)

    # --------------------------------
    # Mejor suma que cruza el medio
    # --------------------------------

    suma = 0
    mejor_izq = float("-inf")
    pos_izq = med

    for i in range(med, izq - 1, -1):
        suma += arr[i]

        if suma > mejor_izq:
            mejor_izq = suma
            pos_izq = i

    suma = 0
    mejor_der = float("-inf")
    pos_der = med + 1

    for i in range(med + 1, der + 1):
        suma += arr[i]

        if suma > mejor_der:
            mejor_der = suma
            pos_der = i

    suma_cruzada = mejor_izq + mejor_der

    # --------------------------------
    # Comparar las 3 posibilidades
    # --------------------------------

    if rama_izq[1] >= rama_der[1] and rama_izq[1] >= suma_cruzada:
        return rama_izq

    elif rama_der[1] >= rama_izq[1] and rama_der[1] >= suma_cruzada:
        return rama_der

    else:
        posiciones = list(range(pos_izq, pos_der + 1))
        return (posiciones, suma_cruzada)


print(encontrar_maximo_subarray(precios,0,len(precios)-1))










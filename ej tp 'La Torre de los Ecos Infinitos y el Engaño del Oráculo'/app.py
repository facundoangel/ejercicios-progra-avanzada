def fib_dc(n,mapParam):
    if n <= 1:
        return n    



    clave = "{}"
    preCalculado1 = mapParam.get(clave.format(n-1),None)
    preCalculado2 = mapParam.get(clave.format(n-2),None)

    if(preCalculado1==None):
        preCalculado1 = fib_dc(n - 1,mapParam)
        mapParam[clave.format(n-1)]= preCalculado1

    if(preCalculado2==None):
        preCalculado2 = fib_dc(n - 2,mapParam)
        mapParam[clave.format(n-2)]= preCalculado2
    
    return preCalculado1 + preCalculado2  



print(fib_dc(6,{}))
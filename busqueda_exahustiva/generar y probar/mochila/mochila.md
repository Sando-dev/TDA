# Problema de la Mochila

Contamos con una mochila con una capacidad de K kilos y queremos introducir dentro de ellas un subconjunto del conjunto E de “n” elementos con el objetivo de maximizar la ganancia. Cada elemento i tiene un peso de ki kilos y un valor de vi. Los elementos no pueden ser divididos y el peso total seleccionado no puede superar la capacidad de la mochila.

# Solución mediante generar y probar

`
Sea C un vector representando un subconjunto de elementos
Inicializar C
Sea maximaGanancia = 0
Sea soluciónMáxima = C

Mientras Incrementar C <> ‘fin’
    Si Es Factible C y Ganancia C > maximaGanancia
        maximaGanancia = Ganancia C
        soluciónMáxima = C

retornar soluciónMáxima y maximaGanancia `


`
Sea C un vector de n posiciones

Inicializar C:
    Establecer cada posición del vector la C[x] en 0.

Incrementar C:
    Sea pos=n-1
    Mientras C[pos]==1 y pos>0
        C[pos]=0
        Decrementar pos
    Si pos==-1
        Retornar ‘fin’  //Overflow!
    C[pos]=1
    retornar C `

` Sea C un vector representando un subconjunto de elementos

Es Factible C:
    Sea pesoNecesario = 0
    Desde i=0 hasta n-1
        pesoNecesario += C[i] * k[i]
    retornar ( pesoNecesario <=K)

Ganancia C:
    Sea valorTotal = 0
    Desde i=0 hasta n-1
        valorTotal += C[i] * v[i]
    retornar valorTotal `
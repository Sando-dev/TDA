mochila = {
    'elemento': ['linterna', 'cantimplora', 'alfajor', 'cuchillo'],
    'peso': [2, 2, 2, 1],
    'valor': [2, 2, 3, 2]
}

def pesoTupla(tupla):
    peso = 0
    for i in range(len(tupla)):
        peso += tupla[i] * mochila['peso'][i]
    return peso

def inicializarTupla(n):
    tupla = [0] * n
    return tupla

def incrementarTupla(tupla):
    if tupla == [1] * len(tupla):
        return 'fin'
    pos = len(tupla) - 1
    while pos >= 0:
        if tupla[pos] == 1:
            tupla[pos] = 0
            pos -= 1
        else:
            tupla[pos] = 1
            break
    return tupla

def esFactibleTupla(tupla):
    pesoNecesario = pesoTupla(tupla)
    return pesoNecesario <= 4

def gananciaTupla(tupla):
    valorTotal = 0
    for i in range(len(tupla)):
        valorTotal += tupla[i] * mochila['valor'][i]
    return valorTotal

def encuentraMejorSolucion():
    n = len(mochila['elemento'])
    c = inicializarTupla(n)
    maximaGanancia = 0
    solucionMaxima = c

    while incrementarTupla(c) != 'fin':
        if esFactibleTupla(c):
            ganancia_actual = gananciaTupla(c)
            if ganancia_actual > maximaGanancia:
                maximaGanancia = ganancia_actual
                solucionMaxima = c

    return solucionMaxima, maximaGanancia

solucion, max_ganancia = encuentraMejorSolucion()
print("Mejor solución:", solucion)
print("Es factible:", esFactibleTupla(solucion))
print("Máxima ganancia:", max_ganancia)

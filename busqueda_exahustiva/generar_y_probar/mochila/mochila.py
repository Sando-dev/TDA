def encontrarMejorSolucion(n, k, v):
    def inicializarC(n):
        return [0] * n

    def incrementarC(C):
        pos = n - 1
        while pos >= 0:
            if C[pos] == 1:
                C[pos] = 0
                pos -= 1
            else:
                C[pos] = 1
                break
        if pos == -1:
            return 'fin'
        return C

    def esFactibleC(C):
        pesoNecesario = 0
        for i in range(n):
            pesoNecesario += C[i] * k[i]
        return pesoNecesario <= K

    def gananciaC(C):
        valorTotal = 0
        for i in range(n):
            valorTotal += C[i] * v[i]
        return valorTotal

    K = 4  # Peso máximo permitido
    C = inicializarC(n)
    maximaGanancia = 0
    solucionMaxima = C

    while incrementarC(C) != 'fin':
        if esFactibleC(C):
            ganancia_actual = gananciaC(C)
            if ganancia_actual > maximaGanancia:
                maximaGanancia = ganancia_actual
                solucionMaxima = C

    return solucionMaxima, maximaGanancia

# Ejemplo de uso
n = 4  # Número de elementos
k = [2, 2, 2, 1]  # Pesos de los elementos
v = [2, 2, 3, 2]  # Valores de los elementos

solucion, max_ganancia = encontrarMejorSolucion(n, k, v)
print("Mejor solución:", solucion)
print("Es factible:", solucion)
print("Máxima ganancia:", max_ganancia)
mochila = {'elemento': ['linterna','cantiplora','alfajor'], 'peso': [2, 2, 2], 'valor': [2,2,3]}

def inicializarTupla(n):
  tupla = [0] * n
  return tupla

def incrementarTupla(tupla):
  if tupla == [1,1,1]:
        return 'fin'
  pos = len(tupla) - 1
  while tupla[pos] == 1 and pos > 0:
    tupla[pos] = 0
    pos -= 1
  if pos == -1:
    return 'fin'
  tupla[pos] = 1
  return tupla

def esFactibleTupla(tupla):
  pesoNecesario = 0
  for i in range(len(tupla) - 1):
    pesoNecesario += tupla[i] * mochila['peso'][i]
  return pesoNecesario

def gananciaTupla(tupla):
  valorTotal = 0
  for i in range(len(tupla)):
    valorTotal += tupla[i] * mochila['valor'][i]
  return valorTotal

c = inicializarTupla(3)
maximaGanancia = 0
solucionMaxima = c

while incrementarTupla(c) != 'fin':
  if esFactibleTupla(c) and gananciaTupla(c) > maximaGanancia:
    maximaGanancia = gananciaTupla(c)
    solucionMaxima = c

print(solucionMaxima)
print(esFactibleTupla(solucionMaxima))
print(maximaGanancia)

#Calculando o distância da rota

def rota_distancia(rota):
  distancia_total = 0
  for (cidade , distancia) in rota:
    distancia_total += distancia
  return distancia_total

#Busca por Distância Uniforme

def bcu(mapa, inicio, objetivo):
  visitado = []
  fila = [[(inicio , 0)]]
  while fila:
    fila.sort(key=rota_distancia)
    rota = fila.pop(0)
    cidade = rota[-1][0]
    if rota in visitado:
      continue
    visitado.append(cidade)
    if cidade == objetivo:
      return rota
    else:
      cidades_interligadas = mapa.get(cidade, [])
      for (cidade2, distancia) in cidades_interligadas:
        nova_rota = rota.copy()
        nova_rota.append((cidade2, distancia))
        fila.append(nova_rota)


#Formatar a rota

def formatar(caminho):

  cidades_caminho = ''

  for i in caminho:
    cidades_caminho += i[0]+', '
  cidades_caminho = cidades_caminho[:-2]
  cidades_caminho += '.'

  return cidades_caminho
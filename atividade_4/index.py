from itertools import permutations


cidades = ['Manaus', 'Salvador', 'Maricá', 'São Gonçalo', 'Búzios']

coordenadas = {
    'Manaus': (-3.1190275, -60.0217316),
    'Salvador': (-12.972224, -38.501675),
    'Maricá': (-22.929722, -42.820833),
    'São Gonçalo': (-22.825500, -43.053900),
    'Búzios': (-22.7469829, -41.8874129)
}


permutacoes = permutations(cidades)


menor_caminho = float('inf')


for permutacao in permutacoes:

    distancia_percorrida = 0
    
    permutacao_completa = permutacao + (permutacao[0],)
   
    for i in range(len(permutacao_completa)-1):
        cidade_origem = coordenadas[permutacao_completa[i]]
        cidade_destino = coordenadas[permutacao_completa[i+1]]
        distancia = ((cidade_destino[0] - cidade_origem[0])**2 + (cidade_destino[1] - cidade_origem[1])**2)**0.5
        distancia_percorrida += distancia
    
    if distancia_percorrida < menor_caminho:
        menor_caminho = distancia_percorrida
        menor_permutacao = permutacao_completa


print('Menor distância percorrida:', menor_caminho)
print('Ordem de visitação das cidades:')
for cidade in menor_permutacao:
    print(cidade)

# O código implementa o algoritmo de força bruta para resolver o problema do caixeiro viajante, que 
# consiste em determinar a menor rota possível que um vendedor pode fazer para visitar um conjunto 
# de cidades uma única vez, partindo e retornando à cidade de origem. O código gera todas as 
# possíveis permutações das cidades, calcula a distância entre cada par de cidades na permutação e 
# atualiza a menor distância encontrada até então. 
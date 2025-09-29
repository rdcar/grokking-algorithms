# O grafo é um dicionário que armazena outros dicionários
grafo = {}

# Nó "início"
grafo["inicio"] = {}
grafo["inicio"]["a"] = 6 # De 'inicio' para 'a', o custo é 6
grafo["inicio"]["b"] = 2 # De 'inicio' para 'b', o custo é 2

# Nó "a"
grafo["a"] = {}
grafo["a"]["fim"] = 1 # De 'a' para 'fim', o custo é 1

# Nó "b"
grafo["b"] = {}
grafo["b"]["a"] = 3 # De 'b' para 'a', o custo é 3
grafo["b"]["fim"] = 5 # De 'b' para 'fim', o custo é 5

# Nó "fim" - não leva a mais nenhum lugar
grafo["fim"] = {}

# A tabela de custos
infinito = float("inf")
custos = {}
custos["a"] = 6       # Custo inicial de "inicio" para "a"
custos["b"] = 2       # Custo inicial de "inicio" para "b"
custos["fim"] = infinito # Custo inicial de "inicio" para "fim" é infinito (ainda não chegamos lá)

# A tabela de pais
pais = {}
pais["a"] = "inicio"  # Para chegar em "a", o nó anterior é "inicio"
pais["b"] = "inicio"  # Para chegar em "b", o nó anterior é "inicio"
pais["fim"] = None    # O "fim" ainda não tem um "pai" definido.

processados = [] # Garante que cada nó processado seja adicionado à lista e não seja processado novamente

def ache_no_custo_mais_baixo(custos):
    """
    Percorre a tabela custos e retorna o nó que tem o caminho mais curto conhecido a partir 
    do inicio e que ainda não foi visitado.
    """
    custo_mais_baixo = float("inf")
    nodo_custo_mais_baixo = None
    # Percorra em cada nodo
    for nodo in custos:
        custo = custos[nodo]
        # Se o custo é o mais baixo que já vimos E o nó ainda não foi processado...
        if custo < custo_mais_baixo and nodo not in processados:
            custo_mais_baixo = custo
            nodo_custo_mais_baixo = nodo
    return nodo_custo_mais_baixo

nodo = ache_no_custo_mais_baixo(custos) # 1. Começa com o nó de menor custo (que será "b" com custo 2)

while nodo is not None:
    custo = custos[nodo]          # Custo do "inicio" até o nó atual
    vizinhos = grafo[nodo]        # Dicionário de vizinhos do nó atual

    for n in vizinhos.keys():     # Para cada vizinho ('n') do nó atual...
        novo_custo = custo + vizinhos[n]  # ... calcule o custo total para chegar no vizinho,
                                          #    passando pelo nó atual.
                            
        # Esta é a parte mais importante:
        if custos[n] > novo_custo:
            custos[n] = novo_custo  # Se o NOVO caminho for mais barato que o caminho ATUALmente conhecido,
            pais[n] = nodo          # ... ATUALIZA a tabela de custos e de pais.

    processados.append(nodo)      # Marca o nó atual como processado.
    nodo = ache_no_custo_mais_baixo(custos) # Encontra o próximo nó de menor custo ainda não processado.

print("Custo do Início à cada um dos nodos (vértices): ")
print(custos)
#Custo do Início à cada um dos nodos (vértices): {'a': 5, 'b': 2, 'fim': 6}
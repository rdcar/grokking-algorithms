# Algoritmo de Dijkstra   

O **Algoritmo de Dijkstra** é um algoritmo guloso (greedy) usado para encontrar o caminho mais curto entre um nó inicial (fonte) e todos os outros nós em um **grafo ponderado e direcionado (ou acíclicos dirigidos)**. Ele funciona iterativamente, explorando o nó mais "barato" (de menor custo) ainda não processado e atualizando o custo para alcançar seus vizinhos.

O algoritmo de Dijkstra é ideal para problemas de roteamento.

- **Roteamento em Mapas:** Imagine um GPS que precisa encontrar o caminho mais rápido ou mais curto de um ponto **A** a um ponto **B**. As ruas são as arestas (arestas com direção em ruas de mão única), e o tempo de percurso ou a distância são os pesos. Dijkstra calcula a rota de menor custo total.

## Limitação Principal

A principal **limitação** do Algoritmo de Dijkstra é sua ineficácia na presença de **arestas com pesos negativos** e a **presença de ciclos** (ou grafos não direcionados pois, neles, cada vértice é considerado um ciclo).

* **Grafos com Pesos Negativos:** Quando um grafo contém arestas com pesos negativos, o algoritmo pode **não encontrar o caminho mais curto correto**. Isso ocorre porque o princípio guloso do Dijkstra (escolher o caminho mais barato conhecido) não consegue lidar com a possibilidade de uma aresta de peso negativo reduzir o custo total de um caminho que já foi considerado o mais curto.
* **Solução Alternativa:** Para grafos com pesos negativos (desde que não haja ciclos de peso negativo), o **Algoritmo de Bellman-Ford** é geralmente a alternativa mais indicada (porém, não foi abordado neste livro).

## Explicação detalhada do código

## 1\. O Grafo (A Rede)

O grafo é a representação da nossa rede de pontos e caminhos. Pense nele como um mapa:

```python
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
```

  * **O que é:** O dicionário `grafo` diz, para cada ponto de partida, quais são seus vizinhos e qual o **peso (custo)** para chegar até eles.
  * **Exemplo:** `grafo["inicio"]["b"] = 2` significa que, do ponto "inicio" para o ponto "b", o custo (ou tempo, ou distância) é **2**.

## 2\. Tabelas de Controle

O algoritmo precisa de algumas tabelas para manter o controle do caminho mais curto encontrado até agora:

### A Tabela de Custos (`custos`)

```python
infinito = float("inf")
custos = {}
custos["a"] = 6       # Custo inicial de "inicio" para "a"
custos["b"] = 2       # Custo inicial de "inicio" para "b"
custos["fim"] = infinito # Custo inicial de "inicio" para "fim" é infinito (ainda não chegamos lá)
```

  * **O que é:** Um dicionário que armazena o **custo mais baixo conhecido** do ponto de partida (`inicio`) até todos os outros pontos.
  * **Importante:** Pontos que não são vizinhos diretos do `inicio` (como o `fim`) recebem um valor de **`infinito`** (`float("inf")`), significando que ainda não encontramos um caminho para eles.

### A Tabela de Pais (`pais`)

```python
pais = {}
pais["a"] = "inicio"  # Para chegar em "a", o nó anterior é "inicio"
pais["b"] = "inicio"  # Para chegar em "b", o nó anterior é "inicio"
pais["fim"] = None    # O "fim" ainda não tem um "pai" definido.
```

  * **O que é:** Um dicionário que armazena o **nó anterior** (o "pai") no caminho mais curto encontrado até o momento. Isso nos permitirá reconstruir o caminho final.

### Processados (`processados`)

```python
processados = []
```

  * **O que é:** Uma **lista** que armazena os nós (pontos) que já foram visitados e tiveram seus vizinhos checados. Isso evita que o algoritmo caia em ciclos e garante que cada nó seja processado apenas uma vez.


## 3\. A Função Auxiliar

Esta função é a alma do algoritmo guloso (greedy): ela sempre escolhe o melhor movimento *no momento*.

```python
def ache_no_custo_mais_baixo(custos):
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
```

  * **O que ela faz:** Percorre a tabela `custos` e retorna o **nó que tem o caminho mais curto conhecido** a partir do `inicio` *e* que ainda não foi visitado.


## 4\. O Loop Principal do Algoritmo

Aqui é onde a mágica acontece. O loop continua até que todos os nós acessíveis tenham sido processados.

```python
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
```

### O que acontece no Loop?

1.  Ele começa com o nó de menor custo: **"b" (custo 2)**.
2.  Ele olha os vizinhos de "b" ("a" e "fim").
      * **Para "a":** O custo de "inicio" para "a" é 6. Se passarmos por "b", o custo é: `2` (até b) + `3` (de b para a) = **5**. Como **5 é menor que 6**, ele **atualiza** `custos["a"]` para 5 e `pais["a"]` para "b".
      * **Para "fim":** O custo de "inicio" para "fim" é infinito. Se passarmos por "b", o custo é: `2` (até b) + `5` (de b para fim) = **7**. Ele **atualiza** `custos["fim"]` para 7.
3.  "b" é adicionado aos `processados`.
4.  Ele encontra o próximo nó de menor custo não processado, que agora é **"a" (custo 5)**.
5.  ... E o processo se repete até que não haja mais nós a serem checados.

**Resultado Final:** O algoritmo encontra o caminho mais curto, que é **Inicio -\> b (2) -\> a (3) -\> fim (1)**, com um custo total de **6**.

O algoritmo de Dijkstra garante que, ao final do loop, a tabela `custos` tenha os valores mínimos de custo para todos os nós e a tabela `pais` seja preenchida com os nodos cujos custos são os menores possíveis.

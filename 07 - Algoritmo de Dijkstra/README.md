# Algoritmo de Dijkstra   

O **Algoritmo de Dijkstra** é um algoritmo guloso (greedy) usado para encontrar o caminho mais curto entre um nó inicial (fonte) e todos os outros nós em um **grafo ponderado e direcionado (ou acíclicos dirigidos)**. Ele funciona iterativamente, explorando o nó mais "barato" (de menor custo) ainda não processado e atualizando o custo para alcançar seus vizinhos.

O algoritmo de Dijkstra é ideal para problemas de roteamento.

- **Roteamento em Mapas:** Imagine um GPS que precisa encontrar o caminho mais rápido ou mais curto de um ponto **A** a um ponto **B**. As ruas são as arestas (arestas com direção em ruas de mão única), e o tempo de percurso ou a distância são os pesos. Dijkstra calcula a rota de menor custo total.

## Limitação Principal

A principal **limitação** do Algoritmo de Dijkstra é sua ineficácia na presença de **arestas com pesos negativos** e a **presença de ciclos** (ou grafos não direcionados pois, neles, cada vértice é considerado um ciclo).

* **Grafos com Pesos Negativos:** Quando um grafo contém arestas com pesos negativos, o algoritmo pode **não encontrar o caminho mais curto correto**. Isso ocorre porque o princípio guloso do Dijkstra (escolher o caminho mais barato conhecido) não consegue lidar com a possibilidade de uma aresta de peso negativo reduzir o custo total de um caminho que já foi considerado o mais curto.
* **Solução Alternativa:** Para grafos com pesos negativos (desde que não haja ciclos de peso negativo), o **Algoritmo de Bellman-Ford** é geralmente a alternativa mais indicada (poré, não foi abordado neste livro).
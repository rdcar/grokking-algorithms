# Pesquisa Binária
- Algoritmo que usa arrays ordenados para pesquisar a posição de um determinado item
- Tempo de execução O(Log n)
- Quando maior a lista, melhor a performance

# Notação BigO
- Notação especial que diz sobre a complexidade de processamento (quantidade de passos) de um algoritmo considerando o pior cenário possível
- Não é medido em segundos, mas sim pelo crescimento no número de operações

## Exemplos
- O(log n): pesquisa binária
- O(n): tempo linear (pesquisa simples)
- O(n * log n): algoritmo rápido de ordenação (quicksort)
- O(n^2): algoritmo lento de ordenação (ordenação por seleção)
- O(n!): caixeiro viajante

## Caixeiro Viajante
O caixeiro viajante Opus precisa ir em cinco cidades. Mas ele quer passar por todas as cidades percorrendo a menor distância possível. Para isso, temos que analisar cada ordem possível de cidades para visitar e somar todas as distâncias.

| Cidades | Operações | 
|----------|:--------:|
| 6 | 720 |
| 7 | 5040 |
| 8 | 40320 |
| ... | ... |
| 15 |  1307674368000 |

O número de operações aumenta drasticamente.
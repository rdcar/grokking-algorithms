# Quicksort

## Estratégia Dividir para Conquistar
- O Quicksort é baseado na técnica **divide and conquer**.  
- A cada passo:
  1. Escolhe-se um **pivô**.  
  2. Particiona-se o array em dois subarrays: elementos **menores** que o pivô e elementos **maiores** que o pivô.  
  3. Aplica-se o mesmo processo recursivamente aos subarrays.  


## Escolha do Pivô
- **Aleatório**: reduz a probabilidade de cair nos piores casos (quando o pivô escolhido gera partições muito desbalanceadas).  
- **Mediano (ideal)**: garante o balanceamento ótimo das partições, resultando em melhor desempenho médio.  
- **Impacto**:
  - Pivô mal escolhido (ex.: sempre o primeiro ou último em array já ordenado) → pior caso.  
  - Pivô bem escolhido (ex.: mediana ou aleatório) → desempenho próximo ao ótimo.  


## Complexidade em BigO
- **Melhor caso**: `O(n log n)`  
- **Caso médio**: `O(n log n)`  
- **Pior caso**: `O(n²)` (quando o pivô é consistentemente ruim)  


## Constante na Notação BigO
- Apesar de ter a mesma ordem assintótica de outros algoritmos de ordenação (`O(n log n)`), o **Quicksort tende a ser mais rápido na prática** por causa de uma **constante pequena**:  
  - Usa operações simples (comparações e trocas).  
  - Favorece **localidade de memória**, aproveitando melhor o cache da CPU.  
- Essa constante faz diferença prática, mesmo que assintoticamente outros algoritmos (como MergeSort) tenham a mesma complexidade.  

# Arrays & Listas Concatenadas

## Arrays
- Sequência contígua de memória (dados armazenados lado a lado)
- Desperdício de memória pois é preciso pré-alocar antes mesmo de preencher com dados
- Inserção e deleção demoradas pois é preciso mover todos os itens caso seja necessário inserir novos itens antes do último
- Leitura rápida, pois não é preciso percorrer todos os dados sequencialmente para lê-los

## Listas Concatenadas
- Armazenamento em diferentes locais de memória contendo, cada um deles, um ponteiro localizador para o próximo item
- Cada item armazena o endereço do próximo item da lista
- Leitura demorada pois precisa percorrer todos os elementos caso você queira saber o último elemento
- Inserção e remoção rápidos pois somente é preciso saber a posição do último elemento para adicionar novos ou mudar o endereço para o qual o elemento anterior está apontando

|  | Arrays | Listas |
|----------|:--------:|--------:|
| Leitura | O(1) | O(n) |
| Inserção | O(n) | O(1) |
| Eliminação | O(n) | O(1) |

Dica:
- Array: aleatório
- Lista: sequencial

# Resumo Ordenação por Selecão (Crescente)

1. Crie uma nova lista vazia para armazenar a lista ordenada
2. Faça um loop na lista original e encontre o menor valor dentro do loop
3. Armazena o índice do menor valor
4. Adicione o menor valor encontrado na nova lista criada no passo 1 usando o método append()
5. Remova o menor valor encontrado da lista original usando o método pop() e o índice encontrado no passo 3
6.Repita os passos 2 a 4 até que a lista original esteja vazia
7. Retorne a nova lista criada no passo 1, que contém a lista original ordenada

- Tempo de execução: O(n * n) = O(n^2)
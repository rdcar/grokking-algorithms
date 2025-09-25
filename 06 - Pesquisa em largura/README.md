# Algoritmo de Pesquisa em Largura

## Introdução a Grafos

Um **grafo** é uma estrutura de dados que representa conexões entre objetos. Ele consiste em **nós** (ou vértices) e **arestas**, que são as ligações entre esses nós. Grafos são usados para modelar uma ampla gama de problemas, como redes sociais, mapas de rotas e circuitos elétricos. O algoritmo de **pesquisa em largura** é utilizado para encontrar o caminho mais curto entre dois nós em um grafo.

## Pesquisa em Largura

A pesquisa em largura (Breadth-First Search - **BFS**) é um algoritmo para explorar um grafo de forma "ampla". Ele começa em um nó inicial e explora todos os vizinhos diretos (nível 1) antes de passar para os vizinhos dos vizinhos (nível 2), e assim por diante. Esse processo garante que o primeiro caminho encontrado até o nó de destino será o caminho **mínimo** (em número de arestas). Para gerenciar a ordem de exploração, a BFS utiliza uma estrutura de dados do tipo **fila** (FIFO - First-In, First-Out), onde os nós a serem visitados são adicionados e removidos.

## Implementando o Grafo

Para implementar um grafo, um **dicionário** (ou tabela hash) é uma escolha eficiente. Cada chave do dicionário representa um nó, e o valor associado é uma lista dos vizinhos desse nó. Por exemplo, `graph['voce'] = ['alice', 'bob', 'claire']` indica que você está conectado a Alice, Bob e Claire.   
Ao implementar o algoritmo de busca em largura (BFS), é crucial garantir que cada nó seja processado **apenas uma vez**. Para isso, você pode usar uma estrutura de dados para manter o controle dos nós que já foram visitados.
Uma forma eficaz de fazer isso é criando um conjunto (set) ou lista chamado `visitados`. Conforme o algoritmo avança, você adiciona cada nó que acabou de processar a esse conjunto. Antes de explorar os vizinhos de um nó, você verifica se o nó já está em visitados. Se sim, você o ignora e passa para o próximo. Isso evita ciclos e o reprocessamento desnecessário, garantindo que o algoritmo seja eficiente.

## Implementando o Algoritmo e seu Tempo de Execução

A implementação da BFS envolve:

1.  Uma **fila** para armazenar os nós a serem visitados.
2.  Um conjunto ou lista para manter um registro dos nós **já visitados**, evitando ciclos infinitos.
3.  Um laço `while` que continua enquanto a fila não estiver vazia.

A cada iteração do laço, um nó é removido da fila, seus vizinhos são inspecionados, e os que ainda não foram visitados são adicionados à fila. O tempo de execução da pesquisa em largura é de **O(V + E)**, onde **V** é o número de vértices (nós) e **E** é o número de arestas do grafo. Isso ocorre porque, no pior cenário, o algoritmo precisa visitar cada nó e cada aresta uma única vez.

## Diferença entre as funções pesquisa1 (minha) e pesquisa2 (autor)   

Os dois códigos apresentados, `pesquisa1` e `pesquisa2`, implementam o algoritmo de busca em largura (BFS) com algumas diferenças notáveis. Embora ambos consigam encontrar o "vendedor de manga" no grafo, a maneira como eles gerenciam a fila e a lista de pessoas verificadas é a principal distinção.

### Análise do Código 1 (`pesquisa1`)

Este algoritmo é mais eficiente em termos de processamento, pois ele faz a checagem da lista de pessoas verificadas antes de adicionar os novos vizinhos à fila.

* **Gerenciamento da Fila:** A fila de pesquisa é populada com os vizinhos do nó atual.
* **Gerenciamento das Pessoas Verificadas:** O conjunto `verificadas` é usado para armazenar as pessoas já processadas. Um `set` (conjunto) em Python é otimizado para operações de busca, inserção e remoção. Isso significa que a verificação `if vizinho not in verificadas` é muito rápida.
* **Lógica:** Quando uma pessoa é retirada da fila (`fila_de_pesquisa.popleft()`), ela é verificada para ver se é um vendedor. Se não for, ela é adicionada **imediatamente** ao conjunto `verificadas`. Em seguida, seus vizinhos só são adicionados à fila se ainda não estiverem nesse conjunto.

Essa abordagem garante que uma pessoa só seja adicionada à fila de pesquisa uma única vez, o que evita processar o mesmo nó múltiplas vezes e previne loops infinitos em grafos com ciclos. O uso de um `set` para a lista de verificadas também torna o algoritmo mais rápido.

### Análise do Código 2 (`pesquisa2`)

Este segundo algoritmo, embora funcional, é menos otimizado.

* **Gerenciamento da Fila:** Os vizinhos são adicionados à fila sem uma verificação prévia. Isso pode resultar em vizinhos já visitados sendo adicionados à fila e processados novamente.
* **Gerenciamento das Pessoas Verificadas:** A lista `verificadas` é uma lista (`[]`), não um conjunto (`set()`). A busca por um elemento em uma lista (`if not pessoa in verificadas`) é menos eficiente em Python do que a busca em um conjunto.
* **Lógica:** A verificação se a pessoa já foi visitada (`if not pessoa in verificadas`) é feita **apenas quando a pessoa é retirada da fila**. Se um nó tem múltiplos caminhos, ele pode ser adicionado à fila mais de uma vez, e a verificação só ocorrerá quando ele for processado.

### Qual código é melhor?

O **código 1 (`pesquisa1`) é superior** em termos de eficiência e robustez.

1.  **Evita Duplicação na Fila:** Ele verifica se uma pessoa já foi visitada antes de adicioná-la à fila, o que mantém a fila menor e mais organizada.
2.  **Eficiência:** O uso de um **conjunto (`set`)** para as pessoas verificadas é mais rápido para operações de busca do que uma lista, o que melhora o desempenho geral do algoritmo, especialmente em grafos grandes.

Ambos os algoritmos funcionam para o grafo dado, mas o primeiro é a melhor prática para implementar a busca em largura, pois é mais eficiente e evita problemas em grafos mais complexos.
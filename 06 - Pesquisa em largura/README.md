## Algoritmo de Pesquisa em Largura

### Introdução a Grafos

Um **grafo** é uma estrutura de dados que representa conexões entre objetos. Ele consiste em **nós** (ou vértices) e **arestas**, que são as ligações entre esses nós. Grafos são usados para modelar uma ampla gama de problemas, como redes sociais, mapas de rotas e circuitos elétricos. O algoritmo de **pesquisa em largura** é utilizado para encontrar o caminho mais curto entre dois nós em um grafo.

### Pesquisa em Largura

A pesquisa em largura (Breadth-First Search - **BFS**) é um algoritmo para explorar um grafo de forma "ampla". Ele começa em um nó inicial e explora todos os vizinhos diretos (nível 1) antes de passar para os vizinhos dos vizinhos (nível 2), e assim por diante. Esse processo garante que o primeiro caminho encontrado até o nó de destino será o caminho **mínimo** (em número de arestas). Para gerenciar a ordem de exploração, a BFS utiliza uma estrutura de dados do tipo **fila** (FIFO - First-In, First-Out), onde os nós a serem visitados são adicionados e removidos.

### Implementando o Grafo

Para implementar um grafo, um **dicionário** (ou tabela hash) é uma escolha eficiente. Cada chave do dicionário representa um nó, e o valor associado é uma lista dos vizinhos desse nó. Por exemplo, `graph['voce'] = ['alice', 'bob', 'claire']` indica que você está conectado a Alice, Bob e Claire.   
Ao implementar o algoritmo de busca em largura (BFS), é crucial garantir que cada nó seja processado **apenas uma vez**. Para isso, você pode usar uma estrutura de dados para manter o controle dos nós que já foram visitados.
Uma forma eficaz de fazer isso é criando um conjunto (set) ou lista chamado `visitados`. Conforme o algoritmo avança, você adiciona cada nó que acabou de processar a esse conjunto. Antes de explorar os vizinhos de um nó, você verifica se o nó já está em visitados. Se sim, você o ignora e passa para o próximo. Isso evita ciclos e o reprocessamento desnecessário, garantindo que o algoritmo seja eficiente.

### Implementando o Algoritmo e seu Tempo de Execução

A implementação da BFS envolve:

1.  Uma **fila** para armazenar os nós a serem visitados.
2.  Um conjunto ou lista para manter um registro dos nós **já visitados**, evitando ciclos infinitos.
3.  Um laço `while` que continua enquanto a fila não estiver vazia.

A cada iteração do laço, um nó é removido da fila, seus vizinhos são inspecionados, e os que ainda não foram visitados são adicionados à fila. O tempo de execução da pesquisa em largura é de **O(V + E)**, onde **V** é o número de vértices (nós) e **E** é o número de arestas do grafo. Isso ocorre porque, no pior cenário, o algoritmo precisa visitar cada nó e cada aresta uma única vez.
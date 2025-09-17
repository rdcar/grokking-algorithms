# Tabelas Hash

As tabelas hash, ou dicionários em Python, são uma estrutura de dados incrivelmente eficiente e fundamental para a programação. Elas armazenam pares de **chave-valor**, permitindo um acesso muito rápido aos dados, com uma complexidade de tempo média de O(1) e O(n) no pior cenário. A chave é usada para encontrar o valor correspondente, semelhante a como você usaria um índice para encontrar um livro em uma biblioteca.

# Funções Hash

Uma **função hash** é o coração de uma tabela hash. Ela pega uma chave (como uma string, um número ou uma tupla) e a transforma em um número inteiro, chamado de **código hash**. Este código hash é então usado para determinar a posição onde o valor será armazenado na tabela. Uma boa função hash distribui as chaves uniformemente, o que é crucial para o desempenho.

Em Python, a função `hash()` é usada internamente para gerar esses códigos. Por exemplo, `hash('minha_chave')` retornará um número que a tabela hash (o dicionário) usará para armazenar ou recuperar o valor associado.

# Utilização

As tabelas hash são usadas em inúmeras aplicações. Sua principal vantagem é a velocidade de busca, inserção e exclusão.

* **Pesquisa:** A pesquisa de um valor por sua chave é quase instantânea O(1). Isso as torna ideais para tarefas como verificar se um item existe em uma coleção.
* **Evitando Entradas Duplicadas:** Ao usar as chaves de um dicionário, você garante que cada entrada seja única, pois uma chave só pode existir uma vez. Isso é útil para eliminar duplicatas de uma lista.
* **Como Cache:** Elas podem atuar como um **cache** temporário. Você pode armazenar o resultado de uma operação computacionalmente cara usando uma chave. Se a mesma operação for solicitada novamente com a mesma chave, você pode simplesmente recuperar o resultado do cache em vez de recalcular.

# Colisões

Uma **colisão** ocorre quando a função hash gera o mesmo código hash para duas chaves diferentes. Como duas chaves não podem ser armazenadas no mesmo lugar, a tabela hash precisa de uma estratégia para lidar com isso. Python, por exemplo, usa uma abordagem chamada **encadeamento separado** (separate chaining), onde cada "balde" da tabela pode conter uma lista de pares de chave-valor. Se uma colisão acontece, o novo par é simplesmente adicionado a essa lista.

# Desempenho

O desempenho de uma tabela hash depende de alguns fatores:

* **Fator de Carga:** É a razão entre o número de itens armazenados e o número de "baldes" na tabela. Um fator de carga alto (muitos itens por balde) pode diminuir o desempenho, pois as listas de encadeamento ficam mais longas. Python redimensiona a tabela internamente quando o fator de carga atinge um certo limite, criando mais baldes e redistribuindo os itens (um processo chamado "rehashing") para manter o desempenho.

* **Uma Boa Função Hash:** Uma função hash que distribui as chaves de forma uniforme é essencial. Se a função hash for ruim, muitas colisões ocorrerão, e o tempo de busca pode se aproximar de O(n), o que anula a principal vantagem da estrutura. A função `hash()` de Python é projetada para ser eficiente e evitar colisões. Nós, provavelmente, nunca implementaremos uma função hash do zero, mas é importante entender o que ocorre por debaixo dos panos.
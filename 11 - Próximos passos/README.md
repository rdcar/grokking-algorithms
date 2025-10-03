# Próximos passos

Neste capítulo, o autor menciona rapidamente dez outros algoritmos interessantes que não foram abordados no livro mas que são amplamente utilizados na computação cotidiana.

---

**Árvores (Árvore Binária de Busca)**
A Árvore Binária de Busca é uma estrutura de dados proposta para melhorar a inserção e remoção em arrays ordenados, especialmente porque a pesquisa binária exige que os dados estejam ordenados, o que torna a inserção de novos elementos lenta. Em uma Árvore Binária de Busca, os nós à esquerda de um nó-raiz têm valores menores, e os nós à direita têm valores maiores, tornando a pesquisa semelhante à pesquisa binária, com tempo de execução médio de $O(\log n)$. No entanto, esta estrutura possui desvantagens como a falta de acesso aleatório, e seu bom desempenho depende fortemente de a árvore estar **balanceada**; árvores não balanceadas funcionam mal. Algumas implementações especiais, como as **Árvores B** e as **árvores vermelho-preto**, lidam com o balanceamento e são frequentemente usadas para armazenar dados em bancos de dados.

**Índices Invertidos**
Os índices invertidos são uma estrutura de dados muito utilizada na construção de ferramentas de busca. Essencialmente, é uma **tabela hash** onde as **chaves** são palavras e os **valores** são as páginas nas quais essa palavra aparece. Essa estrutura permite que, quando um usuário pesquisa uma palavra, a ferramenta de busca retorne rapidamente as páginas relevantes que contêm a palavra em questão.

**A Transformada de Fourier**
A Transformada de Fourier é um algoritmo elegante e versátil, frequentemente explicado como a capacidade de, dado um "smoothie" (um sinal complexo), determinar seus ingredientes (frequências individuais). É amplamente utilizada no **processamento de sinais**, permitindo, por exemplo, separar uma música em frequências para ajustar agudos ou graves. Também é fundamental na **compressão de dados** em formatos como **MP3** e **JPG**, onde se eliminam as frequências ou notas menos importantes, e possui aplicações em análise de DNA, previsão de terremotos e aplicativos de identificação musical como o Shazam.

**Algoritmos Paralelos**
Com o limite no aumento da velocidade singular dos computadores, os algoritmos paralelos se tornaram essenciais para rodar tarefas mais rapidamente em múltiplos **núcleos de processamento** simultaneamente. Embora o melhor desempenho de um algoritmo de ordenação seja $O(n \log n)$, um algoritmo paralelo (como uma versão do quicksort) pode alcançar $O(n)$. No entanto, o projeto de algoritmos paralelos é complexo devido a desafios como o **gerenciamento do paralelismo** (dividir e unir tarefas) e o **balanceamento de carga** (garantir que todos os núcleos trabalhem de forma eficiente e não esperem por tarefas mais lentas).

**MapReduce**
MapReduce é um tipo especial de **algoritmo distribuído** projetado para **escalabilidade**, permitindo que o trabalho seja executado por diversas máquinas (centenas de núcleos). É amplamente utilizado em *frameworks* como Apache Hadoop para processar grandes volumes de dados (bilhões ou trilhões de linhas). O algoritmo baseia-se em duas funções simples: a função **map**, que aplica a mesma função a cada item de um array, muitas vezes de forma paralela, e a função **reduce**, que "reduz" uma lista inteira a um único item (como somar todos os elementos). Essa técnica é crucial para diminuir o tempo de processamento de consultas complexas em grandes conjuntos de dados.

**Filtros de Bloom**
Os Filtros de Bloom são **estruturas de dados probabilísticas** que são incrivelmente eficientes em termos de espaço e são usadas quando se lida com conjuntos de dados muito grandes, como URLs rastreadas pela Google. Eles não fornecem uma resposta exata, mas uma que é **provavelmente correta**. Sua principal característica é que são possíveis os **falsos positivos** (dizer que um item está no conjunto quando não está), mas **falsos negativos não são possíveis** (se o filtro diz que o item não está lá, ele realmente não está). Eles são úteis em casos como verificar duplicatas ou identificar sites maliciosos, onde a incerteza é aceitável em troca da economia de memória.

**HyperLogLog**
Semelhante aos Filtros de Bloom, o HyperLogLog é um algoritmo que **aproxima o número de elementos únicos** em um conjunto, usando apenas uma fração da memória necessária para o rastreamento exato. Essa ferramenta é empregada quando se tem uma grande quantidade de dados e se está satisfeito com uma resposta altamente precisa, mas não necessariamente exata, como quando a Google quer contar o número de pesquisas únicas ou a Amazon o número de itens únicos visualizados.

**Algoritmos SHA (Secure Hash Algorithm)**
SHA é uma **função hash** que recebe uma *string* e retorna uma *hash* (uma *string* curta). É caracterizada por ser **localmente insensitiva**, ou seja, uma pequena modificação na *string* de entrada resulta em uma *hash* totalmente diferente. O SHA é usado para **comparar arquivos** (dois arquivos grandes são considerados iguais se suas *hashes* SHA forem idênticas) e, principalmente, para **verificar senhas** em bancos de dados. Em vez de armazenar a senha original, apenas sua *hash* SHA é guardada, impedindo que um invasor descubra a senha original, pois o SHA funciona como uma *hash* de apenas uma direção.

**Hash Sensitivo Local (Simhash)**
A Simhash é o oposto do SHA, sendo uma **função hash localmente sensitiva**. Se você fizer uma pequena mudança na *string* de entrada, a *hash* gerada será apenas **levemente diferente**, permitindo que se compare as *hashes* para verificar **o quão semelhantes as *strings* originais são**. Essa propriedade é extremamente útil para detectar duplicatas ou similaridades em larga escala, como a Google rastrear páginas duplicadas na web ou o Scribd verificar se um documento carregado se assemelha a material com direitos autorais.

**Troca de Chaves de Diffie-Hellman**
Este algoritmo é um método elegante para resolver o problema de como duas partes podem concordar em uma cifra secreta de forma segura, sem se encontrarem ou trocarem informações secretas por canais inseguros. Ele utiliza uma **chave pública** (que pode ser divulgada livremente e é usada para criptografar mensagens) e uma **chave privada** (que apenas o destinatário possui e que é necessária para decodificar as mensagens). A troca de chaves Diffie-Hellman, juntamente com seu sucessor RSA, garante que as mensagens criptografadas sejam extremamente difíceis de decodificar sem a chave privada.

**Programação Linear**
A Programação Linear é um *framework* geral de otimização que é usado para **maximizar algo em relação a um limite**. Os exemplos incluem maximizar o lucro de produtos dada uma quantidade limitada de material disponível (como tecido e botões) ou maximizar votos dentro de um orçamento e tempo definidos. É um conceito muito geral, de modo que **todos os algoritmos de grafos podem ser formulados por meio da programação linear**, sendo os problemas de grafos apenas um subconjunto. A solução da Programação Linear é encontrada utilizando o complexo **algoritmo Simplex**.
# Programação Dinâmica

A Programação Dinâmica (PD) é uma **técnica para resolução de problemas complexos** que se baseia na divisão de um problema em subproblemas, os quais são resolvidos separadamente. É útil quando se busca **otimizar algo em relação a um limite**, e quando o problema pode ser dividido em **subproblemas discretos** que não dependem um do outro.

Toda solução de programação dinâmica envolve a criação de uma **tabela**, e o algoritmo começa resolvendo subproblemas e os escalando até resolver o problema geral.

## O Problema da Mochila (Knapsack Problem)

O problema da mochila busca **maximizar o valor dos itens roubados** em uma mochila com capacidade limitada (e.g., 16 quilos).

| Característica | Descrição |
| :--- | :--- |
| **Solução Simples (Ineficiente)** | Testar todos os conjuntos de itens possíveis (força bruta). É **muito lenta**, com tempo de execução O($2^n$), sendo impraticável. |
| **Solução Programação Dinâmica** | Envolve a criação de uma **tabela** onde as linhas representam os **itens** e as colunas representam as **capacidades da mochila** (submochilas). Os valores das células são o valor máximo que se pode roubar para aquela capacidade e conjunto de itens. Ao preencher as células, compara-se o valor máximo atual com o valor de incluir o item (valor do item + valor do espaço restante, usando a solução de um subproblema anterior). |

**Perguntas Frequentes sobre a PD no Problema da Mochila:**

*   **Adição de Itens:** Para adicionar um item, basta adicionar uma **nova linha** à tabela e continuar o cálculo. A estimativa máxima em uma coluna nunca pode diminuir.
*   **Ordem das Linhas/Colunas:** A ordem das linhas não importa para a resposta final. Preencher a tabela a partir das colunas, em vez das linhas, geralmente não faz diferença neste problema.
*   **Itens Fracionados:** A PD aplica-se a problemas de "tudo ou nada", <ins>não sendo possível levar frações de um item</ins>. Itens fracionados são resolvidos mais facilmente com um **algoritmo guloso**.
*   **Interdependência:** A PD **não funciona** quando os subproblemas não são discretos, ou seja, se eles dependem uns dos outros. Um exemplo disso é o custo de viagem, onde a inclusão de um item torna o acesso a outro mais "barato" (custo de viagem a Paris).

## Maior Substring Comum (Longest Common Substring)

Este problema pode ser usado em **corretores ortográficos** para encontrar a maior similaridade entre duas palavras.

*   **Tabela de PD:** Os eixos da tabela são as **duas palavras** que estão sendo comparadas (comparando substrings).
*   **Valores das Células:** O comprimento da **maior substring** que duas substrings têm em comum.
*   **Fórmula (Pseudocódigo):**
    *   Se as letras combinarem: `celula[i][j] = celula[i-1][j-1] + 1`.
    *   Se as letras não combinarem: `celula[i][j] = 0`.
*   **Solução:** É o **maior número** encontrado em qualquer célula da tabela.

## Maior Subsequência Comum (Longest Common Subsequence)

Busca o número de **letras em sequência** (não necessariamente contíguas) que duas palavras têm em comum.

*   **Fórmula (Pseudocódigo):**
    *   Se as letras combinarem: `celula[i][j] = celula[i-1][j-1] + 1`.
    *   Se as letras não combinarem: `celula[i][j] = max(celula[i-1][j], celula[i][j-1])`.
*   **Aplicações Práticas:** É utilizada por biólogos para encontrar **similaridades em fitas de DNA**, no comando `diff` (como `git diff`) para informar diferenças entre arquivos, na **Distância Levenshtein** para medir a similaridade de strings, e em aplicativos que fazem quebras de linhas, como o Microsoft Word.

## Recapitulando Programação Dinâmica

*   A PD é útil quando se está tentando **otimizar algo em relação a um limite**.
*   Funciona quando o problema pode ser **dividido em subproblemas discretos**.
*   Todas as soluções em PD envolvem uma **tabela**.
*   Os valores nas células são, em geral, o que se está tentando otimizar.
*   Não existe uma fórmula única para calcular uma solução em programação dinâmica.
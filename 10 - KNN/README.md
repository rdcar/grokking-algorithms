# Capítulo 10: K-Vizinhos Mais Próximos (K-Nearest Neighbors - KNN)

O algoritmo dos k-vizinhos mais próximos é uma técnica de aprendizado de máquina utilizada principalmente para **classificação** e **regressão**. É um algoritmo **simples** e frequentemente é uma boa ideia tentar usá-lo primeiro ao tentar classificar algo. O valor de **K** refere-se ao número de vizinhos próximos considerados, podendo ser dois, dez ou dez mil, e não há nada de especial no número 5 (usado como exemplo).

## Classificação

O KNN é usado para classificar objetos em grupos.

1.  **Princípio da Classificação:** Para classificar um objeto desconhecido (como uma fruta), o algoritmo observa seus **vizinhos mais próximos**.
2.  **Resultado:** Se a maioria dos vizinhos mais próximos for de uma determinada classe (por exemplo, laranjas), o objeto desconhecido provavelmente pertencerá a essa classe.

## Extração de Características (Feature Extraction)

Para utilizar o KNN, é necessário primeiro converter o item que está sendo analisado (como uma fruta ou um usuário) em uma lista de números que podem ser comparados.

*   **Características:** Essas listas de números são chamadas de **características**. No exemplo de classificação de frutas, **o tamanho e a cor** são as características comparadas.
*   **Representação em Coordenadas:** A extração de características permite **converter cada item em um conjunto de coordenadas**, que podem ser plotadas em um gráfico.
*   **Medida de Similaridade:** A distância entre dois pontos (itens) é calculada usando o **teorema de Pitágoras** (fórmula da distância). Essa fórmula é **flexível** e pode ser usada em múltiplas dimensões (por exemplo, cinco dimensões) para encontrar a distância. A distância calculada informa a **similaridade** entre esses conjuntos.
*   **Importância das Características:** É fundamental **escolher as características certas**. As características devem ser **diretamente correlacionadas** ao que se tenta recomendar ou prever, e devem ser **imparciais**.

## Regressão

A regressão é o uso do KNN para **adivinhar uma resposta numérica**.

*   **Exemplos:** Prever a nota que um usuário dará a um filme ou prever quantos pães uma padaria venderá em um dia.
*   **Cálculo da Resposta:** A resposta numérica é geralmente determinada pela **média das respostas** dos K-vizinhos mais próximos.

## Aplicações Práticas

O KNN é aplicável a diversos cenários:

1.  **Sistemas de Recomendações (Netflix):** Usuários são agrupados por similaridade de gostos, utilizando suas avaliações como características. Filmes são recomendados a um usuário com base no que seus **vizinhos** (pessoas classificadas com gostos parecidos) gostaram.
2.  **OCR (Reconhecimento Óptico de Caracteres):** O algoritmo pode ser usado para reconhecer caracteres medindo linhas, pontos e curvas (extraindo características) e comparando-as com vizinhos próximos.
3.  **Treinamento:** O processo de percorrer imagens e extrair características, como é feito no OCR, é chamado de **treinamento**. A maioria dos algoritmos de aprendizado de máquina possui uma etapa de treinamento.
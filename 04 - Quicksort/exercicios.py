#Exercício 4.1 - Escreva o código para função soma que recebe uma lista e a soma

def soma(lista):
    total = 0
    for i in lista:
        total += i
    return total

print(soma([1, 2, 4, 6])) #13
    

#Exercício 4.2 - Escreva uma função recursiva que conte o núimero de itens em uma lista

def conte(lista):
    cont=0
    for i in lista:
        cont += 1
    return cont

print(conte([2,56,75,32,1,2,10])) #7

#Exercício 4.3 - Encontre o maior elemento em uma lista

def encontra_maior(lista):
    #Caso-Base: A lista tem apenas um elemento.
    if len(lista) == 1:
        return lista[0]
    
    #Divide a lista em duas metades.
    meio = len(lista) // 2
    lista_esquerda = lista[:meio]
    lista_direita = lista[meio:]

    #Caso-recursivo para encontrar o maior em cada metade
    maior_esquerda = encontra_maior(lista_esquerda)
    maior_direita = encontra_maior(lista_direita)
    
    #Compara os maiores de cada metade e retorna o maior de todos
    if maior_esquerda > maior_direita:
        return maior_esquerda
    else:
        return maior_direita
lista_exemplo = [12, 5, 8, 20, 3, 15, 7,89, 90, 102]
maior_valor = encontra_maior(lista_exemplo)
print(f"O maior elemento da lista dada é {maior_valor}")

#Exercício 4.4 - Determine o caso-base e o caso recursivo pada o algoritmo da pesquisa binária
"""
Caso-base: quando a função para por ter encontrado o elemento da busca ou quando o elemento não está presente
É quando a recursão para por não precisar mais chamar a si mesma

Caso-recursivo: é, na pesquisa binária, o loop while que subdivide o problema em problemas menores na medida
em que move os ponteiros `maior` e `menor' para posições diferentes a cada recursão de acordo com o `chute`.

O chute foi muito alto: Se o elemento do meio for maior que o item procurado, a função chama a si mesma novamente, mas com uma nova lista, que é a metade esquerda da lista original.
O chute foi muito baixo: Se o elemento do meio for menor que o item procurado, a função chama a si mesma novamente, mas com uma nova lista, que é a metade direita da lista original.
"""

#Exercício 4.5 - Quanto tempo levaria (em BigO) para comletar cada uma das operações:

#Imprimir o valor de cada elemento em um array: O(n)
"""
Para imprimir cada elemento de um array, você precisa percorrer o array do início ao fim. Se o array tem n elementos, você realizará n operações de impressão. 
Portanto, o tempo de execução é diretamente proporcional ao número de elementos, resultando em uma complexidade de tempo linear.
"""
#Duplicar o valor de cada elemento em um array: O(n)
"""
Assim como na impressão, para duplicar o valor de cada elemento, você precisa iterar sobre o array completo. 
Para cada um dos n elementos, você realizará uma operação de multiplicação. Por isso, a complexidade de tempo é novamente linear.
"""
#Duplicar o valor apenas do primeiro elemento do array: O(1)
"""
Neste caso, a operação é realizada apenas no primeiro elemento do array, independentemente do tamanho total do array. 
Se o array tem 10 ou 10 milhões de elementos, a operação será sempre a mesma: acessar o primeiro elemento e duplicar seu valor. 
O tempo de execução é constante e não depende do tamanho da entrada, por isso usamos a notação O(1)
"""
#Criar uma tabela de multiplicação com todos os elementos do array: O(n²)
"""
Para criar uma tabela de multiplicação com todos os elementos do array, você precisa pegar cada elemento e multiplicá-lo por todos os outros elementos do array (incluindo ele mesmo). 
Isso significa que, para cada elemento do array (n), você terá que percorrer o array inteiro novamente (n). Um loop aninhado i * j, portanto O(n²)
"""
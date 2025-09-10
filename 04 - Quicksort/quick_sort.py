# [2, 5, 1, 3, 10, 9, 78, 60, 102, 99, 73, 105, 123, 204]
# [] => []
# [i] => [i]
# [i, j] => [i, j] se i<=j ou [j, i] se j < i

# BigO Log (n^2) 
def quicksort(lista):
    if len(lista) < 2:
        return lista
    
    #Definição do pivô e divisão da lista em listas menores
    pivo = lista.pop(0)
    menores = [i for i in lista if i <= pivo]
    maiores = [i for i in lista if i> pivo]

    # Ordenação da lista menor e maior recursivamente
    return quicksort(menores) + [pivo] + quicksort(maiores)

print(quicksort([1, -2, 3, 5, 9, -10, 60, 73, 78, 99, 102, 105, 123, 204]))
# [1, -2, 3, 5, 9, -10, 60, 73, 78, 99, 102, 105, 123, 204]

"""
A complexidade do algoritmo vai depender da escolha do pivô
Se estamos escolhendo sempre o pivô à esquerda (pop.lista(0)), sempre
estaremos iterando sobre o número completo de elementos da lista. Assim,
BigO -> Log(n^2)

Se quisermos otimizar, podemos escolher o pivô como sendo o elemento
do meio da lista (a mediana). Dessa forma, a complexidade seria n*log(n)

meio = len(lista) // 2

"""
# BigO n*Log(n) - mais eficiente, menos complexo
def quicksort(lista):
    if len(lista) < 2:
        return lista
    
    #Definição do pivô mediano
    meio = len(lista) // 2
    pivo = lista.pop(meio)

    menores = [i for i in lista if i <= pivo]
    maiores = [i for i in lista if i> pivo]

    # Ordenação da lista menor e maior recursivamente
    return quicksort(menores) + [pivo] + quicksort(maiores)

print(quicksort([1, -2, 3, 5, 9, -10, 60, 73, 78, 99, 102, 105, 123, 204]))
# [1, -2, 3, 5, 9, -10, 60, 73, 78, 99, 102, 105, 123, 204]



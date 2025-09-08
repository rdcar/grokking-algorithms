#Encontra o menor valor de uma lista
def encontreMenor(lista):
    menor = lista[0]
    menor_indice = 0
    for i in range(1, len(lista)):
        if lista[i] < menor:
            menor_indice = i
            menor = lista[i]
    return menor_indice

#Ordenar a lista de forma crescente
def selection_sort(lista):
    nova_lista=[]
    for i in range(len(lista)):
        menor = encontreMenor(lista)
        nova_lista.append(lista.pop(menor))
    return nova_lista

print(selection_sort([5, 3, 6, 2, 10])) #-> [2, 3, 5, 6, 10]
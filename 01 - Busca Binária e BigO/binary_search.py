def pesquisa_binaria(lista, item):
    """Localiza um item em uma lista ordenada

    Args:
        lista (_list_)
        item (_object_)

    Returns:
        _object_: posição do item encontrado
        _None_ : se o item não for localizado na lista
    """
    #Setup dos ponteiros alto e baixo definindo uma zona de pesquisa
    baixo = 0
    alto = len(lista) - 1
    #Enquanto não reduzir a um único elemento, faça...
    while baixo <= alto:
        #ache o elemento central
        meio = (baixo + alto) // 2 #meio é a posição do item
        chute = lista[meio]
        #Posição do item encontrada
        if chute == item:
            return meio
        #chute foi muito baixo
        if chute > item:
            alto = meio - 1
        #chute foi muito alto
        else:
            baixo = meio + 1
        #A posição do item não foi encontrada
    return None #quando o item não existe na lista

minha_lista=[1, 3, 5, 7, 9] #precisa estar ordenada
print(pesquisa_binaria(minha_lista, 7)) # -> 3

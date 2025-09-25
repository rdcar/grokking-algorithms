#Pesquisa em largura (BFS - Breadth-frist search)
from collections import deque

#definindo regra para busca
def pessoa_e_vendedor(nome):
    return nome[-1] == "m"

#grafo
grafo = {}
grafo["você"] = ["alice", "bob", "claire"]
grafo["bob"] = ["anuj", "peggy"]
grafo["alice"] = ["peggy"]
grafo["claire"] = ["thom", "jonny"]
grafo["anuj"] = []
grafo["peggy"] = []
grafo["thom"] = []
grafo["jonny"] = []

# Meu algoritmo (mais eficiente pois adiciona a pessoa a um set imediatamente depois de ser verificada se é um vendedor e, 
# em seguida, adiciona seus vizinhos apenas se já não estiverem sido adicionados ao set previamente)

def pesquisa1(nome):
    fila_de_pesquisa = deque()
    fila_de_pesquisa += grafo[nome]
    verificadas = set() 
    
    while fila_de_pesquisa:
        pessoa = fila_de_pesquisa.popleft()
        
        if pessoa_e_vendedor(pessoa):
            print(pessoa + " é um vendedor de manga!")
            return True
        else:
            # Marca a pessoa como verificada IMEDIATAMENTE
            verificadas.add(pessoa)

            # Adiciona os vizinhos da pessoa à fila, se eles ainda não foram visitados
            for vizinho in grafo[pessoa]:
                if vizinho not in verificadas:
                    fila_de_pesquisa.append(vizinho)
    
    return False

pesquisa1("você")


# Algoritmo do autor (pode ocorrer a adição de vizinhos duplicados à lista de pesquisa. Além disso, usa uma LISTA 
# e não um set para o conjunto de pessoas já verificadas)

def pesquisa2(nome):
    fila_de_pesquisa = deque()
    fila_de_pesquisa += grafo[nome]
    verificadas = []

    while fila_de_pesquisa:
        pessoa = fila_de_pesquisa.popleft()

        if not pessoa in verificadas:
            if pessoa_e_vendedor(pessoa):
                print(pessoa + " é um vendedor de manga!")
                return True
            else:
                fila_de_pesquisa += grafo[pessoa] 
                verificadas.append(pessoa)

pesquisa2("você")

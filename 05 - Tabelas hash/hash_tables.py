votaram = {} #dicionário vazio para armazenar pares de chave-valor (dict são tabelas hash built-in no python)

def verifica_eleitor(nome):
    if votaram.get(nome): #retorna True caso haja valor para chave "nome" inserida
        print("Já votou! Mande embora!") 
    else: 
        votaram[nome] = True # Atribui valor True para a chave "nome" inserida, caindo no if na proxima inserção
        print("Ainda não votou. Pode votar!")
verifica_eleitor("tom")
verifica_eleitor("mike") 
verifica_eleitor("mike") #mike já foi inserido na chamada anterior

#Caching
cache = {}

def pega_pagina(url):
    if cache.get(url):
        return cache[url]
    else:
        dados = pega_dados_do_servidor(url)
        cache[url] = dados
        return dados
    
#Exercícios
"""
5.5
D e C

5.6
B e D

5.7
D, B e C """

#Problema: contagem regressiva

#Definição do caso recursivo
def contagemregressiva(x):
    print(x)
    if x >= 0:
        contagemregressiva(x-1)
    else: #Definição do caso base para evitar stack overflow
        return

contagemregressiva(10) #10 9 8 7 6 5 4 3 2 1 0 -1

#Recursividade em problemas fatoriais
def fatorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * fatorial(n-1)
    
print(fatorial(6)) #6! = 720

# Recursividade no problema sequência de Fibonacci
def fibonacci(z):
    # Casos bases
    if z == 0:
        return 0
    if z == 1:
        return 1
    # Caso recursivo
    else:
        return fibonacci(z-1) + fibonacci(z-2)

numero_fib = fibonacci(6)

print(f"O 7º número da sequência de Fibonacci é: {numero_fib}")

"""
Para imprimir a sequência de Fibonacci até um número específico, a abordagem recursiva que usamos antes não é a mais eficiente. 
A recursividade é ótima para calcular um único valor, mas para gerar uma série de valores, um loop (iteração) é a melhor escolha.
Vamos usar um loop while para fazer isso.
"""
def fibonacci_ate_limite(limite):
    # Condição especial para o caso do limite ser 0
    if limite <= 0:
        print("Nenhum número na sequência para exibir.")
        return

    # Inicia com os dois primeiros números da sequência
    a, b = 0, 1

    # Imprime o primeiro número (0) se o limite for maior que 0
    print(a, end=" ")

    # Loop para gerar e imprimir os próximos números
    while b <= limite:
        print(b, end=" ")
        # Atualiza os valores: o 'b' se torna o novo 'a' e a soma se torna o novo 'b'
        a, b = b, a+b

# Exemplo de uso: imprimir a sequência até o número 200
fibonacci_ate_limite(200)

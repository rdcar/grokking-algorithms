 # Recursão

- O conceito fundamental é que a função recursiva se chama repetidamente até atingir um caso base, que é uma condição de parada que não requer mais chamadas para a função. Sem esse caso base, a função se chamaria infinitamente, causando um loop infinito.
- *Caso-recursivo:* é quando a função chama a si mesma.
- *Caso-base:* é quando a função não chama a si mesma novamente de forma que o programa não se torna um loop infinito.

*Exemplo do livro: Contagem regressiva:*  
Em vez de usar um loop (while ou for), você pode criar uma função contagemRegressiva(i) que imprime o número i e depois se chama novamente com i-1. O caso base seria quando i é igual ou menor que zero, interrompendo as chamadas.  
``` 
função contagemRegressiva(i):
      imprima i
      se i <= 0:
        return
      senão:
        contagemRegressiva(i-1)
```
No exemplo, a função continua a se chamar com valores cada vez menores até chegar a zero, quando o return é ativado e a cadeia de chamadas é desfeita, finalizando a execução.  
A recursão é uma técnica elegante e poderosa, mas é **importante garantir que haja um caso base claro para evitar erros e loops infinitos**. Ela é frequentemente usada para resolver problemas que envolvem estruturas de dados como árvores e grafos, ou para algoritmos como o *Quicksort*. 
- Não há nenhum benefício quanto ao desempenho ao utilizar a recursão. Na verdade, os loops algumas vezes são melhor para o desempenho de um programa.

## Pilha
- Forma com a qual o processador/OS empilha tarefas sequenciais que precisam ser feitas durante a chamada de uma função
- Quando você INSERE um item, ele é colocado no TOPO da pilha
- Quando você LÊ um item, lê apenas o item do TOPO da pilha e ele é RETIRADO da lista
- Segue o conceito LIFO (Last-In First-Out).
- *Push*: adicione um novo item ao topo
- *Pop*: remova o item do topo e leia-o

## Pilha de Chamada na Recursão  

Na recursão, essa estrutura é especialmente importante. Cada vez que uma função recursiva se chama, uma nova "cópia" da função é empurrada para o topo da pilha, com seus próprios argumentos e variáveis locais.  

Vamos revisitar o exemplo da contagem regressiva:
- Você chama a função contagemRegressiva(3). A função contagemRegressiva(3) é colocada na pilha.
- Dentro de contagemRegressiva(3), a função contagemRegressiva(2) é chamada. A função contagemRegressiva(2) é colocada em cima de contagemRegressiva(3) na pilha.
- O mesmo acontece com contagemRegressiva(1). Ela é colocada no topo.
- Por fim, contagemRegressiva(0) é chamada e adicionada ao topo da pilha.

* Neste ponto, a pilha de chamada se parece com:

````
contagemRegressiva(0)
contagemRegressiva(1)
contagemRegressiva(2)
contagemRegressiva(3)
````
* Dizemos, assim que essa pilha está em um estado "parcialmente completo".

Quando a função ``contagemRegressiva(0)`` chega ao caso base, ela retorna. Isso a remove do topo da pilha. Em seguida, a execução volta para a função ``contagemRegressiva(1)``, que estava logo abaixo. Quando ela termina, é removida também, e assim por diante, até que a pilha esteja vazia e o programa termine.  

## O perigo do "Stack Overflow"
- Se você não tiver um caso base claro em uma função recursiva, a função continuará a se chamar indefinidamente. A pilha de chamada continuará a crescer, adicionando uma nova "cópia" da função a cada chamada, até que todo o espaço de memória alocado para a pilha seja consumido. Quando isso acontece, o programa falha e você recebe um erro de "Stack Overflow" (literalmente, "estouro da pilha"). Por isso, o caso base é vital para garantir que a pilha de chamada esvazie corretamente e que a recursão termine de forma segura. 

* Desvantagem: tamanho em memória. A pilha pode ficar muito grande e ocupar muita memória
  * Reescrever seu código utilizando loops
  * Utilizar tail recursivo

## Limitações da Recursão
````
def fibonacci_recursivo(n):
    # Caso Base 1
    if n == 0:
        return 0
    # Caso Base 2
    if n == 1:
        return 1
    # Passo Recursivo
    else:
        # A função chama a si mesma duas vezes, para os dois números anteriores
        return fibonacci_recursivo(n - 1) + fibonacci_recursivo(n - 2)

# Exemplo de uso: encontrar o 6º número da sequência (lembre-se que o índice começa em 0)
numero_fib = fibonacci_recursivo(6)
print(f"O 6º número da sequência de Fibonacci é: {numero_fib}")
````

Embora a recursividade seja elegante, para a sequência de Fibonacci ela pode ser ineficiente para números muito grandes. Isso porque a função recalcula os mesmos valores várias vezes (por exemplo, fibonacci_recursivo(2) é calculado várias vezes no exemplo acima). Para casos de uso mais sérios, o ideal é usar um método iterativo (com loops) ou a programação dinâmica, que armazena os valores já calculados para evitar retrabalho.

No entanto, para aprender o conceito, a abordagem recursiva é excelente! Espero que tenha ajudado a entender.
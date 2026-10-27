Introdução

A análise de algoritmos não depende exclusivamente de execução em máquina. Em muitos contextos, é necessário estimar custos manualmente para compreender comportamento e eficiência. Neste exercício, você analisará passo a passo a execução da busca linear em um conjunto pequeno de dados, reforçando o entendimento das etapas da operação e do custo associado.

Tarefa

Considere o array ordenado [2, 4, 6, 8, 10, 12, 13].
Simule manualmente a execução da busca linear pelo valor 8.
Conte o número de comparações realizadas.
Justifique o resultado obtido.
Relacione o número de passos ao tamanho do array.
 
*** 
array ordenado -> [2, 4, 6, 8, 10, 12, 13]
target = 8

usando busca linear:
Comparo 2 com 8 (diferente)
Comparo 4 com 8 (diferente)
Comparo 6 com 8 (diferente)
Comparo 8 com 8 (encontrei)

Precisei de 4 comparações para encontrar o target(idx = 3)

Relacione o número de passos ao tamanho do array -> No pior caso, a busca linear precisa percorrer o array inteiro, ou seja, O(n), porque o número de comparações cresce proporcionalmente ao tamanho do meu array
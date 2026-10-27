Introdução

Antes de codificar algoritmos, é fundamental saber abstrair e modelar soluções independentemente da linguagem. Muitos algoritmos clássicos de ordenação surgem de processos manuais intuitivos. Este exercício propõe a construção de um algoritmo conceitual sob fortes restrições operacionais, simulando limitações reais de acesso e movimentação de dados. O objetivo é avaliar sua capacidade de decompor o problema, definir passos claros e reconhecer o padrão algorítmico subjacente à solução.

Tarefa

Elabore um algoritmo passo a passo para ordenar as 13 cartas de espadas conforme as restrições apresentadas.
Descreva claramente o estado inicial, as operações permitidas e o estado final.
Identifique qual algoritmo de ordenação clássico o procedimento mais se aproxima.
Justifique sua resposta com base nas operações realizadas.
Descreva qualitativamente o custo do algoritmo em termos de Big O.

***
Estado inicial: 13 cartas de espadas embaralhadas, do Ás ao Rei, sem nenhuma ordem definida

Operações: Pegar uma carta, comparar seu valor com as anteriores e deslocar as cartas maiores para a direita, abrindo espaço para inserir a carta na posição correta

Funcionamento:

1. Pegar a primeira carta e usar como base para a ordenação
2. Pegar a segunda carta e comparar com a primeira
3. Se a segunda carta for menor, eu coloco antes da primeira, se for maior, eu coloco depois
4. Pegar a próxima carta e comparar com as anteriores, da direita para a esquerda
5. Deslocar as cartas maiores para a direita para abrir espaço e inserir a carta na posição correta
6. Repetir esse ciclo até organizar as cartas

Resultado: Todas as cartas estarão organizadas em ordem crescente, do Ás ao Rei

Algoritmo clássico: Insertion Sort, já que cada carta é inserida na posição correta dentro de um grupo que já está ordenado

Complexidade: O(n²) no caso médio e no pior caso, porque cada carta pode precisar ser comparada com várias outras. No melhor caso, quando as cartas já estão ordenadas, a complexidade é O(n)

OBS: Esse algoritmo é parecido com a forma como organizamos cartas na mão. Pegamos uma carta, depois outra, e vamos encaixando cada uma na posição correta em relação às que já estão organizadas
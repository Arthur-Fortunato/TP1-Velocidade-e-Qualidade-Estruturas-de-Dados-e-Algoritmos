Introdução

Este exercício explora crescimento exponencial e sua relação direta com análise de complexidade algorítmica. O clássico problema do tabuleiro de xadrez e grãos de arroz é utilizado para demonstrar como funções aparentemente simples podem crescer rapidamente, tornando soluções ingênuas inviáveis. O objetivo é exercitar a modelagem correta do problema, a implementação em Python e a análise do custo computacional da abordagem adotada.

Tarefa

Considere as seguintes premissas obrigatórias:

O tabuleiro possui 64 quadrados, numerados de 1 a 64.
No quadrado 1, há 1 grão de arroz.
Em cada quadrado seguinte, a quantidade de grãos dobra em relação ao quadrado anterior.
A quantidade de grãos em um quadrado é dada por:
grãos = $2^{(n-1)}$, onde n é o índice do quadrado.
A entrada da função representa uma quantidade alvo de grãos, e não o número do quadrado.
Com base nessas premissas:

Implemente uma função em Python que receba como parâmetro um número inteiro positivo qtd_graos.
Calcule qual é o menor índice de quadrado do tabuleiro em que a quantidade de grãos acumulada no próprio quadrado é maior ou igual a qtd_graos.
Caso a quantidade informada ultrapasse o total de grãos do tabuleiro (64 quadrados), a função deve retornar uma mensagem indicando que o valor excede o limite do tabuleiro.
Teste a função com, no mínimo:
valores pequenos (ex: 1, 2, 4, 8);
valores intermediários (ex: 1.000, 1.000.000);
um valor maior que o total de grãos possíveis no tabuleiro.
Descreva a complexidade temporal da solução implementada utilizando Notação Big O, justificando sua resposta com base no número de iterações realizadas.
Observações

Não utilize fórmulas matemáticas prontas para calcular diretamente o índice do quadrado.
A solução deve ser baseada em iteração ou recursão, permitindo a análise explícita do custo computacional.
A clareza da implementação e da análise de complexidade faz parte da avaliação.

***
Implementei uma função que recebe a quantidade de grãos como parâmetro e percorre os 64 quadrados do tabuleiro de xadrez

Começo com 1 grão no primeiro quadrado, a cada iteração, vajo se a quantidade de grãos da casa atual é maior ou igual ao valor procurado

Caso não seja, dobro a quantidade de grãos e continuo

Se percorrer todos os 64 quadrados sem encontrar uma quantidade suficiente, a função retorna uma mensagem informando que o valor excede o limite

A quantidade de grãos cresce exponencialmente, mas a complexidade temporal da implementação é O(1), porque o tabuleiro possui um limite fixo de 64 quadrados, ou seja, a função faz no máximo 64 iterações
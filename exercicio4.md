Introdução

A busca binária explora a organização dos dados para reduzir significativamente o espaço de busca. A análise manual desse algoritmo é fundamental para compreender por que ele é mais eficiente do que a busca linear em arrays ordenados. Neste exercício, você realizará essa análise de forma detalhada.

Tarefa

Utilize o mesmo array do Exercício 3.
Simule manualmente a execução da busca binária pelo valor 8.
Conte o número de comparações realizadas.
Compare o resultado com a busca linear.
Relacione a diferença observada à notação Big O.

***
array ordenado -> [2, 4, 6, 8, 10, 12, 13]
target = 8

A busca binária começa no meio do array, então, se tem 7 elementos(n-1, logo, de 0 até 6), começa pelo índice 3, o número que está no índice 3 é justamente o target, então, apenas 1 comparação é feita, diferente da linear que precisou de 4 comparações

Relacione a diferença observada à notação Big O -> A busca linear tem complexidade O(n) no pior caso, pois pode precisar percorrer todos os elementos. A busca binária tem complexidade O(log n) no pior caso, porque reduz o espaço de busca pela metade a cada comparação
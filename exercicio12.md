Introdução

Pequenas otimizações podem gerar ganhos relevantes. Neste exercício, você aplicará uma otimização clássica ao Bubble Sort e avaliará seu impacto.

Tarefa

Modifique o Bubble Sort para interromper quando não houver trocas.
Execute o algoritmo com os mesmos dados do Exercício 11.
Compare os resultados.
Analise o ganho obtido.
Relacione com Big O.

***
Na comparação dos exercícios 11 e 12, o Bubble Sort(12) realizou menos comparações em alguns testes, mas manteve a mesma quantidade de trocas. O ganho acontece porque o algoritmo interrompe a execução quando uma passagem termina sem nenhuma troca, evitando comparações desnecessárias

Com uma lista ordenada de 100 elementos, as comparações caíram de 4.950 para 99. Em relação ao Big O, o melhor caso muda de O(n²) para O(n), enquanto o caso médio e o pior caso continuam O(n²)
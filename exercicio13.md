Introdução

Na prática, a escolha entre busca linear e busca binária depende de pré-requisitos, custo de preparação dos dados e perfil de uso (quantidade de buscas realizadas). Neste exercício, você vai implementar, instrumentar e testar as duas estratégias, comparando o custo por meio de contagem de operações (comparações e iterações), e não por tempo de execução em segundos. O objetivo é tornar a comparação objetiva e reproduzível, usando Notação Big O para interpretar os resultados.

Premissas obrigatórias

Você receberá listas de números inteiros com tamanho N.
A busca binária só pode ser aplicada corretamente em lista ordenada.
Quando a lista não estiver ordenada e você quiser usar busca binária, você deve ordená-la antes usando Bubble Sort (já visto nas subcompetências avaliadas).
Você deve comparar os algoritmos pelo número de comparações realizadas.
Faça a análise considerando o pior caso e também observe empiricamente os casos testados.
Tarefa

Parte A — Implementação instrumentada

Implemente a função linear_search_count(arr, target) que:
retorna uma tupla (index, comparisons)
index é a posição do elemento encontrado ou -1 se não encontrado
comparisons é o número de comparações arr[i] == target executadas

Implemente a função binary_search_count(sorted_arr, target) que:
retorna uma tupla (index, comparisons)
assume que o array já está ordenado
conta comparações de chave (comparações entre target e o valor do meio)

Implemente a função bubble_sort_count(arr) que:
ordena uma cópia da lista (não altere a original)
retorna (sorted_arr, comparisons) onde comparisons conta comparações entre pares adjacentes


Parte B — Casos de teste controlados

Crie 3 listas com N = 31:
arr_sorted: lista ordenada crescente
arr_reverse: lista ordenada decrescente
arr_random: lista com os mesmos elementos, mas embaralhada (use random.seed(42))

Para cada uma das 3 listas, execute as buscas para três alvos:
target_first = primeiro elemento da lista
target_middle = elemento do meio (posição N//2)
target_absent = um valor que você garanta que não existe na lista (ex: -1)

Em cada execução, registre:
Comparações da busca linear
Comparações da busca binária (quando aplicável)
Se a lista não estiver ordenada, registre também:
Comparações do Bubble Sort
Comparações totais “Bubble Sort + Busca Binária”


Parte C — Interpretação e Big O

Escreva uma conclusão técnica em Markdown respondendo:
Quais são os pré-requisitos de cada busca?
Qual é o Big O da busca linear e da busca binária?
Em listas não ordenadas, quando faz sentido pagar o custo do Bubble Sort para usar busca binária?
Relacione suas conclusões com os resultados (comparações) observados.

***
Parte **C** Aqui.

1. Pré-requisitos

A busca linear funciona tanto em listas ordenadas quanto desordenadas. A busca binária precisa que a lista esteja ordenada para funcionar direito

2. Complexidade Big O

A busca linear possui complexidade O(n) no pior caso, pois pode precisar percorrer todos os elementos. A busca binária possui O(log n), porque elimina metade da região de busca a cada comparação

3. Quando vale a pena ordenar?

Em uma lista desordenada, usar Bubble Sort antes da busca binária pode não compensar quando fazemos poucas buscas, porque a ordenação custa O(n²), porém,  quando precisamos realizar muitas buscas na mesma lista, podemos ordenar uma única vez e aproveitar a lista ordenada em outras buscas

4. Resultados observados

Nos testes, a busca linear fez 1, 16 e 31 comparações, dependendo da posição do alvo. A busca binária precisou de no máximo 5 comparações, o que mostra uma boa eficiência com listas ordenadas. Porém, nas desordenadas, o Bubble Sort fez 465 comparações antes da busca binária, fazendo o custo total chegar a até 470 comparações

Esses resultados mostram que a busca binária é mais eficiente na busca, mas, quando precisamos ordenar a lista antes, o custo pode não compensar para poucas buscas
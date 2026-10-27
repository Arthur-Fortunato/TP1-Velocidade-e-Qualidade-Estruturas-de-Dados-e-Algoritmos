Introdução

Identificar e eliminar ineficiências algorítmicas é uma competência central no desenvolvimento de software de qualidade. Algoritmos com complexidade quadrática rapidamente se tornam inviáveis em grandes volumes de dados. Neste exercício, você analisará um código real, identificará seu gargalo e o reescreverá de forma mais eficiente, preservando a funcionalidade.

def maior_unico(arr):
    """
    Retorna o maior número que aparece exatamente uma vez no array.
    """

    maior = None  # Guardará o maior número único encontrado

    # Percorre cada elemento do array
    for i in range(len(arr)):
        atual = arr[i]
        contador = 0  # Contará quantas vezes 'atual' aparece

        # Compara o elemento atual com todos os outros
        for j in range(len(arr)):
            if arr[j] == atual:
                contador += 1

        # Se apareceu exatamente uma vez, é um candidato
        if contador == 1:
            # Atualiza o maior único encontrado
            if (maior is None) or (atual > maior):
                maior = atual

    return maior


Tarefa

Analise a função fornecida para encontrar o maior número único.
Identifique o motivo de sua complexidade O(N²).
Reescreva a função para que opere em O(N).
Explique a estratégia utilizada para reduzir a complexidade.
Justifique a nova complexidade usando Big O.

***
O código original tem a complexidade O(n²) porque usa dois laços **for** aninhados. Para cada elemento do array, o segundo laço percorre todos os elementos de novo para contar quantas vezes aquele número aparece.

Para fazer uma otimização, usei um dicionário que armazena a quantidade de aparições de cada número.

No primeiro **for**, eu percorro o array e conto quantas vezes cada número aparece. No segundo, eu percorro o dicionário e vejo quais números aparecem só uma vez, guardando o maior deles.

Assim, não preciso percorrer o array inteiro para cada número.

A complexidade sai de O(n²) para O(n), porque os dois laços são executados separadamente e as operações de consulta e atualização do dicionário possuem custo O(1) normalmente.
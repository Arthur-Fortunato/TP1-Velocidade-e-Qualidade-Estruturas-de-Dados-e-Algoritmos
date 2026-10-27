Introdução

Código eficiente não é apenas código rápido, mas também código legível, organizado e sustentável. Em ambientes profissionais, algoritmos corretos frequentemente precisam ser mantidos, revisados e evoluídos por outras pessoas. Este exercício avalia a capacidade de melhorar a qualidade estrutural do código sem alterar seu comportamento ou sua complexidade assintótica.

Código fornecido para refatoração

Utilize o código abaixo como ponto de partida. Não altere a lógica do algoritmo nem os resultados produzidos.

def f(a, t):
    c = 0
    i = 0
    j = len(a) - 1
    r = -1
    while i <= j:
        m = (i + j) // 2
        c = c + 1
        if a[m] == t:
            r = m
            break
        c = c + 1
        if t < a[m]:
            j = m - 1
        else:
            i = m + 1
    return r, c

def h(arr):
    b = arr[:]
    n = len(b)
    k = 0
    for last in range(n - 1, 0, -1):
        for p in range(last):
            k += 1
            if b[p] > b[p + 1]:
                tmp = b[p]
                b[p] = b[p + 1]
                b[p + 1] = tmp
    return b, k

Tarefa

Refatore o código fornecido, preservando exatamente o comportamento.
Melhore nomes de funções, variáveis e parâmetros.
Organize o código para tornar a leitura e manutenção mais claras.
Adicione comentários técnicos objetivos.
Mantenha a complexidade assintótica dos algoritmos (busca binária e Bubble Sort).
Crie um pequeno teste que demonstre que a versão refatorada produz o mesmo resultado da original.
Observações

Não utilize funções prontas como sorted, .sort() ou bibliotecas externas.
Não altere contadores ou critérios de parada.
O foco é qualidade de código, não otimização algorítmica.
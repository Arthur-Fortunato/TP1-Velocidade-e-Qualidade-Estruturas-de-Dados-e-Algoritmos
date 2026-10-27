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

def busca_binaria(array_ordenado, alvo):
    comparacoes = 0
    esquerdo = 0
    direito = len(array_ordenado) - 1
    indice_encontrado = -1
    while esquerdo <= direito:
        meio = (esquerdo + direito) // 2
        # comparação de igualdade com o alvo
        comparacoes += 1
        if array_ordenado[meio] == alvo:
            indice_encontrado = meio
            break

        # comparação para decidir o lado da busca
        comparacoes += 1
        if alvo < array_ordenado[meio]:
            direito = meio - 1
        else:
            esquerdo = meio + 1
    return indice_encontrado, comparacoes


def bubble_sort(array):
    array_ordenado = array[:]
    tamanho = len(array_ordenado)
    comparacoes = 0
    for ultimo_indice in range(tamanho - 1, 0, -1):
        for indice in range(ultimo_indice):
            # cada comparação entre elementos vizinhos
            comparacoes += 1
            if array_ordenado[indice] > array_ordenado[indice + 1]:
                # Troca os elementos sem alterar a lista original
                temporario = array_ordenado[indice]
                array_ordenado[indice] = array_ordenado[indice + 1]
                array_ordenado[indice + 1] = temporario

    return array_ordenado, comparacoes


listas_teste = [
    [5, 2, 9, 1, 7],
    [1, 2, 3, 4, 5],
    [9, 7, 5, 3, 1],
    [4, 2, 4, 1, 2],
]

for array in listas_teste:
    resultado_original = h(array)
    resultado_refatorado = bubble_sort(array)

    print(f"Bubble Sort: {resultado_original == resultado_refatorado}")

    array_ordenado = resultado_original[0]

    for alvo in [1, 5, 9, -1]:
        resultado_original_busca = f(array_ordenado, alvo)
        resultado_refatorado_busca = busca_binaria(array_ordenado, alvo)

        print(f"Busca binária: {resultado_original_busca == resultado_refatorado_busca}")

    print()
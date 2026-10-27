def bubble_sort_string(array):
    tamanho = len(array)
    for passagem in range(tamanho - 1):
        for indice in range(tamanho - 1 - passagem):
            if array[indice] > array[indice + 1]:
                array[indice], array[indice + 1] = array[indice + 1], array[indice]
    return array


testes = [
    ["banana", "abacaxi", "uva", "manga"],
    ["abacaxi", "banana", "manga", "uva"],
    ["uva", "manga", "banana", "abacaxi"],
    ["casa", "carro", "cachorro", "caderno"],
    ["banana", "uva", "banana", "manga"],
]

for array in testes:
    resultado_bubble = bubble_sort_string(array.copy())
    resultado_esperado = sorted(array)
    print(f"Original: {array}")
    print(f"Ordenado: {resultado_bubble}")
    print(f"Correto: {resultado_bubble == resultado_esperado}\n")
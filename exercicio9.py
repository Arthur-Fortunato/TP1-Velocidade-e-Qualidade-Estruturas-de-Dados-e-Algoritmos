def bubble_sort(array):
    tamanho = len(array)
    for passagem in range(tamanho - 1):
        for indice in range(tamanho - 1 - passagem):
            if array[indice] > array[indice + 1]:
                array[indice], array[indice + 1] = array[indice + 1], array[indice]
    return array

testes = [
    [5, 2, 9, 1, 7],     
    [1, 2, 3, 4, 5],     
    [9, 7, 5, 3, 1],     
    [4, 2, 4, 1, 2]
]

for array in testes:
    resultado_bubble = bubble_sort(array.copy())
    resultado_esperado = sorted(array)
    print(f"Original: {array}")
    print(f"Ordenado: {resultado_bubble}")
    print(f"Correto: {resultado_bubble == resultado_esperado}\n")
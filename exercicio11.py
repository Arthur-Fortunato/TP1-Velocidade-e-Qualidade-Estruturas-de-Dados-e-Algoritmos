import random

random.seed(42)

testes = [random.sample(range(1, 1001), tamanho) for tamanho in [10, 25, 50, 75, 100]]

def bubble_sort(array):
    tamanho = len(array)
    comparacoes = 0
    trocas = 0
    for passagem in range(tamanho - 1):
        for indice in range(tamanho - 1 - passagem):
            comparacoes += 1
            if array[indice] > array[indice + 1]:
                array[indice], array[indice + 1] = array[indice + 1], array[indice]
                trocas += 1
    return array, comparacoes, trocas



for array in testes:
    resultado, comparacoes, trocas = bubble_sort(array.copy())
    print(f"Tamanho: {len(array)}")
    print(f"Comparações: {comparacoes}")
    print(f"Trocas: {trocas}")
    print(f"Correto: {resultado == sorted(array)}")
    print()


array = list(range(1, 101))
resultado, comparacoes, trocas = bubble_sort(array.copy())
print(f"Comparações: {comparacoes}")
print(f"Trocas: {trocas}")
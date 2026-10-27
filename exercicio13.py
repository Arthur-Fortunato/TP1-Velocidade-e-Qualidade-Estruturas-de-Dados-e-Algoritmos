# A
def linear_search_count(arr, target):
    comparisons = 0
    for indice in range(len(arr)):
        comparisons += 1
        if arr[indice] == target:
            return indice, comparisons
    return -1, comparisons


def binary_search_count(sorted_arr, target):
    esquerdo = 0
    direito = len(sorted_arr) - 1
    comparisons = 0
    while esquerdo <= direito:
        meio = (esquerdo + direito) // 2
        comparisons += 1
        if sorted_arr[meio] == target:
            return meio, comparisons
        if target < sorted_arr[meio]:
            direito = meio - 1
        else:
            esquerdo = meio + 1
    return -1, comparisons


def bubble_sort_count(arr):
    sorted_arr = arr.copy()
    tamanho = len(sorted_arr)
    comparisons = 0
    for passagem in range(tamanho - 1):
        for indice in range(tamanho - 1 - passagem):
            comparisons += 1
            if sorted_arr[indice] > sorted_arr[indice + 1]:
                sorted_arr[indice], sorted_arr[indice + 1] = (sorted_arr[indice + 1], sorted_arr[indice])
    return sorted_arr, comparisons

# B
import random

arr_sorted = list(range(1, 32))
arr_reverse = arr_sorted[::-1]

random.seed(42)
arr_random = arr_sorted.copy()
random.shuffle(arr_random)

listas = {
    "Ordenada": arr_sorted,
    "Invertida": arr_reverse,
    "Aleatoria": arr_random
}

for nome_lista, array in listas.items():
    print(f"\nLISTA: {nome_lista}")

    alvos = {
        "target_first": array[0],
        "target_middle": array[len(array) // 2],
        "target_absent": -1
    }

    if array == sorted(array):
        sorted_arr = array
        comparisons_ordenacao = 0
    else:
        sorted_arr, comparisons_ordenacao = bubble_sort_count(array)

    for nome_alvo, alvo in alvos.items():
        indice_linear, comparisons_linear = linear_search_count(array, alvo)
        indice_binario, comparisons_binaria = binary_search_count(sorted_arr, alvo)
        total_binario = comparisons_ordenacao + comparisons_binaria

        print(f"\nAlvo: {nome_alvo} ({alvo})")
        print(f"Busca linear: índice {indice_linear}, {comparisons_linear} comparações")
        print(f"Busca binária: índice {indice_binario}, {comparisons_binaria} comparações")
        print(f"Bubble Sort: {comparisons_ordenacao} comparações")
        print(f"Bubble Sort + Binária: {total_binario} comparações")
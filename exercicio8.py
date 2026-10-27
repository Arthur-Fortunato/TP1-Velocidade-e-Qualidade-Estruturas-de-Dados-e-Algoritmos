def cocktail_sort(array):
    esquerdo = 0
    direito = len(array) - 1
    while esquerdo < direito:
        for indice in range(esquerdo, direito):
            if array[indice] > array[indice + 1]:
                array[indice], array[indice + 1] = array[indice + 1], array[indice]

        direito -= 1

        for indice in range(direito, esquerdo, -1):
            if array[indice] < array[indice - 1]:
                array[indice], array[indice - 1] = array[indice - 1], array[indice]
        esquerdo += 1
    return array


testes = [
    [5, 2, 9, 1, 7],       
    [9, 7, 5, 3, 1, 2, 4, 8, 6, 10],       
    [4, 2, 4, 1, 2]                 
]

for array in testes:
    print(f"Array original: {array}")
    print(f"Array ordenado: {cocktail_sort(array.copy())}\n")
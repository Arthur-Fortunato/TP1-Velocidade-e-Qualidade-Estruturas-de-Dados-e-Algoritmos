import random

array = random.sample(range(20001), 10000)

def busca_linear(array, target):
    num_comparacoes = 0
    for numero in array:
        num_comparacoes += 1
        if numero == target:
            return num_comparacoes
    return num_comparacoes


elemento_primeira_posicao = array[0]
resultado_1 = busca_linear(array, elemento_primeira_posicao)
print(f"Número para busca: {elemento_primeira_posicao}")
print(f"Total de comparações: {resultado_1}\n")

alvo_aleatorio = random.choice(array)
resultado_2 = busca_linear(array, alvo_aleatorio)
print(f"Número para busca: {alvo_aleatorio}")
print(f"Total de comparações: {resultado_2}")

def maior_unico(array):
    frequencia_numeros = {}
    maior_numero_unico = None
    for numero in array:
        frequencia_numeros[numero] = frequencia_numeros.get(numero, 0) + 1
    for numero, quantidade_aparicoes in frequencia_numeros.items():
        if quantidade_aparicoes == 1:
            if maior_numero_unico is None or numero > maior_numero_unico:
                maior_numero_unico = numero
    return maior_numero_unico


numeros = [5, 12, 3, 48, 19, 48, 3, 5, 19, 64]
resultado = maior_unico(numeros)
print(f"Maior número único: {resultado}")
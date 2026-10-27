def encontrar_quadrado(qtd_graos):
    graos_quadrado = 1
    for quadrado in range(1, 65):
        if graos_quadrado >= qtd_graos:
            return quadrado
        graos_quadrado *= 2
    return "Quantidade excede o limite do tabuleiro."

print(f"Grãos: {1} | Resultado: {encontrar_quadrado(1)}")
print(f"Grãos: {2} | Resultado: {encontrar_quadrado(2)}")
print(f"Grãos: {4} | Resultado: {encontrar_quadrado(4)}")
print(f"Grãos: {8} | Resultado: {encontrar_quadrado(8)}")
print(f"Grãos: {1000} | Resultado: {encontrar_quadrado(1000)}")
print(f"Grãos: {1000000} | Resultado: {encontrar_quadrado(1000000)}")
print(f"Grãos: {2**64} | Resultado: {encontrar_quadrado(2**64)}")
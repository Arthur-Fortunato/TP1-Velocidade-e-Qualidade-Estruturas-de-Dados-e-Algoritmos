Introdução

A análise de complexidade raramente ocorre apenas sobre algoritmos escritos pelo próprio desenvolvedor. Na prática profissional, é comum avaliar código existente para estimar seu custo computacional, identificar gargalos e orientar decisões de otimização. Este exercício desenvolve a habilidade de ler código de forma analítica, explicitando hipóteses sobre o modelo de custo adotado e relacionando estrutura de controle, tamanho da entrada e crescimento assintótico.

Considere a seguinte função em Python:
```json
def only_a_strings(strings):
    result = []
    for s in strings:
        if len(s) > 0 and s[0] == "a":
            result.append(s)
    return result
```
Tarefa

Considere as seguintes premissas obrigatórias para a análise:

O array de entrada strings possui N elementos.
Cada elemento do array é uma string de tamanho médio constante (ou seja, o tamanho das strings não cresce com N).
As operações len(s), s[0] == "a" e append possuem custo constante O(1).
Não considere o custo de alocação de memória interna do Python além dessas operações.
Com base nessas premissas:

Identifique quantas vezes o laço for é executado em função de N.
Descreva as operações realizadas a cada iteração do laço.
Determine o custo total da função em função do tamanho do array de entrada.
Expresse a complexidade temporal do algoritmo utilizando Notação Big O.
Justifique tecnicamente sua resposta, relacionando a estrutura do código ao crescimento assintótico.
Observações

Não é necessário reescrever ou otimizar o código.
A resposta deve ser baseada exclusivamente na análise estrutural do algoritmo.
A clareza da justificativa é parte essencial da avaliação.

***
Identifique quantas vezes o laço for é executado em função de N -> Se o meu array tem N elementos, o for vai executar N vezes

Descreva as operações realizadas a cada iteração do laço -> Ele vê se a string não está vazia, depois, se não estiver vazia, ele vê se a primeira letra da string é "a", no fim, se essas duas condições forem True, adiciona a string na lista

Determine o custo total da função em função do tamanho do array de entrada -> o custo cresce proporcionalmente à quantidade de strings no array

Expresse a complexidade temporal do algoritmo utilizando Notação Big O -> O(n)

Justifique tecnicamente sua resposta, relacionando a estrutura do código ao crescimento assintótico -> A complexidade temporal é O(n), porque o algoritmo vai percorrer os N elementos uma só vez, sem laços aninhados ou operações que aumentem de custo conforme N for crescendo
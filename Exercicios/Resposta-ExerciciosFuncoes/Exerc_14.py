# Quadrado mágico. Um quadrado mágico é aquele dividido em linhas e colunas, com um número em cada posição e no qual a
# soma das linhas, colunas e diagonais é a mesma. Por exemplo, veja um quadrado mágico de lado 3, com números de 1 a 9:
            # 8 3 4
            # 1 5 9
            # 6 7 2
# Elabore uma função que identifica e mostra na tela todos os quadrados mágicos com as características acima. Dica:
# produza todas as combinações possíveis e verifique a soma quando completar cada quadrado. Usar um vetor de 1 a 9
# parece ser mais simples que usar uma matriz 3x3.

from itertools import permutations

numeros_validos = [1, 2, 3, 4, 5, 6, 7, 8, 9]

def verficar_soma_valores(matriz_criada):
    if sum(matriz_criada[:3]) == sum(matriz_criada[3:6]) == sum(matriz_criada[6:10]):
        if sum(matriz_criada[::3]) == sum(matriz_criada[1::3]) == sum(matriz_criada[2::3]):
            if sum(matriz_criada[::4]) == sum(matriz_criada[2:8:2]):
                print('Quadrado mágico criado com sucesso')
                print(f'{matriz_criada[0:3]}\n'
                      f'{matriz_criada[3:6]}\n'
                      f'{matriz_criada[6:]}\n')
                return 1
            else:
                return 0
        else:
            return 0
    return 0

def gerar_matriz(matriz):
    cont = 0
    validos = 0
    for i in permutations(matriz, 9):
        cont += 1
        validos += verficar_soma_valores(i)
    print(f'Foram verificados {cont} e obtivemos {validos} matrizes validas')

gerar_matriz(numeros_validos)


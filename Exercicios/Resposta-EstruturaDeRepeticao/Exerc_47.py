# Em uma competição de ginástica, cada atleta recebe votos de sete jurados. A melhor e a pior nota são eliminadas. A sua nota
# fica sendo a média dos votos restantes. Você deve fazer um programa que receba o nome do ginasta e as notas dos sete jurados
# alcançadas pelo atleta em sua apresentação e depois informe a sua média, conforme a descrição acima informada (retirar o
# melhor e o pior salto e depois calcular a média com as notas restantes). As notas não são informados ordenadas. Um exemplo de
# saída do programa deve ser conforme o exemplo abaixo:
    # Atleta: Aparecido Parente
    # Nota: 9.9
    # Nota: 7.5
    # Nota: 9.5
    # Nota: 8.5
    # Nota: 9.0
    # Nota: 8.5
    # Nota: 9.7
    # Resultado final:
    # Atleta: Aparecido Parente
    # Melhor nota: 9.9
    # Pior nota: 7.5
    # Média: 9,04

import numpy as np

nome_atleta = 'NomeAtleta'
nota_jurado = []

while nome_atleta != '':
    nome_atleta = input('Informe o nome do Atleta: ')

    for i in range(1, 8):
        valor_salto = float(input(f'{i}° Jurado informe nota: '))
        nota_jurado.append(valor_salto)

    print()
    melhor_nota = max(nota_jurado)
    pior_nota = min(nota_jurado)

    print(f'Atleta: {nome_atleta}')
    for valor in nota_jurado:
        print(f'Nota: {valor:.1f}')

    nota_jurado.remove(melhor_nota)
    nota_jurado.remove(pior_nota)
    media = np.mean(nota_jurado)
    print()
    print('Resultado Final:')
    print(f'Atleta: {nome_atleta}')
    print(f'Melhor nota: {melhor_nota:.1f}')
    print(f'Pior nota: {pior_nota:.1f}')
    print(f'Média: {media:.2f}')

    print()
    print('Informe o nome do próximo atleta ou deixe em branco para finalizar o sistema')
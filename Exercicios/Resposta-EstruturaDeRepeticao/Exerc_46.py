# Em uma competição de salto em distância cada atleta tem direito a cinco saltos. No final da série de saltos de cada atleta, o
# melhor e o pior resultados são eliminados. O seu resultado fica sendo a média dos três valores restantes. Você deve fazer um
# programa que receba o nome e as cinco distâncias alcançadas pelo atleta em seus saltos e depois informe a média dos saltos
# conforme a descrição acima informada (retirar o melhor e o pior salto e depois calcular a média). Faça uso de uma lista para
# armazenar os saltos. Os saltos são informados na ordem da execução, portanto não são ordenados. O programa deve ser
# encerrado quando não for informado o nome do atleta. A saída do programa deve ser conforme o exemplo abaixo:
    # Atleta: Rodrigo Curvêllo
    # Primeiro Salto: 6.5 m
    # Segundo Salto: 6.1 m
    # Terceiro Salto: 6.2 m
    # Quarto Salto: 5.4 m
    # Quinto Salto: 5.3 m
    # Melhor salto: 6.5 m
    # Pior salto: 5.3 m
    # Média dos demais saltos: 5.9 m
    # Resultado final:
    # Rodrigo Curvêllo: 5.9 m

import numpy as np

nome_atleta = 'NomeAtleta'
nota_saltos = []

while nome_atleta != '':
    nome_atleta = input('Informe o nome do Atleta: ')
    if nome_atleta == '':
        print('Programa encerrado')

    else:
        for i in range(1, 6):
            valor_salto = float(input(f'Informe a {i}° distância do Salto: '))
            nota_saltos.append(valor_salto)
    print()
    melhor_salto = max(nota_saltos)
    pior_salto = min(nota_saltos)

    print(f'Atleta: {nome_atleta}')
    for key, valor in enumerate(nota_saltos, start=1):
        print(f'{key}° salto: {valor:.1f}m')

    nota_saltos.remove(melhor_salto)
    nota_saltos.remove(pior_salto)
    media = np.mean(nota_saltos)
    print()
    print(f'Melhor Salto {melhor_salto:.1f}m')
    print(f'Pior Salto {pior_salto:.1f}m')
    print(f'Média dos demais saltos {media:.1f}m')
    print()
    print('Resultado Final:')
    print(f'{nome_atleta}: {media:.1f}m')
    print()
    print('Informe o nome do próximo atleta ou deixe em branco para finalizar o sistema')

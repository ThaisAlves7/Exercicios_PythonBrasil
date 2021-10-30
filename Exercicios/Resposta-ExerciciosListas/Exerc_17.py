# Em uma competição de salto em distância cada atleta tem direito a cinco saltos. O resultado do atleta será determinado pela
# média dos cinco valores restantes. Você deve fazer um programa que receba o nome e as cinco distâncias alcançadas pelo atleta
# em seus saltos e depois informe o nome, os saltos e a média dos saltos. O programa deve ser encerrado quando não for informado
# o nome do atleta. A saída do programa deve ser conforme o exemplo abaixo:
    # Atleta: Rodrigo Curvêllo
    # Primeiro Salto: 6.5 m
    # Segundo Salto: 6.1 m
    # Terceiro Salto: 6.2 m
    # Quarto Salto: 5.4 m
    # Quinto Salto: 5.3 m
    # Resultado final:
    # Atleta: Rodrigo Curvêllo
    # Saltos: 6.5 - 6.1 - 6.2 - 5.4 - 5.3
    # Média dos saltos: 5.9 m

import numpy as np

nome_atleta = 'NomeAtleta'
distancia_salto = []

while nome_atleta != '':
    nome_atleta = input('Informe o nome do Atleta: ').title()
    if nome_atleta == '':
        print('Programa encerrado')

    else:
        for i in range(1, 6):
            salto = float(input(f'Informe a {i}° distância do Salto: '))
            distancia_salto.append(salto)
    print()

    print(f'Atleta: {nome_atleta}')
    for key, valor in enumerate(distancia_salto, start=1):
        print(f'{key}° salto: {valor:.1f}m')

    media = np.mean(distancia_salto)
    print()
    print('Resultado Final:')
    print(f'Atleta: {nome_atleta}')
    print(f'Saltos: {distancia_salto[0]} - {distancia_salto[1]} - {distancia_salto[2]} - {distancia_salto[3]} - {distancia_salto[4]}')
    print(f'Média dos demais saltos {media:.1f}m')
    print()
    print('Informe o nome do próximo atleta ou deixe em branco para finalizar o sistema')
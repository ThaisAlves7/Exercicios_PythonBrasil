# Foi feita uma estatística em cinco cidades brasileiras para coletar dados sobre acidentes de trânsito. Foram obtidos os seguintes
# dados:
    # a. Código da cidade;
    # b. Número de veículos de passeio (em 1999);
    # c. Número de acidentes de trânsito com vítimas (em 1999). Deseja-se saber:
    # d. Qual o maior e menor índice de acidentes de transito e a que cidade pertence;
    # e. Qual a média de veículos nas cinco cidades juntas;
    # f. Qual a média de acidentes de trânsito nas cidades com menos de 2.000 veículos de passeio.

import numpy as np

codigo_cidade = []
veiculos = acidentes = []
continuar = 1

def adicionar_lista(codigo):
    if codigo == 1:
        codigo_cidade.append('cidadeA')

    elif codigo == 2:
        codigo_cidade.append('cidadeB')

    elif codigo == 3:
        codigo_cidade.append('cidadeC')

    elif codigo == 4:
        codigo_cidade.append('cidadeD')

    else:
        codigo_cidade.append('cidadeE')

    print(f'Adiciona na lista: {codigo_cidade}')

def relatorio_acidentes(lista_codigos: list, lista_veiculos: list, lista_acidentes: list):
    soma = 0
    cont = index_maior = index_menor = 1
    maior_acidente = menor_acidente = None

    for index, valor in enumerate(lista_acidentes):
        if (maior_acidente is None) or (valor > maior_acidente):
            maior_acidente = valor
            index_maior = index

        if (menor_acidente is None) or (valor < menor_acidente):
            menor_acidente = valor
            index_menor = index

        if (valor < 2000):
            soma += valor
            cont = + 1

    veic = lista_veiculos
    print(veiculos)
    media_veiculos = np.mean(veic)
    media_menos_2000 = soma / cont

    print()
    print(f'O maior índice de acidentes é na cidade Código: {lista_codigos[index_maior]}: Veiculos: {lista_veiculos[index_maior]} ,Acidentes: {lista_acidentes[index_maior]}')
    print(f'O menor índice de acidentes é na cidade Código: {lista_codigos[index_menor]}: Veiculos: {lista_veiculos[index_menor]} ,Acidentes: {lista_acidentes[index_menor]}')
    print(f'A média de veiculos nas 5 cidades foi: {media_veiculos:.0f}')
    print(f'A media de acidentes nas 5 cidades com menos de 2000 veiculos é {media_menos_2000:.0f}')



while continuar != 2:
    codigo = int(input('Informe o codigo da cidade\n'
                       '1 - cidadeA\n'
                       '2 - cidadeB\n'
                       '3 - cidadeC\n'
                       '4 - cidadeD\n'
                       '5 - cidadeE: '))
    while codigo not in [1, 2, 3, 4, 5]:
        print()
        print('Informe um codigo de cidade válido')
        codigo = int(input('Informe o codigo da cidade\n'
                           '1 - cidadeA\n'
                           '2 - cidadeB\n'
                           '3 - cidadeC\n'
                           '4 - cidadeD\n'
                           '5 - cidadeE: '))
        print()

    adicionar_lista(codigo)
    veiculo = int(input('Informe a quantidade de veiculos de passeio em 1999: '))
    veiculos.append(veiculo)
    acidente = int(input('Informe a quantidade de acidentes em 1999: '))
    acidentes.append(acidente)
    print()
    continuar = int(input('Deseja continuar 1 - Sim ou 2 Não: '))
    while continuar not in [1, 2]:
        print()
        print('Informe uma seleção válida')
        continuar = int(input('Deseja continuar 1 - Sim ou 2 Não: '))
        print()

relatorio_acidentes(codigo_cidade, veiculos, acidentes)

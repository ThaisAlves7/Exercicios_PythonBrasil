#  Em uma eleição presidencial existem quatro candidatos. Os votos são informados por meio de código. Os códigos utilizados são:
    # 1 , 2, 3, 4 - Votos para os respectivos candidatos
# (você deve montar a tabela ex: 1 - Jose/ 2- João/etc)
    # 5 - Voto Nulo
    # 6 - Voto em Branco
    # Faça um programa que calcule e mostre:
    # O total de votos para cada candidato;
    # O total de votos nulos;
    # O total de votos em branco;
    # A percentagem de votos nulos sobre o total de votos;
    # A percentagem de votos em branco sobre o total de votos. Para finalizar o conjunto de votos tem-se o valor zero


voto = 1
qtde_votos = []

while voto != 0:

    voto = int(input('Insira o a opção de voto que voce deseja\n'
                     '1 - José\n'
                     '2 - João\n'
                     '3 - Pedro\n'
                     '4 - Marina\n'
                     '5 - Nulo\n'
                     '6 - Branco'
                     '0 - Sair: '))
    print()
    while voto not in [0, 1, 2, 3, 4, 5, 6]:
        print('Insira um voto válido')
        voto = int(input('Insira o a opção de voto que voce deseja\n'
                         '1 - José\n'
                         '2 - João\n'
                         '3 - Pedro\n'
                         '4 - Marina\n'
                         '5 - Nulo\n'
                         '6 - Branco'
                         '0 - Sair: '))
        print()
    qtde_votos.append(voto)

votos_brancos = qtde_votos.count(6)
votos_nulos = qtde_votos.count(5)
total_votos = len(qtde_votos)
porc_nulo = ((votos_nulos / total_votos) - 1) * 100
porc_branco = ((votos_nulos / total_votos) - 1) * 100

print('A quantidade de votos para\n'
      f'1 - José foram {qtde_votos.count(1)}'
      f'2 - João foram {qtde_votos.count(2)}'
      f'3 - Pedro foram {qtde_votos.count(3)}'
      f'4 - Marina foram {qtde_votos.count(4)}'
      f'5 - Nulo foram {votos_nulos}'
      f'6 - Branco foram {votos_nulos}')
print(f'A porcentagem total de votos nulos é {porc_nulo}')
print(f'A porcentagem total de votos brancos é {porc_branco}')

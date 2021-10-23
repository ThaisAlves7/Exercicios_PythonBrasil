# Faça um programa para um caixa eletronico. O programa deverá perguntar ao usuario o valor do saque e depois informar
# quantas notas de cada valor serão fornecidas. As notas disponiveis serão as de 1, 5, 10, 50, 100. O valor minimo é de 10
# reias e o maximo de 600 reais. O programa não deve se preocupar com a quantidade de notas existentes na maquina.
    # A - Exemplo 1: Para sacar a quantia de 256 reais, o programa fornece 2 notas de 100, uma nota de 50 uma de 5 e 1 nota de 1
    # B - Exemplo 2: Para sacar a quantia de 399 reias, o programa fornece 3 notas de 100, uma nota de 50 ,uma nota de 10,
        # uma nota de 5, 1 nota de 1

valor = int(input('Digite um valor para sacar minimo de 10 e maximo de 600: '))

saque = valor

nota100 = int(valor / 100)
valor = valor - (nota100 * 100)

nota50 = int(valor / 50)
valor = valor - (nota50 * 50)

nota10 = int(valor / 10)
valor = valor - (nota10 * 10)

nota5 = int(valor / 5)
valor = valor - (nota5 * 5)

nota1 = valor

if ((saque < 10) or (saque > 600)):
    print(f'O valor de {saque} reais não é um valor válido. Para sacar escolha um valor entre 10 a 600 reais')

else:
    print(f'O valor para saque é R${saque} = {nota100} notas de 100, {nota50} notas de 50, {nota10} notas de 10, {nota5} notas de 5 e {nota1} notas de 1')

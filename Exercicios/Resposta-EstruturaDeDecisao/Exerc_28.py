# O Hipermercado Tabajara está com uma promoção de carnes que é imperdível. Confira:
    #                            Até 5Kg             Acima de 5Kg
    # File Duplo           R$4,90 por Kg            R$5,80 por Kg
    # Alcatra              R$5,90 por Kg            R$6,80 por Kg
    # Picanha              R$6,90 por Kg            R$7,80 por Kg

# Para atender a todos os clientes, cada cliente poderá levar apenas 1 dos tipos de carne na promoção, porém não há limites
    # para a quantidade de carne por cliente. Se compra foi feita no cartão Tabajaras o cliente receberá ainda um desconto
    # de 5% sobre o total da compra. Escreva um programa que peça o tipo e a quantidade de carne comprada pelo usuario e gere
    # um cupom fiscal, contendo as informações da compra: tipo e quantidade de carne, preço total, tipo de pagamento, valor do desconto
    # e valor a pagar


file_ate_5 = 4.90
file_acima_5 = 5.80

alcatra_ate_5 = 5.90
alcatra_acima_5 = 6.80

picanha_ate_5 = 6.90
picanha_acima_5 = 7.80

desconto = 5
selecao = ['Filé Duplo', 'Alcatra', 'Picanha']

tipo = int(input('Informe o tipo da Carne\n'
                 '1 - Filé Duplo\n'
                 '2 - Alcatra\n'
                 '3 - Picanha: \n'
                 ''))

while (tipo not in [1, 2, 3]):
    print('Informe uma opção válida do menu ')
    tipo = int(input('Informe o tipo da Carne\n'
                     '1 - Filé Duplo\n'
                     '2 - Alcatra\n'
                     '3 - Picanha: \n'
                     ''))
kg = float(input('Informe quantos Kg você esta comprando: '))
forma_pagamento = int(input('Informe a tipo de pagamento\n'
                            '1 - Cartão Tabajaras\n'
                            '2 - Outra forma de pagamento: \n'
                            ''))

while (forma_pagamento not in [1, 2]):
    print('Informe uma opção de pagamento válida ')
    forma_pagamento = int(input('Informe a tipo de pagamento\n'
                                '1 - Cartão Tabajaras\n'
                                '2 - Outra forma de pagamento: \n'
                                ''))

if (tipo == 1):
    tipo = selecao[0]
    if (kg <= 5):
        valor_pagar = kg * file_ate_5

    else:
        valor_pagar = kg * file_acima_5

elif (tipo == 2):
    tipo = selecao[1]
    if (kg <= 5):
        valor_pagar = kg * alcatra_ate_5

    else:
        valor_pagar = kg * alcatra_acima_5
else:
    tipo = selecao[2]
    if (kg <= 5):
        valor_pagar = kg * picanha_ate_5

    else:
        valor_pagar = kg * picanha_acima_5

preco_total = valor_pagar

if (forma_pagamento == 1):
    forma_pagamento = 'Cartão Tabajaras'
    desconto_tabajaras = (valor_pagar * desconto) / 100
    valor_pagar -= desconto_tabajaras
else:
    valor_pagar = preco_total
    desconto_tabajaras = 0
    forma_pagamento = 'Outra forma de pagamento'
    desconto = 0

print(f'A carne escolhida foi: {tipo}')
print(f'A quantidade comprada foi {kg}Kg')
print(f'O preço total da compra ficou R${preco_total:.2f}')
print(f'A forma de pagamento escolhida foi {forma_pagamento}')
print(f'O valor do desconto foi R${desconto_tabajaras:.2f}')
print(f'O valor a pagar ficou em R${valor_pagar}')
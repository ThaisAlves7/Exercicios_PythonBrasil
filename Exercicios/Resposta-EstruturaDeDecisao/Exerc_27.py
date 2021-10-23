# Uma fruteira esta vendendo frutas com a seguinte tabela de preços:
    #                       Até 5Kg             Acima de 5Kg
    # Morango         R$2,50 por Kg            R$2,20 por Kg
    # Maça            R$1,80 por Kg            R$1,50 por Kg

# Se o cliente comprar mais de 8Kg em frutas ou o valor total da comprar ultrapassar R$25,00 reias, recebera ainda um desconto
    # de 10% sobre este total. Escreva um algoritmo para ler a quantidade (em Kg) de morangos e a quantidade (em Kg) de maças
    # adquiridas e escreva o valor a ser pago pelo cliente.

morango_ate_5 = 2.50
morango_acima_5 = 2.20

maca_ate_5 = 1.80
maca_acima_5 = 1.50

desconto = 10

maca = int(input('Quantas Kg de Maçã voê comprou: '))
morango = int(input('Quantos Kg de Morango você comprou: '))

if ((maca == 0) and (morango == 0)):
    print('Informe quantos kilos você comprou de frutas')

else:
    if (maca <= 5):
        valor_maca = maca * maca_ate_5

    else:
        valor_maca = maca * maca_acima_5

    if ((maca >= 8) or (valor_maca >= 25)):
        valor_maca = valor_maca - ((valor_maca * desconto) / 100)


    if (morango <= 5):
        valor_morango = morango * morango_ate_5

    else:
        valor_morango = morango * morango_acima_5

    if ((maca >= 8) or (valor_morango >= 25)):
        valor_morango = valor_morango - ((valor_morango * desconto) / 100)

print(f'Você comprou {maca}Kg e ira pagar R${valor_maca:.2f}')
print(f'Você comprou {morango}Kg e ira pagar R${valor_morango:.2f}')
print(f'Valor Total da compra é R${valor_maca+valor_morango:.2f}')

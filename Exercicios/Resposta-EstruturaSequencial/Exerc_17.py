# Faça um programa para uma loja de tintas. O programa deverá pedir o tamanho em metros quadrados da área ser pintada.
#Considere que a cobertura da tinta é de 1 litro para cada 6 metros quadrados e que a tinta é vendida em latas de 18 litros
# que custam R$ 80,00 ou em galões de 3,6 litros que custam R$25,00.
#Informe ao usuario as quantidades de tintas compradas e os respectivos preços em 3 situações:
    # Comprar apenas latas de 18 litros
    # Comprar apenas galões de 3.6 litros
    # Misturas latas e galoes de forma que o disperdicio de tintas seja menor. Acrecescente 10% de folga e sempre arredonde os valores para cima , isto é considere latas cheias

import math

preco_galao = 80.00
preco_lata = 25.00
capacidade_galao = 18
capacidade_lata = 3.6
acrescimo = 1.1

metro = float(input('Digite o metro da area: '))
qtde_necessaria = metro / 6 * acrescimo

qtde_galao = math.ceil(qtde_necessaria / capacidade_galao)
total_a_pagar_galao = qtde_galao * preco_galao

qtde_latas = math.ceil(qtde_necessaria / capacidade_lata)
total_a_pagar_lata = qtde_latas * preco_lata

qtde_mista_galao = qtde_necessaria // capacidade_galao
qtde_mista_lata = math.ceil((qtde_necessaria - qtde_mista_galao * capacidade_galao) / capacidade_lata)
valor_a_pagar_misto = (qtde_mista_galao * preco_galao) + (qtde_mista_lata * preco_lata)


mistura_latas = 3
pagamento_misto = 2

print(f'Quantidade de tinta necessaria é: {qtde_necessaria:.2f}')
print()
print(f'Quantidade de Latas necessárias: {qtde_latas:.0f}')
print(f'Valor a ser gasto com as Latas é R$ {total_a_pagar_lata:.2f}')
print()
print(f'Quantidade de Galões necessárias: {qtde_galao:.0f}')
print(f'Valor a ser gasto com os Galões é R$ {total_a_pagar_galao:.2f}')
print()
print(f'Se você for considerar reduzir o disperdicio temos a seguinte opção mista para você:')
print()
print(f'Quantidade de Galões a ser considerado: {qtde_mista_galao:.0f}')
print(f'Quantidade de Latas a ser considerada: {qtde_mista_lata:.0f}')
print(f'Valor a ser pago para a modalidade de compra mista é R$ {valor_a_pagar_misto:.2f}')

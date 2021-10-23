# Faça um programa para uma loja de tintas. O programa deverá pedir o tamanho em metros quadrados da area a ser pintada
#Considere que a cobertura da tinta é de 1 litro para cada 3 metros quadrados e que a tinta é vendida em latas de 18 litros
# que custam R$80 reais. Informe ao usuario a quantidade de latas de tintas a serem compradas e o preço total.

preco_lata = 80.00
capacidade_Litro = 18

metro = float(input('Digite o metro da area: '))
quantidade_necessaria = metro / 3

qtde_latas = quantidade_necessaria / capacidade_Litro
total_a_pagar = qtde_latas * preco_lata

print(f'Quantidade de Latas necessárias: {qtde_latas:.1f}')
print(f'Valor a ser gasto R$ {total_a_pagar:.2f}')
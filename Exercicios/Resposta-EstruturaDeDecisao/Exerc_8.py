# Faça um programa que pergunte o preço de 3 produtos e informe qual produto voce deve comprar, sabendo
# que a decisão é sempre pelo mais barato.

preco = []
for i in range(1, 4):
    numero = float(input('Digite o preço do produto: '))
    preco.append(numero)

menor = min(preco)

print(f'O produto com o menor valor custa R${menor}')

# Faça um programa que peça 4 notas bimestrais e mostre a média

print('Calculando a média de notas!!!')
soma = 0
for i in range(1, 5):
    nota = float(input(f'Digite a {i}° nota: '))
    soma += nota

media = soma / 4
# print(soma)
print(f'A média dessas notas é {media:.1f}')
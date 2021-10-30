# Faça um Programa que leia 4 notas, mostre as notas e a média na tela.

import numpy as np

lista_notas = []

for i in range(1, 5):
    nota = float(input(f'Informe a {i}° nota: '))
    lista_notas.append(nota)

media = np.mean(lista_notas)

print(f'As notas inseridas foram: {lista_notas}')
print(f'A média das notas é: {media:.2f}')
# Faça um programa que calcule e o mostre a media aritmetica de N notas.

import numpy as np

continuar = 1
notas = []

nota1 = float(input('Digite uma nota: '))
notas.append(nota1)
nota2 = float(input('Digite outra nota: '))
notas.append(nota2)

while continuar != 2:
    print()
    continuar = int(input('Você deseja continuar: 1 - Sim ou 2 - Não: '))
    if continuar == 1:
        nota2 = float(input('Digite outra nota: '))
        notas.append(nota2)

media = np.mean(notas)

print(f'A média das notas digitadas foi {media}')

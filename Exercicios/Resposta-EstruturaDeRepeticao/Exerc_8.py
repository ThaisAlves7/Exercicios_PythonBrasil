# Faça um programa que leia 5 numeros e informe a soma e a media aritmetica dos numeros

import numpy as np

valores = []

for i in range(1, 6):
    number = int(input(f'Informe {i}° número: '))
    valores.append(number)

maior = max(valores)
media = np.mean(valores)

print(f'O Maior numero digitado foi {maior}')
print(f'A Média Aritmetica foi {media:.1f}')
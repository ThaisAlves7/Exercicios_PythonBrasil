# O Departamento Estadual de Meteorologia lhe contratou para desenvolver um programa que leia as um conjunto indeterminado
# de temperaturas, e informe ao final a menor e a maior temperaturas informadas, bem como a média das temperaturas.

import numpy as np

temperatura = []
temp = cont = 1

while temp != 0:
    temp = float(input(f'Informe a {cont}° temperatura ou 0 para finalizar a inserção:  '))
    if temp != 0:
        temperatura.append(temp)
    cont += 1

media = np.mean(temperatura)
maior = max(temperatura)
menor = min(temperatura)

print(f'A Média de temperatura é: {media:.2f}°C')
print(f'A Maior Temperatura é: {maior}°C')
print(f'A Menor Temperatura é : {menor}°C')

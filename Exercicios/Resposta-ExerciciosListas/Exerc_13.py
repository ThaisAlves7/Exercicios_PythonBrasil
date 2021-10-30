# Faça um programa que receba a temperatura média de cada mês do ano e armazene-as em uma lista. Após isto, calcule a média
# anual das temperaturas e mostre todas as temperaturas acima da média anual, e em que mês elas ocorreram (mostrar o mês por
# extenso: 1 – Janeiro, 2 – Fevereiro, . . . )

import numpy as np

mes = ['Janeiro', 'Fevereiro', 'Março', 'Abril', 'Maio', 'Junho', 'Julho', 'Agosto', 'Setembro', 'Outubro', 'Novembro', 'Dezembro']
temperatura = []

for key, value in enumerate(mes):
    temp = float(input(f'Informe a temperatura do mês de {value}: '))
    temperatura.append(temp)
print()
temp_media = np.mean(temperatura)

for mes, temp in zip(mes, temperatura):
    if temp > temp_media:
        print(f'O {mes} teve a temperatura maior que a média anual')

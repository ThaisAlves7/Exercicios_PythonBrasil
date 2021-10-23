# Faça um programa que peça o raio de um circulo, calcule e mostre sua area

import math

print('Calculo de Area do Circulo')

raio = float(input('Digite o raio do Circulo: '))
area = math.pi * (raio ** 2)

print(f'A area do Circulo é {area:.2f}')

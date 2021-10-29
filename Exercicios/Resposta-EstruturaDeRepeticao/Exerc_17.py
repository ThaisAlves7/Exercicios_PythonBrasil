# Faça um programa que calcule  o fatorial de um numero inteiro fornecido pelo usuario. Ex: 5! = 5.4.3.2.1 = 120

import math

number = int(input('Informe um numero: '))

fatorial = math.factorial(number)

print(f'O Fatorial de {number} é {fatorial}')
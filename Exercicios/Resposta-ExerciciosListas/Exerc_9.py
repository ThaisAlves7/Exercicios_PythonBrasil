# Faça um Programa que leia um vetor A com 10 números inteiros, calcule e mostre a soma dos quadrados dos elementos do vetor

import math

numbers, number_quadrado = [], []

for i in range(1, 11):
    num = int(input('Informe um número inteiro: '))
    numbers.append(num)

for x in numbers:
    number_quadrado.append(math.sqrt(x))

soma = sum(number_quadrado)
print()
print(f'A soma do quadrado dos elementos é: {soma:.2f}')
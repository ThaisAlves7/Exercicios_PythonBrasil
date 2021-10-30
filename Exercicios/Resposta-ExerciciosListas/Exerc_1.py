# Faça um Programa que leia um vetor de 5 números inteiros e mostre-os

lista_numeros = []

for i in range(1, 6):
    numbers = int(input(f'Informe {i}° numero: '))
    lista_numeros.append(numbers)

print(f'Os números digitados foram: {lista_numeros}')
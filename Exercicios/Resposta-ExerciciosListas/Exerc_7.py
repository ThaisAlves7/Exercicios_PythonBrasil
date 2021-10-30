# Faça um Programa que leia um vetor de 5 números inteiros, mostre a soma, a multiplicação e os números

from math import prod

lista = []

for i in range(1, 6):
    number = int(input('Informe um numero: '))
    lista.append(number)

produto = prod(lista)
soma = sum(lista)

print(f'Os números digitados foram: {lista}')
print(f'A soma dos números foi: {soma}')
print(f'A multiplicação dos números é: {produto}')
# Faça um programa que leia 3 numeros e mostre o maior deles

number = []
for i in range(1, 4):
    numero = int(input('Digite um numero: '))
    number.append(numero)

maior = max(number)

print(f'O maior numero digitado foi: {maior}')

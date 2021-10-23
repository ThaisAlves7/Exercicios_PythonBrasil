# Faça um programa que leia 3 numeros e mostre o maior e o menor deles

number = []
for i in range(1, 4):
    numero = int(input('Digite um numero: '))
    number.append(numero)

maior = max(number)
menor = min(number)

print(f'O maior numero digitado foi: {maior}')
print(f'O menor numero digitado foi: {menor}')

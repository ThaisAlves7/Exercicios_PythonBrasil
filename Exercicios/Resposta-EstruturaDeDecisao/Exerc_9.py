# Faça um programa que leia 3 numeros e mostre-os em ordem descrescente

number = []
for i in range(1, 4):
    numero = int(input('Digite um número: '))
    number.append(numero)

descrescente = sorted(number, reverse=True)

print(f'Os numeros em ordem descrescente é: {descrescente}')

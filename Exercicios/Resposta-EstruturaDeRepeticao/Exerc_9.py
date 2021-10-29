# Faça um programa que imprima na tela apenas os numeros impares entre 1 e 50

impares = []

for i in range(1, 51):
    if (i % 2 != 0):
         impares.append(i)

print(f'Os números impares entre 1 e 50 são: {impares}')
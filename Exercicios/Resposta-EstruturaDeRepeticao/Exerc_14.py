# Faça um programa que leia 10 numeros inteiros, calcule e mostre a quantidade de numeros pares e a quantidade de numeros impares

impares, pares = [], []

for i in range(1, 11):
    number = int(input(f'Informe {i}° numero: '))

    if (number % 2 != 0):
        impares.append(number)

    else:
        pares.append(number)

par = len(pares)
impar = len(impares)

print(f'Tivemos {par} quantidade números pares')
print(f'Tivemos {impar} quantidade números impares')
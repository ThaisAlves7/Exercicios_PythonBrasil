# Faça um Programa que leia 20 números inteiros e armazene-os num vetor. Armazene os números pares no vetor PAR e os
# números IMPARES no vetor impar. Imprima os três vetores

par, impar = [], []

for i in range(1, 7):
    num = int(input(f'Informe {i} numero inteiro: '))
    resto = num % 2

    if resto % 2 == 0:
        par.append(num)

    else:
        impar.append(num)


print(f'Números Pares: {par}')
print(f'Números Impares: {impar}')
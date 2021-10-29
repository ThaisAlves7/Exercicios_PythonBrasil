# Sendo H= 1 + 1/2 + 1/3 + 1/4 + ... + 1/N, Faça um programa que calcule o valor de H com N termos.

final = int(input('Informe o numero de repetições: '))
valor = 0
inicioS = finalS = 1
sequencia = []
sequencia_imprimir = []

for i in range(1, final):
    valor = inicioS / finalS
    finalS += 1
    print(f'{inicioS} / {finalS}')

    sequencia.append(valor)
    sequencia_imprimir.append('1')
    sequencia_imprimir.append(f'{inicioS} / {finalS}')
    sequencia_imprimir.append('+')

soma = sum(sequencia) + 1

print(f'H = {sequencia_imprimir}')
print(f'A soma da sequência é {soma:.2f}')
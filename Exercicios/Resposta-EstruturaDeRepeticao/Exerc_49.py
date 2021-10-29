# Faça um programa que mostre os n termos da Série a seguir:
# S = 1/1 + 2/3 + 3/5 + 4/7 + 5/9 + ... + n/m.


final = int(input('Informe o numero de repetições: '))
valor = 0
inicioS = 1
finalS =1
sequencia = []
sequencia_imprimir = []

for i in range(1, final):
    valor = inicioS / finalS
    inicioS += 1
    finalS += 2
    sequencia.append(valor)
    sequencia_imprimir.append(f'{inicioS} / {finalS}')

soma = sum(sequencia)

print(f'H = {sequencia_imprimir}')
print(f'A soma da sequência é {soma:.2f}')

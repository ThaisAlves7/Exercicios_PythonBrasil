# Faça um programa qudado um conjunto de N numero determine o menor, o maior, a soma dos valores

valores = []
continuar = 1

while (continuar != 2):
    number = int(input('Entre com o numero um numero: '))
    print()
    continuar = int(input('Deseja continuar digitando numeros?\n'
                          '1 - Sim ou 2 - Não: '))
    valores.append(number)
print()
print(f'O maior número é {max(valores)}')
print(f'O menor número é {min(valores)}')
print(f'A soma deles é {sum(valores)}')

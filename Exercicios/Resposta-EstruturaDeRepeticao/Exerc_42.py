# Faça um programa que leia uma quantidade indeterminada de números positivos e conte quantos deles estão nos seguintes
# intervalos: [0-25], [26-50], [51-75] e [76-100]. A entrada de dados deverá terminar quando for lido um número negativo.
cont_25 = cont_50 = cont_75 = cont_100 = 1

while True:
    number = int(input('Insira um numero (Para encerrar insira um número negativo): '))
    if number > 0:

        if (number >= 0 and number <= 25):
            cont_25 += 1

        elif (number >= 26 and number <= 50):
            cont_50 += 1

        elif (number >= 51 and number <= 75):
            cont_75 += 1

        elif (number >= 76 and number <= 100):
            cont_100 += 1

    else:
        break

print(f'Foram inseridos {cont_25} entre [0-25]')
print(f'Foram inseridos {cont_50} entre [26-50]')
print(f'Foram inseridos {cont_75} entre [51-75]')
print(f'Foram inseridos {cont_100} entre [76-100]')
# Faça um programa que calcule as raizes de uma equação do segundo grau, na forma ax2 + bx + c. O programa devera pedir os valores a, b, c
# e fazer as consistencias, informando ao usuario nas seguintes situações:
    # A - Se o usuário informar o valor de A igual a zero, a equação não é do segundo grau e o programa não deve fazer pedir os demais valores, sendo encerrado
    # B - Se o delta calculado for negativo , a equação não possui raizaes reias. Informe ao usuario e encerre o programa
    # C - Se o delta for igual a zero a equação possui apenas uma raiz real, informe ao usuario
    # D - Se o delta for positivo, a equação possui 2 raizes reias; informe as ao usuario

import math

a = int(input('Informe o coeficiente A: '))

if (a == 0):
    print('Isso não é uma Equação de Segundo Grau')

else:
    b = int(input('Informe o coeficiente B: '))
    c = int(input('Informe o coeficiente C: '))

    delta = b * b - (4 * a * c)
    if (delta < 0):
        print('Isso é uma raiz imaginária')

    elif (delta == 0):
        raiz = -b / (2 * a)
        print(f'A raiz de Delta {delta} é {raiz}')

    else:
        raiz_mais = (-b + math.sqrt(delta)) / (2 * a)
        raiz_menos = (-b - math.sqrt(delta)) / (2 * a)
        print(f'A raiz de Delta {delta} é MAIS {raiz_mais} ou MENOS {raiz_menos}')
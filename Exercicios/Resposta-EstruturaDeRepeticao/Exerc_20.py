# Altere o programa de calculo fatorial, permitindo que ao usuario calcular o fatorial varias vezes e limitando a numeros
    # inteiros e moenores que 16

import math

continuar = 1

while continuar != 2:
    number = int(input('Informe um numero inteiro e menor que 16 para o cálculo Fatorial: '))
    validar = True if (number < 16) else False
    while validar != True:
        print('Informe um numero valido para o cálculo')
        number = int(input('Informe um numero inteiro e menor que 16 para o cálculo Fatorial: '))
        validar = True if (number < 16) else False

    fatorial = math.factorial(number)
    print(f'O Fatorial de {number} é {fatorial}')
    print()
    continuar = int(input('Deseja continuar digitando numeros?\n'
                          '1 - Sim ou 2 - Não: '))
    print()


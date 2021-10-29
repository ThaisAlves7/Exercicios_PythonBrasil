# Altere o programa de calculo dos numero primos, informando, caso o numero não seja primo, quais numeros ele
    # é divisivel


def validar_numeros_primos(number):
    cont = 1
    nao_primo = []

    for i in range(1, number):
        if (number % i == 0):
            cont += 1
            nao_primo.append(i)

    if (cont == 2):
        print(f'O numero {number} é um número primo')

    else:
        print(f'O numero {number} não é um número primo - Ele é divisível por {nao_primo}')



num = int(input('Digite um número: '))

if ((num < 0) or (num == 1)):
    print(f'O número {num} não é um número válido')

else:
    validar_numeros_primos(num)

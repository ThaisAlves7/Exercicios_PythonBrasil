# Faça um programa que mostre todos os numeros primos entre 1 e N sendo N o numero inteiro fornecido pelo usuario. O programa
    # deverá mostrar tambem o numero de divisões que ele executou para encontrar os numeros primos. Serão avaliados o funcionamento
    # o estilo e o numero de testes divisões executados


def validar_numeros_primos(number):
    cont, vezes = 1, 1

    for i in range(1, number):
        if (number % i == 0):
            cont += 1
            vezes += 1

        else:
            vezes += 1

    if (cont == 2):
        print(f'O numero {number} é um número primo')

    else:
        print(f'O numero {number} não é um número primo')

    print(f'Foram realizados {vezes} testes para o resultado')


num = int(input('Digite um número: '))

if ((num < 0) or (num == 1)):
    print(f'O número {num} não é um número válido')

else:
    validar_numeros_primos(num)

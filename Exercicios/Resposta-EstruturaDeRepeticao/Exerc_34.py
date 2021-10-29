# Os números primos possuem várias aplicações dentro da Computação, por exemplo na Criptografia. Um número primo é aquele
# que é divisível apenas por um e por ele mesmo. Faça um programa que peça um número inteiro e determine se ele é ou não um
# número primo..


def validar_numeros_primos(number):
    cont = 1
    for i in range(1, number):
        if (num % i == 0):
            cont += 1

    if (cont == 2):
        print(f'O numero {number} é um número primo')

    else:
        print(f'O numero {number} não é um número primo')


num = int(input('Digite um número: '))

if ((num < 0) or (num == 1)):
    print(f'O número {num} não é um número válido')

else:
    validar_numeros_primos(num)

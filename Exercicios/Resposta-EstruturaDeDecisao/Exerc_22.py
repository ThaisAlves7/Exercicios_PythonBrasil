# Faça um programa que peça um numero inteiro e determine se ele é par ou impar.
# Dica: utlize o operador de modulo(resto da divisão).


number = int(input('Digite um numero: '))
resto = number

resto = resto % 2
resto = int(resto)

if (resto == 1):
    print(f'O numero {number} é IMPAR')

elif (resto == 0):
    print(f'O numero {number} é PAR')

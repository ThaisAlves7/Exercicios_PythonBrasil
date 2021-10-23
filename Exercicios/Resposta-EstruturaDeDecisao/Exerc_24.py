# Faça um programa que leia 2 numeros e em seguida pergunte ao usuario qual operação ele deseja realizar. O resultado
# da operação deve ser acompanhado de uma frase que diga se o numero é:
    # A - Par ou Impar
    # B - Positvo ou Negativo
    # C - Inteiro ou Decimal

number = float(input('Digite um numero: '))
print('Escolha umas das opções para a operação:\n'
            '1 - Par ou Impar\n'
            '2 - Positivo ou Negativo\n'
            '3 - Inteiro ou Decimal')
opc = int(input())

if (opc == 1):
    resto = number
    resto = resto % 2
    resto = int(resto)

    if (resto == 1):
        print(f'O numero {number} é Impar')

    elif (resto == 0):
        print(f'O numero {number} é Par')

elif (opc == 2):
    if (number > 0):
        print(f'O numero {number} é Positivo')

    else:
        print(f'O numero {number} é Negativo')

elif (opc == 3):
    if (round(number) == number):
        print(f'O número {number} é um numero Inteiro')

    else:
        print(f'O número {number} é um numero Decimal')

else:
    print('Opção de menu inválida tente novamente')
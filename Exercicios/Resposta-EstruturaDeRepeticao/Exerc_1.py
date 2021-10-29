# Faça um programa que peça um nota entre Zero e Dez. Mostre uma mensagem caso o valor seja inválido e continue pedindo
    # até que o usuario informe um valor válido

number = int(input('Informe um número entre 0 e 10: '))
validar = True if ((number >= 0) and (number <= 10)) else False

while (validar == False):
    print()
    print(f'O número {number} - Informe um valor válido')
    number = int(input('Informe um número entre 0 e 10: '))
    validar = True if ((number >= 0) and (number <= 10)) else False

print()
print(f'O numero {number} é um número válido')
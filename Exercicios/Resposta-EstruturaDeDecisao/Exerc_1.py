# Faça um programa que peça dois numeros e imprima o maior deles

number1 = int(input('Insira um numero: '))
number2 = int(input('Insira outro numero: '))

if (number1 == number2):
    print('Por favor insira numeros diferentes')

elif (number1 > number2):
    print(f'O numero {number1} é maior que o numero {number2}')

else:
    print(f'O numero {number2} é maior que o numero {number1}')
# Faça um programa que peça 2 numeros inteiros e um numero real. Calcule e mostre:
    # A - O produto do dobro do primeiro com a metade do segundo
    # B - A soma do triplo do primeiro com o terceiro
    # C - O terceiro elevado ao cubo

number1 = int(input('Digite um numero: '))
number2 = int(input('Digite outro numero: '))
number3 = float(input('Digite um numero real: '))

a = (number1 * 2) + (number2 / 2)
b = (number1 * 3) + number3
c = number3 ** 3

print(f'O produto do dobro do primeiro com a metade do segundo é {a}')
print(f'A soma do triplo do primeiro com o terceiro é {b}')
print(f'O terceiro elevado ao cubo é {c}')
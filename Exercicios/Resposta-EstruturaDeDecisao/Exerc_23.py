# Faça um programa que peça um numero e informe se o numero é inteiro ou decimal. Dica: Utilize uma função de arrendondamento

number = float(input('Digite um numero: '))

if (round(number) == number):
    print(f'O número {number} é um numero inteiro')

else:
    print(f'O número {number} é um numero decimal')
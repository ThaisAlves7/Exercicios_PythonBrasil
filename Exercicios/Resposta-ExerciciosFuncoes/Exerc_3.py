# Faça um programa, com uma função que necessite de três argumentos, e que forneça a soma desses três argumentos.

def soma_valores(num_a, num_b, num_c):
    soma = num_a+num_b+num_c
    return print(f'A soma é {soma:.2f}')


a = float(input('Diga um numero para somar: '))
b = float(input('Diga outro um numero para somar: '))
c = float(input('Diga outro um numero para somar: '))

soma_valores(a, b, c)
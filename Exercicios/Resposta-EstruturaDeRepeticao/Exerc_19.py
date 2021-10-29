# Altere o programa anterior para que aceite numeros apanas entre 0 e 1000

valores = []
continuar = 1

while (continuar != 2):
    number = int(input('Entre com o numero um numero entre 0 e 1000: '))
    validar = True if ((number > 0) and (number < 1000)) else False
    while validar != True:
        print('Digite um numero entre 0 e 1000')
        number = int(input('Entre com o numero um numero entre 0 e 1000: '))
        validar = True if ((number > 0) and (number < 1000)) else False
    print()
    continuar = int(input('Deseja continuar digitando numeros?\n'
                          '1 - Sim ou 2 - Não: '))
    valores.append(number)
print()
print(f'O maior número é {max(valores)}')
print(f'O menor número é {min(valores)}')
print(f'A soma deles é {sum(valores)}')

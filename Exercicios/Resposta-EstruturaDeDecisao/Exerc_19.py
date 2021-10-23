# Faça um programa que leia um numero inteiro menor que 1000 e imprima a quantiade de centenas, dezenas e unidades do mesmo
# observando os termos no plural a colocado do "e", da virgula e outros. Exemplo:
    # 326 = 3 centenas, 2 dezenas e 6 unidades
    # 12 = 1 dezena e 2 unidades
    # Testar com 326, 300, 100, 320, 310,305, 301, 101, 311, 111, 25, 20, 10, 21, 11, 1, 7 e 16


num = int(input('Digite um numero menor que 1000: '))
number = list(str(num))
tamanho = len(number)

if (num > 1000):
    print('Digite um numero menor que 1000 u.u')

else:

    if (tamanho == 3):
        print(f'O numero {num} = {number[0]} centena, {number[1]} dezenas e {number[2]} unidades')

    elif (tamanho == 2):
        print(f'O numero {num} = {number[0]} dezenas e {number[1]} unidades')

    else:
        print(f'O numero {num} = {number[0]} unidades')


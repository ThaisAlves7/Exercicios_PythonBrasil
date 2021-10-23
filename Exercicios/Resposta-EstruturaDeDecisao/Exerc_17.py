# Faça um programa que peça um numero correspondente a um determinado ano e em seguida informe se este ano é ou não bissexto

from calendar import isleap

ano = int(input('Informe o ano: '))
bissexto = isleap(ano)

if (bissexto):
    print(f'O ano de {ano} é Bissexto')

else:
    print(f'O ano de {ano} não é Bissexto')
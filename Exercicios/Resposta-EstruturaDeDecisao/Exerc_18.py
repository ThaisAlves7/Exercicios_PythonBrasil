# Faça um programa que peça uma data no formato dd/mm/aaaa e determine se a mesma é uma data valida

from calendar import isleap

meses_31 = [1, 3, 5, 7, 8, 10, 12]
meses_30 = [4, 6, 9, 11]

data = input('Insira a data seguindo o padrão dd/mm/yyyy: ')

dia = int((data[0:2]))
mes = int((data[3:5]))
ano = int((data[6:]))
bissexto = isleap(ano)

if (len(str(ano)) > 4 ):
    print('Digite um ano válido')

else:
    if (bissexto):
        if mes in meses_31:
            if (dia <= 31):
                print(f'{data} é válida')
            else:
                print('Digite um dia válido')

        elif mes in meses_30:
            if (dia <= 30):
                print(f'{data} é válida')
            else:
                print('Digite um dia válido')

        elif ((mes == 2) and (dia <= 29)):
            print(f'{data} é válida')

        else:
            print('Digite um mês valido')

    else:
        if mes in meses_31:
            if (dia <= 31):
                print(f'{data} é válida')
            else:
                print('Digite um dia válido')

        elif mes in meses_30:
            if (dia <= 30):
                print(f'{data} é válida')
            else:
                print('Digite um dia válido')

        elif ((mes == 2) and (dia <= 28)):
            print(f'{data} é válida')

        else:
            print('Digite um mês válido')

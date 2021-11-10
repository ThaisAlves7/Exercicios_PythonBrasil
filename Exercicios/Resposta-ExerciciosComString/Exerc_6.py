# Data por extenso. Faça um programa que solicite a data de nascimento (dd/mm/aaaa) do usuário e imprima a data com o
# nome do mês por extenso.
        # Data de Nascimento: 29/10/1973
        # Você nasceu em 29 de Outubro de 1973.

from datetime import datetime

def validar_data(data_string):
    try:
        data_texto = datetime.strptime(data_string, '%d/%m/%Y')
        data_texto = data_texto.strftime('%d/%m/%Y')
        data_convertida = datetime.strptime(data_texto, '%d/%m/%Y')
        data_extenso = data_convertida.strftime('%d de %B de %Y')
        print(f'Data de Nascimento: {data_texto}')
        print(f'Você nasceu em {data_extenso}')
    except ValueError:
        raise ValueError("A data inserida é inválida")


print('Insira a Data em formato DD/MM/YYY')
data_nascimento = input('Informe sua data de nascimento: ')
validar_data(data_nascimento)

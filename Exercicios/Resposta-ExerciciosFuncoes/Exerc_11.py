# Data com mês por extenso. Construa uma função que receba uma data no formato DD/MM/AAAA e devolva uma string no
# formato D de mesPorExtenso de AAAA. Opcionalmente, valide a data e retorne NULL caso a data seja inválida.

#datetime.datetime.strptime(date_text, '%Y-%m-%d')

from datetime import datetime

def validar_data(data_string):
    try:
        data_texto = datetime.strptime(data_string, '%d/%m/%Y')
        data_texto = data_texto.strftime('%d/%m/%Y')
        data_convertida = datetime.strptime(data_texto, '%d/%m/%Y')
        data_extenso = data_convertida.strftime('%d %B, %Y')
        print(data_extenso)
    except ValueError:
        raise ValueError("A data inserida é inválida")



print('Insira uma data no formato DD/MM/AAAA')
data_informada = input('Informe a data: ')
validar_data(data_informada)



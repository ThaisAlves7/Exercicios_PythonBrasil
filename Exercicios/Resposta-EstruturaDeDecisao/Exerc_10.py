# Faça um programa que pergunte em que turno voce estuda. Peça para digitar M-Matutino ou V-Vespertino
# ou N-noturno. Imprima a mensagem "Bom dia!", "Boa Tarde!" ou "Boa Noite!" ou "Valor Inválido!". Conforme o caso

periodo = input('Digite o turno que voce estuda: M-Matutino, V-Vespertino ou N-Noturno: ').strip()
periodo = periodo.capitalize()

if ((periodo == 'M') or (periodo == 'Matutino')):
    print('Bom dia!')

elif ((periodo == 'V') or (periodo == 'Vespertino')):
    print('Boa Tarde!')

elif ((periodo == 'N') or (periodo == 'Noturno')):
    print('Boa Noite!')

else:
    print('Valor Inválido')

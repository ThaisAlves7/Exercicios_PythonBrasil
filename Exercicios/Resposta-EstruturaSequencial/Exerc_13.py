# Tendo como dado de entrada a altura (h) de uma pessoa, construa um algoritmo que calcule o peso ideal, utilizando
# as seguintes formulas:
    # A - Para homens: (72.7 * h) - 58
    # B - Para mulheres: (62.1 * h) - 44.7

sexo = input('Você é Masculino (M) ou Feminino (F): ')
sexo = sexo.capitalize()

h = float(input('Digite sua altura em metros: '))

if (sexo == 'M'):
    imc = (72.7 * h) - 58
    print(f'O seu IMC é: {imc:.2f}kg')

elif (sexo == 'F'):
    imc = (62.1 * h) - 44.7
    print(f'O seu IMC é: {imc:.2f}kg')

else:
    print('Informação inserida não atende aos requisitos por favor tente novamente')
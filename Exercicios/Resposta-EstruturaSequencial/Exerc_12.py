# Tendo como dados de entrada a altura de uma pessoa, construa um algoritmo que calcule seu peso ideal,
# usando a seguinte formula: (72.7 * altura) - 58

print('Calculo de IMC')

altura = float(input('Entre com sua altura em metros: '))

imc = (72.7 * altura) - 58

print(f'O seu IMC é: {imc:.2f}kg')
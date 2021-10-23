# Faça um programa que peça a temperatura em graus Fahrenheit, trasnforme e mostre a temperatura em graus Celsius.

print('Convertendo Fahrenheit em Celsius!!!')

f = float(input('Entre com a temperatura em Fahrenheit: '))
c = 5 * ((f-32) / 9)

print(f'A temperatura {f:.1f}°F é {c:.1f}°C')
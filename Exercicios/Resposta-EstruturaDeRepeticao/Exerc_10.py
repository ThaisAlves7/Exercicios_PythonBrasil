# Faça um program que receba 2 numeros inteiros e gere os numeros inteiros que estão no intervalo coompreendidos entre eles.

intervalo = []

number1 = int(input('Informe um numero: '))
number2 = int(input('Informe outro numero: '))
if (number1 < number2):
    inicio = number1
    final = number2

else:
    inicio = number2
    final = number1

for i in range(inicio, final):
    intervalo.append(i)

print(f'Os numeros entre o intervalo de {inicio} e {final} são: {intervalo}')
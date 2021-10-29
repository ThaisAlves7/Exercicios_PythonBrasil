# Altere o programa anterior paa mostrar no final a soma dos numeros

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

soma = sum(intervalo)
print(f'Os numeros entre o intervalo de {inicio} e {final} são: {intervalo}')
print(f'A soma dos valores no intervalo de {inicio} e {final} é {soma}')
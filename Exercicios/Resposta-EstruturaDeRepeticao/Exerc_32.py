# Faça um programa que calcule o fatorial de um número inteiro fornecido pelo usuário. Ex.: 5!=5.4.3.2.1=120. A saída deve ser
# conforme o exemplo abaixo:
    # Fatorial de: 5
    # 5! = 5 . 4 . 3 . 2 . 1 = 120

resultado = 1
number = []
num = int(input('Informe o número que sera usado na fatoração: '))
inicio = num

for i in range(inicio, 1, -1):
    resultado = resultado * i
    number.append(i)

frase = ''
for item in number:
    frase += f'{item} . '

print(f'Fatorial de: {num}!')
print(f'{num}! = {frase} 1 = {resultado}')
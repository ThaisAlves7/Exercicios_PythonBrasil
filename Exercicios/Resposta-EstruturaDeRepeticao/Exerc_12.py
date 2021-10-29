# Desenvolva um gerador de tabuada, capaz de gerar a tabuada de qualquer numero inteiro entre 1 a 10. O usuario deve informar
    # de qual numero ele deseja ver a tabuada. A Saida deve ser conforme o exemplo abaixo


valores = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

number = int(input('Informe um numero para calcular a tabuada entre 1 a 10: '))
print()
while number not in valores:
    print('Insira um valor valido')
    number = int(input('Informe um numero para calcular a tabuada entre 1 a 10: '))
print(f'Tabuada de {number}')
for i in range(len(valores)):
    print(f'{number} x {valores[i]} = {number * valores[i]}')
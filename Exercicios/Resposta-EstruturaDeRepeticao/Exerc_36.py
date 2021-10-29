#  Desenvolva um programa que faça a tabuada de um número qualquer inteiro que será digitado pelo usuário, mas a tabuada não
# deve necessariamente iniciar em 1 e terminar em 10, o valor inicial e final devem ser informados também pelo usuário, conforme
# exemplo abaixo:
    # Montar a tabuada de: 5
    # Começar por: 4
    # Terminar em: 7
    # Vou montar a tabuada de 5 começando em 4 e terminando em 7:
    # 5 X 4 = 20
    # 5 X 5 = 25
    # 5 X 6 = 30
    # 5 X 7 = 35

numero = int(input('Informe de qual numero voce quer a tabuada: '))
inicio = int(input('Informe de qual numero vai começar a tabuada: '))
final = int(input('Informe de qual numero vai terminar a tabuada: '))
print()
if final < inicio:
    print('Informe um final maior que o inicio')
else:
    print(f'Montar a tabuada de: {numero}')
    print(f'Começar por: {inicio}')
    print(f'Terminar em: {final}')
    print()
    print(f'Vou montar a tabuada de {numero} começando em {inicio} e terminando em {final}:')
    for i in range(inicio, final+1):
        print(f'{numero} X {i} = {numero * i}')
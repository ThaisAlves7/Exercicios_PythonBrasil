# Faça um programa que peça para n pessoas a sua idade, ao final o programa devera verificar se média de idade da turma varia entre 0 e 25,
    # 26 e 60 e maior que 60; e então dizer se a turma é jovem, adulta ou idosa , conforme a media calculada.

import numpy as np

continuar = 1
lista_idade = []

while continuar != 2:
    idade = int(input('Digite a sua idade: '))
    lista_idade.append(idade)
    print()
    continuar = int(input('Você deseja continuar: 1 - Sim ou 2 - Não: '))
    print()
    while continuar not in [1, 2]:
        print('Informe uma seleção valida para o menu')
        continuar = int(input('Você deseja continuar: 1 - Sim ou 2 - Não: '))
        print()

media = np.mean(lista_idade)

if ((media >= 0) and (media <= 25)):
    print(f'A média foi {media:.2f} - Turma Jovem')

elif ((media > 25) and (media < 60)):
    print(f'A média foi {media:.2f} - Turma Adulta')

else:
    print(f'A média foi {media:.2f} - Turma Idosa')



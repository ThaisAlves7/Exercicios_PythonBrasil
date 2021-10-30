# Faça um programa que leia um número indeterminado de valores, correspondentes a notas, encerrando a entrada de dados
# quando for informado um valor igual a -1 (que não deve ser armazenado). Após esta entrada de dados, faça:
    # a. Mostre a quantidade de valores que foram lidos;
    # b. Exiba todos os valores na ordem em que foram informados, um ao lado do outro;
    # c. Exiba todos os valores na ordem inversa à que foram informados, um abaixo do outro;
    # d. Calcule e mostre a soma dos valores;
    # e. Calcule e mostre a média dos valores;
    # f. Calcule e mostre a quantidade de valores acima da média calculada;
    # g. Calcule e mostre a quantidade de valores abaixo de sete;
    # h. Encerre o programa com uma mensagem;

import numpy as np

lista_numbers = []
num, cont, cont_acima, cont_abaixo = 1, 0, 0, 0

while num != -1:
    num = int(input('Informe um numero ou insira -1 para encerrar: '))
    condicao = num < 0 and num != -1

    while condicao == True:
        print()
        print('Insira o valor de -1 para encerrar')
        num = int(input('Informe um numero ou insira -1 para encerrar: '))
        condicao = num < 0 and num != -1
        print()
    if num != -1:
        lista_numbers.append(num)
        cont += 1
    else:
        print('Programa encerrado!!!!')
        print()

number_inversos = list(reversed(lista_numbers))
soma = sum(lista_numbers)
media = np.mean(lista_numbers)

print(f'O números inseridos foi {lista_numbers}')
print('Os valores na ordem inversa é ')
for num in number_inversos:
    print(num)
for valor in lista_numbers:
    if valor > media:
        cont_acima += 1

    if valor < 7:
        cont_abaixo += 1
print(f'A soma do numeros é {soma}')
print(f'A média do numeros é {media:.2f}')
print(f'A quantidade de numeros acima da média é {cont_acima}')
print(f'A quantidade de numeros abaixo de 7 é {cont_abaixo}')

# Faça um programa que leia um numero e exiba o dia correspondente da semana.(1-Domingo, 2-Segunda, etc.), se digitar outro
# valor deve aparecer valor inválido.

semana = ['Domingo', 'Segunda', 'Terça', 'Quarta', 'Quinta', 'Sexta']
# 0 - 5

number = int(input('Insira um numero entre 0 a 5: '))
tamanho = len(semana) - 1

if (number > tamanho):
    print('Informe um numero válido para a realização da pesquisa')

elif (number < 0):
    print('Informe um numero válido para a realização da pesquisa')

else:
    print(f'O numero escolhido se refere a {semana[number]}')


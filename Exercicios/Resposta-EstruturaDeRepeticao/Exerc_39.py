#  Faça um programa que leia dez conjuntos de dois valores, o primeiro representando o número do aluno e o segundo
# representando a sua altura em centímetros. Encontre o aluno mais alto e o mais baixo. Mostre o número do aluno mais alto e o
# número do aluno mais baixo, junto com suas alturas.

# Uma academia deseja fazer um senso entre seus clientes para descobrir o mais alto, o mais baixo, a mais gordo e o mais magro,
    # para isto você deve fazer um programa que pergunte a cada um dos clientes da academia seu código, sua altura e seu peso. O final
    # da digitação de dados deve ser dada quando o usuário digitar 0 (zero) no campo código. Ao encerrar o programa também
    # deve ser informados os códigos e valores do clente mais alto, do mais baixo, do mais gordo e do mais magro, além da média das
    # alturas e dos pesos dos clientes

import numpy as np

lista_codigo, lista_altura = [], []

mais_alto = mais_baixo = None

for i in range(1, 11):
    codigo = input('Informe seu código do Aluno: ')
    lista_codigo.append(codigo)
    altura = int(input('Informe sua Altura em cm: '))
    lista_altura.append(altura)
    print()


#Altura
for index, valor in enumerate(lista_altura):
    if (mais_alto is None) or (valor > mais_alto):
        mais_alto = valor
        index_alto = index

    if (mais_baixo is None) or (valor < mais_baixo):
        mais_baixo = valor
        index_baixo = index

print()
print(f'O Mais Alto é Cliente de Codigo: {lista_codigo[index_alto]}: {lista_altura[index_alto]} Altura')
print(f'O Mais Baixo é Cliente de Codigo: {lista_codigo[index_baixo]}: {lista_altura[index_baixo]} Altura')


# Uma academia deseja fazer um senso entre seus clientes para descobrir o mais alto, o mais baixo, a mais gordo e o mais magro,
    # para isto você deve fazer um programa que pergunte a cada um dos clientes da academia seu código, sua altura e seu peso. O final
    # da digitação de dados deve ser dada quando o usuário digitar 0 (zero) no campo código. Ao encerrar o programa também
    # deve ser informados os códigos e valores do clente mais alto, do mais baixo, do mais gordo e do mais magro, além da média das
    # alturas e dos pesos dos clientes

import numpy as np

lista_codigo, lista_altura, lista_peso = [], [], []
continuar = 1

mais_alto = mais_baixo = mais_gordo = mais_magro = None

while continuar != 0:
    codigo = input('Informe seu código na Academia: ')
    lista_codigo.append(codigo)

    altura = int(input('Informe sua Altura em cm: '))
    lista_altura.append(altura)

    peso = float(input('Informe seu Peso: '))
    lista_peso.append(peso)
    print()

    continuar = int(input('Deseja continuar 1 - Sim ou 0 - Não: '))
#Altura
for index, valor in enumerate(lista_altura):
    if (mais_alto is None) or (valor > mais_alto):
        mais_alto = valor
        index_alto = index

    if (mais_baixo is None) or (valor < mais_baixo):
        mais_baixo = valor
        index_baixo = index

#Peso
for index, valor in enumerate(lista_peso):
    if (mais_gordo is None) or (valor > mais_gordo):
        mais_gordo = valor
        index_gordo = index

    if (mais_magro is None) or (valor < mais_magro):
        mais_magro = valor
        index_magro = index

media_peso = np.mean(lista_peso)
media_altura = np.mean(lista_altura)
print()
print(f'O Mais Alto é Cliente de Codigo: {lista_codigo[index_alto]}: {lista_altura[index_alto]} Altura - {lista_peso[index_alto]:.2f}Kg')
print(f'O Mais Baixo é Cliente de Codigo: {lista_codigo[index_baixo]}: {lista_altura[index_baixo]} Altura - {lista_peso[index_baixo]}Kg')
print(f'O Mais Magro é Cliente de Codigo: {lista_codigo[index_magro]}: {lista_altura[index_magro]} Altura - {lista_peso[index_magro]:.2f}Kg')
print(f'O Mais Gordo é Cliente de Codigo: {lista_codigo[index_gordo]}: {lista_altura[index_gordo]} Altura - {lista_peso[index_gordo]:.2f}Kg')
print()
print(f'O Media de Altura: {media_altura:.2f} Altura')
print(f'O Media de Peso: {media_peso:.2f}Kg')

# Foram anotadas as idades e alturas de 30 alunos. Faça um Programa que determine quantos alunos com mais de 13 anos
# possuem altura inferior à média de altura desses alunos.

import numpy as np

lista_idade, lista_altura = [], []
cont = 0

for i in range(1, 31):
    idade = int(input('Informe a idade: '))
    lista_idade.append(idade)

    altura = int(input('Informe sua idade em centimetros: '))
    lista_altura.append(altura)
    print()

media = np.mean(lista_altura)
print(media)

for idade, altura in zip(lista_idade, lista_altura):
    if idade > 13 and altura < media:
        cont += 1

print(f'A quantidade de crianças com mais de 13 anos com altura menor que a média é {cont}')
# Faça um programa que programa que calcule o numero médio de alunos por turma. Para isto, peça a quantidade de turmas e a
    # a quantidade de alunos por turmas. As turmas não podem ter mais de 40 alunos.

import numpy as np

qtde_alunos = []

turmas = int(input('Informe a quantidade de turmas: '))
tamanho = turmas + 1

for i in range(1, tamanho):
    alunos = int(input(f'Informe a quantidade de alunos entre 0 a 40 da {i}° turma: '))
    condicao = alunos <= 40

    while not condicao:
        print('Informe uma quantidade valida entre 0 a 40')
        alunos = int(input(f'Informe a quantidade de alunos da {i}° turma: '))
        condicao = alunos <= 40

    qtde_alunos.append(alunos)
media = np.mean(qtde_alunos)

print(f'A média de aluno entre as {turmas} é {media:.2f}')

# Faça um Programa que peça as quatro notas de 10 alunos, calcule e armazene num vetor a média de cada aluno, imprima o
# número de alunos com média maior ou igual a 7.0.

lista_medias = []
soma, media, cont = 0, 1, 0


for x in range(1, 11):
    print(f'Informe a nota do {x}° Aluno')
    for y in range(1, 5):
        nota = float(input(f'Informe a {y}° Nota: '))
        soma += nota
    media = soma / 4
    lista_medias.append(media)
    if media >= 7:
        cont += 1
    print()

print(f'A quantidade de Alunos com média maior ou igual a 7 é: {cont}')
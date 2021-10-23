# Faça um programa que lê as duas notas parciais obtidas por um aluno numa disciplina ao longo de um semestre, calcule a sua média.
# A atribuição de conceitos obedece á tabela abaixo:
    # Média de Aproveitamento Conceito      Conceito
        # Entre 9.0 e 10.0                      A
        # Entre 7.5 e 9.0                       B
        # Entre 6.0 e 7.5                       C
        # Entre 4.0 e  6.0                      D
        # Entre 4.0 e zero                      E
# O Algortimo deve mostrar na tela as notas, a media, o conceito correspondente e a mensagem "APROVADO"  se o coneceito for A,B ou C
# "REPROVADO" se o conceito for D ou E

nota_1 = float(input('Informe a 1° nota: '))
nota_2 = float(input('Informe a 2° nota: '))

media = (nota_1 + nota_2) / 2

if (media < 4.0):
    print(f'As notas do aluno foi: {nota_1} e {nota_2}')
    print(f'A média dele foi: {media} - Você fico com E')
    print(f'Ele foi REPROVADO')

elif ((media >= 4.0) and (media < 6.0)):
    print(f'As notas do aluno foi: {nota_1} e {nota_2}')
    print(f'A média dele foi: {media} - Você fico com D')
    print(f'Ele foi REPROVADO')


elif ((media >= 6.0) and (media < 7.5)):
    print(f'As notas do aluno foi: {nota_1} e {nota_2}')
    print(f'A média dele foi: {media} - Você fico com C')
    print(f'Ele foi APROVADO')

elif ((media >= 7.5) and (media < 9.0)):
    print(f'As notas do aluno foi: {nota_1} e {nota_2}')
    print(f'A média dele foi: {media} - Você fico com B')
    print(f'Ele foi APROVADO')

else:
    print(f'As notas do aluno foi: {nota_1} e {nota_2}')
    print(f'A média dele foi: {media} - Você fico com A')
    print(f'Ele foi APROVADO')
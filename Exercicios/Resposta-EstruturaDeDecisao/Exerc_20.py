# Faça um programa para leitura de 3 notas parcias de um aluno. O programa deve calcular a média alcançada por aluno e presentear:
    # A - A mensagem "Aprovado", se a média for maior ou igual a 7, com a respectiva média alcançada
    # B - A mensagem "Reprovado", se a média for menor 7, com a respectiva média alcançada
    # C - A mensagem "Aprovado com Distinção", se a média for igual a 10

divisor = 3
media = 0
for i in range(1, 4):
    nota = float(input(f'Digite a {i}° nota: '))
    media += nota

media = media / divisor

if (media == 10):
    print(f'Media de {media:.2f} - Aprovado com Distinção')

elif (media >= 7):
    print(f'Media de {media:.2f} - Aprovado')

else:
    print(f'Media de {media:.2f} - Reprovado')
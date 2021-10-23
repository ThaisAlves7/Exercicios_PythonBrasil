# Faça um programa que para a leitura de duas notas parcias de um aluno. O programa deve calcular a média
# alcançada por aluno e apresentar:
    # A mensagem "Aprovado", se a média alcançada for maior que ou igual a sete
    # A mensagem "Reprovado", se a média for menor do que sete
    # A mensagem "Aprovado com Distinção", se a média for igual a dez

nota_1 = float(input('Digite a 1° nota: '))
nota_2 = float(input('Digite a 2° nota: '))
media = (nota_1 + nota_2) / 2

if (media == 10):
    print(f'Media de {media:.2f} - Aprovado com Distinção')

elif (media >= 7):
    print(f'Media de {media:.2f} - Aprovado')

else:
    print(f'Media de {media:.2f} - Reprovado')
# Faça um programa que pergunte quanto voce ganha por hora e o numero de horas trabalhadas no mês,
# Calcule e mostre o total do seu salario no referido mes

ganho_hora = float(input('Digite quanto você ganha por hora: '))
horas_trabalhadas = float(input('Digite total de horas trabalhadas: '))

salario = ganho_hora * horas_trabalhadas

print(f'O seu salario do mês é R$ {salario:.2f} reais')
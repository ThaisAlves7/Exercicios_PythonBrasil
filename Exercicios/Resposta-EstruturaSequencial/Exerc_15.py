#Faça um programa que pergunte quanto você ganha por hora e o numero de horas trabalhadas no mês.
    #Calcule e mostre o total do seu salario referido do mês, sabendo que são descontados:
        # 11% para o Imposto de Renda
        # 8% para o INSS
        # 5% para o sindicato
    #Faça um programa que nos dê:
        # A - Salario Bruto
        # B - Quanto pagou de INSS
        # C - Quanto pagou ao sindicato
        # D - O Salario Liquido
        # E - Calcule os descontos e salario liquido, conforme a tabela a abaixo:
#OBS: Salario Bruto - Descontos = Salario liquido

ganho_hora = float(input('Digite quanto você ganha por hora: '))
horas_trabalhadas = float(input('Quantas horas você trabalhou no mês: '))

salario_bruto = ganho_hora * horas_trabalhadas

ir = (salario_bruto * 11) / 100
inss = (salario_bruto * 8) / 100
sindico = (salario_bruto * 5) / 100
descontos = ir + inss + sindico
salario_liquido = salario_bruto - descontos

print(f'Salário Bruto: R${salario_bruto:.2f}')
print(f'IR (11%): R${ir:.2f}')
print(f'INSS (8%): R${inss:.2f}')
print(f'Sindicato: R${sindico:.2f}')
print(f'O Salário Liquido: R${salario_liquido:.2f}')
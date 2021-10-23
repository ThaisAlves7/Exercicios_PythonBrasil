# As Organizações Tabajaras resolveram dar um aumento de salario aos seus colaboradores e lhe contrataram
# para desenvolver o programa que calculara os reajustes.
# Faça um programa que recebe o salario de um colaborador e o reajuste segundo o seguinte criterio, baseado no salario atual
    # Salario ate R$ 280,00 (incluido): aumento de 20%
    # Salario entre R$280,00 e R$ 700,00: aumento de 15%
    # Salario entre R$ 700,00 e R$ 1500,00: aumento de 10%
    # Salario de R$ 1500,00 em diante: aumento de 5%
    # Apos o aumento realizado, informe na tela
        # O Salario antes do reajuste
        # O percentual de aumento aplicado
        # O valor do aumento
        # O novo Salario, apos o aumento


porcentual_1 = 20
porcentual_2 = 15
porcentual_3 = 10
porcentual_4 = 5

salario = float(input('Informe o salário do colaborador: '))

if (salario <= 280.00):
    aumento = (salario * porcentual_1) / 100
    novo_salario = salario + aumento
    porcentual_usado = porcentual_1

elif ((salario > 280.01) and (salario <= 700)):
    aumento = (salario * porcentual_2) / 100
    novo_salario = salario + aumento
    porcentual_usado = porcentual_2

elif ((salario > 700.01) and (salario <= 1500)):
    aumento = (salario * porcentual_3) / 100
    novo_salario = salario + aumento
    porcentual_usado = porcentual_3

else:
    aumento = (salario * porcentual_4) / 100
    novo_salario = salario + aumento
    porcentual_usado = porcentual_4

print(f'O antigo Salário é: R$ {salario:.2f}')
print(f'O porcentual utilizado para o reajuste foi: {porcentual_usado}')
print(f'O valor de aumento adicionado foi: R$ {aumento:.2f}')
print(f'O novo Salário é: R$ {novo_salario:.2f}')
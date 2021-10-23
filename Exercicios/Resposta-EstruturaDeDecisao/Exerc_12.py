# Faça um programa para o calculo de folha de pagamento, sabendo que os descontos são do Impostos de Renda, que depende do Salario Bruto
# (conforme tabela abaixao) e 3% para o Sindicato e que o FGTS corresponde a 11% do Salario Bruto, mas não é descontado (é a empresa que deposita).
# O Salario Liquido corresponde ao Salario Bruto menos os descontos. O programa devera pedir ao usuario o valor da sua hora e a quantidade de horas
# no mês
    # Desconto do IR:
        # O Salario até 900(inclusive) - isento
        # Salario Bruto ate 1500(inclusive)- descontos de 5%
        # Salario Bruto ate 2500(inclusive) - descontos de 10%
        # Salario Bruto aima de 2500 - descontos de 20%
    # Imprima na tela as informações, dispostas conforme o exemplo abaixo.
        # No exemplo o valor de hora é 5 e a quantidade de hora é 220.
            # Salario Bruto: (5 * 220)      :R$ 1100,00
            # IR (5%)                       :R$   55,00
            # INSS: (10%)                   :R$  110,00
            # FGTS (11%)                    :R$  121,00
            # Total de descontos            :R$  165,00
            # Salario Liquido               :R$  935,00

ir_1 = 5
ir_2 = 10
ir_3 = 20

valor_hora = float(input('Informe o valor da sua hora trabalhada R$ '))
hora_trabalhada = float(input('Informe suas horas trabalhadas: '))

salario_bruto = hora_trabalhada * valor_hora

if (salario_bruto <= 900):
    ir = ir_custo = 0
    inss = (salario_bruto * 10) / 100
    fgts = (salario_bruto * 11) / 100
    total_descontos = inss
    salario_liquido = salario_bruto - total_descontos

elif (salario_bruto <= 1500):
    ir = ir_1
    ir_custo = (salario_bruto * ir_1) / 100
    inss = (salario_bruto * 10) / 100
    fgts = (salario_bruto * 11) / 100
    total_descontos = ir_custo + inss
    salario_liquido = salario_bruto - total_descontos

elif (salario_bruto <= 2500):
    ir = ir_2
    ir_custo = (salario_bruto * ir_2) / 100
    inss = (salario_bruto * 10) / 100
    fgts = (salario_bruto * 11) / 100
    total_descontos = ir_custo + inss
    salario_liquido = salario_bruto - total_descontos

else:
    ir = ir_3
    ir_custo = (salario_bruto * ir_3) / 100
    inss = (salario_bruto * 10) / 100
    fgts = (salario_bruto * 11) / 100
    total_descontos = ir_custo + inss
    salario_liquido = salario_bruto - total_descontos


print(f'Salario Bruto: ({hora_trabalhada} * {valor_hora})      :R$   {salario_bruto}')
print(f'IR ({ir}%)                                             :R$   {ir_custo}')
print(f'INSS: (10%)                                            :R$   {inss}')
print(f'FGTS (11%)                                             :R$   {fgts}')
print(f'Total de descontos                                     :R$   {total_descontos}')
print(f'Salario Liquido                                        :R$   {salario_liquido}')
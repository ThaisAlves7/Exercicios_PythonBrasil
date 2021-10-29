# Um funcionário de uma empresa recebe aumento salarial anualmente: Sabe-se que:
    # a. Esse funcionário foi contratado em 1995, com salário inicial de R$ 1.000,00;
    # b. Em 1996 recebeu aumento de 1,5% sobre seu salário inicial;
    # c. A partir de 1997 (inclusive), os aumentos salariais sempre correspondem ao dobro do percentual do ano anterior. Faça
# um programa que determine o salário atual desse funcionário. Após concluir isto, altere o programa permitindo que o
# usuário digite o salário inicial do funcionário.

import datetime

def resposta_a_b(valor):

    data_atual = datetime.datetime.now()
    ano_atual = data_atual.year

    if valor is None:
        salario = 1000.00
    else:
        salario = valor

    ano_contratacao = 1995
    porc_aumento = 1.5

    porc_atual_aumento = (ano_atual - (ano_contratacao + 1)) * porc_aumento

    salario_96 = salario + ((salario * porc_aumento) / 100)

    salario_atual = salario_96 + ((salario_96 * porc_atual_aumento) / 100)

    print(f'O salario atual é {salario_atual:.2f}')

resposta_a_b(1500)
# resposta_a_b(None)


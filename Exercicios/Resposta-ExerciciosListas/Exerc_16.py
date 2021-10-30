# Utilize uma lista para resolver o problema a seguir. Uma empresa paga seus vendedores com base em comissões. O vendedor
# recebe $200 por semana mais 9 por cento de suas vendas brutas daquela semana. Por exemplo, um vendedor que teve vendas
# brutas de $3000 em uma semana recebe $200 mais 9 por cento de $3000, ou seja, um total de $470. Escreva um programa
# (usando um array de contadores) que determine quantos vendedores receberam salários nos seguintes intervalos de valores:
    # a. $200 - $299
    # b. $300 - $399
    # c. $400 - $499
    # d. $500 - $599
    # e. $600 - $699
    # f. $700 - $799
    # g. $800 - $899
    # h. $900 - $999
    # i. $1000 em diante
# Desafio: Crie ma fórmula para chegar na posição da lista a partir do salário, sem fazer vários ifs aninhados

list_contador = [0, 0, 0, 0, 0, 0, 0, 0, 0]
entrada = 1

def atualizar_lista(posicao):
    contador = list_contador[posicao]
    contador += 1
    del (list_contador[posicao])
    list_contador.insert(posicao, contador)

while entrada == 1:
    valor_vendas = float(input('Informe o salário do funcionário R$ '))
    comissao = 200 + ((valor_vendas * 9) / 100)
    print()
    while entrada not in [1, 2]:
        print('Insira uma entrada válida')
        entrada = int(input('Deseja continuar? 1 - Sim ou 2 - Não: '))

    if comissao < 299:
        atualizar_lista(0)

    elif comissao < 399:
        atualizar_lista(1)

    elif comissao < 499:
        atualizar_lista(2)

    elif comissao < 599:
        atualizar_lista(3)

    elif comissao < 699:
        atualizar_lista(4)

    elif comissao < 799:
        atualizar_lista(5)

    elif comissao < 899:
        atualizar_lista(6)

    elif comissao < 999:
        atualizar_lista(7)

    else:
        atualizar_lista(8)

    entrada = int(input('Deseja continuar? 1 - Sim ou 2 - Não: '))

print(list_contador)
print(f'Funcionario com na seguinte faixa $200 - $299 é: {list_contador[0]}')
print(f'Funcionario com na seguinte faixa $300 - $399 é: {list_contador[1]}')
print(f'Funcionario com na seguinte faixa $400 - $499 é: {list_contador[2]}')
print(f'Funcionario com na seguinte faixa $500 - $599 é: {list_contador[3]}')
print(f'Funcionario com na seguinte faixa $600 - $699 é: {list_contador[4]}')
print(f'Funcionario com na seguinte faixa $700 - $799 é: {list_contador[5]}')
print(f'Funcionario com na seguinte faixa $800 - $899 é: {list_contador[6]}')
print(f'Funcionario com na seguinte faixa $900 - $999 é: {list_contador[7]}')
print(f'Funcionario com na seguinte faixa $1000 em diante é: {list_contador[8]}')


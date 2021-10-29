# Faça um programa que receba o valor de uma dívida e mostre uma tabela com os seguintes dados: valor da dívida, valor dos
# juros, quantidade de parcelas e valor da parcela.
# Os juros e a quantidade de parcelas seguem a tabela abaixo:
    # Quantidade de Parcelas % de Juros sobre o valor inicial da dívida
    # 1 0
    # 3 10
    # 6 15
    # 9 20
    # 12 25
# Exemplo de saída do programa:
    # Valor da Dívida Valor dos Juros Quantidade de Parcelas Valor da Parcela
    # R$ 1.000,00 0 1 R$ 1.000,00
    # R$ 1.100,00 100 3 R$ 366,00
    # R$ 1.150,00 150 6 R$ 191,67

def tabela_parcelas(divida):
    parcelas = 3
    porcentagem = 10
    print('Tabela de Valores de Parcela do Empréstimo')
    print()
    print('Valor da Divida\t\tValor dos Juros\t\tQuantidade de Parcelas\t\tValor da Parcela')
    print('R$ %2.2f\t\t\t\t%d\t\t\t\t\t\t%d\t\t\t\t\tR$ %2.2f' % (valor_divida, 0, 1, divida))
    while parcelas < 13:

        valor_final = divida + ((divida * porcentagem) / 100)
        juros = valor_final - divida
        valor_parcelas = valor_final / parcelas

        print('R$ %2.2f\t\t\t\t%d\t\t\t\t\t\t%d\t\t\t\t\tR$ %2.2f' % (valor_final, juros, parcelas, valor_parcelas))
        parcelas += 3
        porcentagem += 5

valor_divida = float(input('Informe valor da dívida R$ '))
tabela_parcelas(valor_divida)
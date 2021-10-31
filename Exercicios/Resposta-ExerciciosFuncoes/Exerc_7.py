#  Faça um programa que use a função valorPagamento para determinar o valor a ser pago por uma prestação de uma conta. O
# programa deverá solicitar ao usuário o valor da prestação e o número de dias em atraso e passar estes valores para a função
# valorPagamento, que calculará o valor a ser pago e devolverá este valor ao programa que a chamou. O programa deverá então
# exibir o valor a ser pago na tela. Após a execução o programa deverá voltar a pedir outro valor de prestação e assim continuar
# até que seja informado um valor igual a zero para a prestação. Neste momento o programa deverá ser encerrado,
# exibindo o relatório do dia, que conterá a quantidade e o valor total de prestações pagas no dia. O cálculo do valor a ser pago é feito da
# seguinte forma. Para pagamentos sem atraso, cobrar o valor da prestação. Quando houver atraso, cobrar 3% de multa, mais 0,1%
# de juros por dia de atraso


def valorPagamento(valor, dias_atraso):
    multa, juros = 3, 0.1

    juros_total = multa + (dias_atraso * juros)

    valor_ajustado = valor + ((valor * juros_total) / 100)
    valor_ajustado = round(valor_ajustado, 2)
    relatorio.append(valor_ajustado)
    print(f'O valor atual com atraso é R$ {valor_ajustado}')


valor_parcela = 1
relatorio = []

while valor_parcela != 0:
    valor_parcela = float(input('Informe o valor parcela ou 0 para encerrar: R$ '))
    if valor_parcela > 0:
        dia = int(input('Informe quantidade de dias em atraso: '))
        valorPagamento(valor_parcela, dia)
    print()

print(f'A quantidade de prestações pagas foram {len(relatorio)}')
for valor in relatorio:
    print(f'Os o valores pagos foram R$ {valor}')
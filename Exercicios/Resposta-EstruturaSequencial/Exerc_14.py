# João Papo-de-Pescador, homem de bem, comprou  um microcomputador para controlar o rendimento diario de seu
    # trabalho. Toda vez que ele traz um peso de peixes maior que o estabelecido pelo regulamento do estado de São Paulo
    # (50 kilos) deve pagar uma multa de R$4,00 por kilo excendente. João precisa que voce faça um programa que leia
    # a variavel de peso (peso do peixe) e calcule o excesso. Grava na variavel excesso a quantidade de quilos além
    # do limite e na variavel multa o valor de multa que João devera pagar. Imprima os dados do programa com as mensagens adequadas.

print('Calcular excesso de peso e valor de multa do Peixe')

multa = 4.00
kilo = 50.00

peso = float(input('Digite o peso do Peixe que foi pescado: '))

excesso = peso - kilo

if (excesso > 0):
    valor_multa = excesso * multa
    print(f'O peixe pescado passou {excesso:.2f}kg do permitido')
    print(f'O valor da multa a ser pago é R${valor_multa:.2f} reais')


else:
    print('Dentro da regulamentação')

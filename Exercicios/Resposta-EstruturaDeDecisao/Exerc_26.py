# Um posto está vendendo combustíveis com a seguinte tabela de descontos:
    # A - Álcool:
        # Ate 20 litros, desconto de 3% por litro
        # Acima de 20 litros, desconto de 5% por litro
    # B - Gasolina:
        # Ate 20 litros, desconto de 4% por litro
        # Acima de 20 litros, desconto de 6% litros.
    # Escreva um algoritmo que leia o numero de litros vendidos, o tipo de combustivel(codificado da seguinte forma:
        # A-álcool e G-gasolina), calcule e imprima o valor pago pelo cliente sabendo que o preço do litro da gasolina é
        # R$2,50 e o preço do litro do álcool é R$ 1,90.

preco_gasolina = 2.50
preco_alcool = 1.90

tipo = input('Qual a gasolina voce ira abastecer? A-álcool e G-gasolina: ').strip()
tipo = tipo.capitalize()

while (tipo not in ['A', 'G']):
    tipo = input('Qual a gasolina voce ira abastecer? A-álcool e G-gasolina: ').strip()
    tipo = tipo.capitalize()

litros = float(input('Informe quantos litros você ira abastecer: '))

if (tipo == 'A'):
    if (litros <= 20):
        valor_pagar = preco_alcool - ((litros * 3) / 100)

    else:
        valor_pagar = preco_alcool - ((litros * 5) / 100)

    print(f'Você abasteceu {litros} dando um total a pagar de R$ {valor_pagar:.2f}')

else:
    if (litros <= 20):
        valor_pagar = preco_gasolina - ((litros * 4) / 100)

    else:
        valor_pagar = preco_gasolina - ((litros * 6) / 100)

    print(f'Você abasteceu {litros} dando um total a pagar de R$ {valor_pagar:.2f}')
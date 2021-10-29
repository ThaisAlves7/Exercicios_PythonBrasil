#  O cardápio de uma lanchonete é o seguinte:
    # Especificação     Código      Preço
    # Cachorro Quente   100         R$ 1,20
    # Bauru Simples     101         R$ 1,30
    # Bauru com ovo     102         R$ 1,50
    # Hambúrguer        103         R$ 1,20
    # Cheeseburguer     104         R$ 1,30
    # Refrigerante      105         R$ 1,00
# Faça um programa que leia o código dos itens pedidos e as quantidades desejadas. Calcule e mostre o valor a ser pago
# por item (preço * quantidade) e o total geral do pedido. Considere que o cliente deve informar quando o pedido deve
# ser encerrado.

cardapio = {100: 'Cachorro Quente', 101: 'Bauru Simples', 102: 'Bauru com Ovo', 103: 'Hámburguer    ', 104: 'Cheeseburguer', 105: 'Refrigerante    '}
preco = {100: 1.20, 101: 1.30, 102: 1.50, 103: 1.20, 104: 1.30, 105: 1.00}
encerrar = 1
pedido = {100: 3, 103: 5}

print('Cardápio Bom Apetite - Tabela de Preços')
print()
for key, valor in cardapio.items():
    print(f'Tipo: {valor} \t\t- Código: {key}  \t\t- Preço: {preco[key]:.2f}')
print()

while encerrar != -1:
    codigo = int(input('Informe o codigo do pedido que voce deseja: '))

    while codigo not in cardapio.keys():
        print()
        print('Informe um código valido, verifique corretamente o cardapio')
        codigo = int(input('Informe o codigo do pedido que voce deseja: '))
        print()

    qtde = int(input('Informe a quantidade do pedido: '))
    pedido.update({codigo: qtde})
    encerrar = int(input('Deseja encerrar? Digite -1: '))
    while encerrar > 0:
        print()
        print('Insira um valor negativo para encerrar o pedido')
        encerrar = int(input('Deseja encerrar? Digite -1: '))
        print()

for key, valor in pedido.items():

    valor_pagar = preco[key] * valor
    print(f'Tipo: {cardapio[key]} \t- Quantidade: {valor} \t- Total a Pagar: R$ {valor_pagar:.2f}')



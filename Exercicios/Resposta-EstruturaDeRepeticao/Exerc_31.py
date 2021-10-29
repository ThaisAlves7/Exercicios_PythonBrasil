# O Sr. Manoel Joaquim expandiu seus negócios para além dos negócios de 1,99 e agora possui uma loja de conveniências. Faça
    # um programa que implemente uma caixa registradora rudimentar. O programa deverá receber um número desconhecido de
    # valores referentes aos preços das mercadorias. Um valor zero deve ser informado pelo operador para indicar o final da compra. O
    # programa deve então mostrar o total da compra e perguntar o valor em dinheiro que o cliente forneceu, para então calcular e
    # mostrar o valor do troco. Após esta operação, o programa deverá voltar ao ponto inicial, para registrar a próxima compra. A
    # saída deve ser conforme o exemplo abaixo:
        # Lojas Tabajara
            # Produto 1: R$ 2.20
            # Produto 2: R$ 5.80
            # Produto 3: R$ 0
            # Total: R$ 9.00
            # Dinheiro: R$ 20.00
            # Troco: R$ 11.00
            # ...

valores = []
valor = cont = 1

while valor != 0:
    valor = float(input(f'Informe o valor do {cont}° produto ou 0 para finalizar a compra R$ '))
    if valor != 0:
        valores.append(valor)
    cont += 1

print()
dinheiro = float(input('Informe o valor pago pelo cliente R$ '))
print()

cont = 1
print('Lojas Tabajaras')
for valor in valores:
    print(f'Produto {cont}: R${valor:.2f}')
    cont += 1

total = sum(valores)
troco = dinheiro - total

print(f'Total: R${total:.2f}')
print(f'Dinheiro: R${dinheiro:.2f}')
print(f'Troco: R${troco:.2f}')

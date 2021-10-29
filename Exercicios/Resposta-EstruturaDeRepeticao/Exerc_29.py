# O Sr. Manoel Joaquim possui uma grande loja de arqtigos pde R$1.99, com cerca de 10 caixas. Para agilizar o calulco de
    # de quanto cada cliente deve pagar ele desenvolveu um atbaela que contém o numero de itens de que o cliente comprou
    # e ao lado o valor da conta. Desta forma atendente do caixa precisa apenas contar quantos itens o cliente esta levando
    # e olhar a na tabela de preços. Voceê foi contratado para desenvolver o prograna qye nibta esta tabela de preços, que conterá
    #  os preços de 1 ate 50 produtos, conforme o exemplo abaixo:
    # Loja de Quase Dois - Tabela de Preços
        # 1 - R$1.99
        # 2 - R$3.98
        # ......
        # 50 - R$99.50

preco = 1.99

print('Loja de Quase Dois - Tabela de Preços')

for i in range(1, 51):
    print(f'Quantidade {i} - Preço R${i*preco:.2f}')
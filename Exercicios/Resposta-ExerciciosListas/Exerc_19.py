# Uma empresa de pesquisas precisa tabular os resultados da seguinte enquete feita a um grande quantidade de organizações:

# "Qual o melhor Sistema Operacional para uso em servidores?"
# As possíveis respostas são:
    # 1- Windows Server
    # 2- Unix
    # 3- Linux4- Netware
    # 5- Mac OS
    # 6- Outro
# Você foi contratado para desenvolver um programa que leia o resultado da enquete e informe ao final o resultado da mesma. O
# programa deverá ler os valores até ser informado o valor 0, que encerra a entrada dos dados. Não deverão ser aceitos valores
# além dos válidos para o programa (0 a 6). Os valores referentes a cada uma das opções devem ser armazenados num vetor. Após
# os dados terem sido completamente informados, o programa deverá calcular a percentual de cada um dos concorrentes e
# informar o vencedor da enquete. O formato da saída foi dado pela empresa, e é o seguinte:

# Sistema Operacional   Votos   %
# ------------------- ----- ---
# Windows Server        1500    17%
# Unix                  3500    40%
# Linux                 3000    34%
# Netware                500     5%
# Mac OS                 150     2%
# Outro                  150     2%
# ------------------- ------
# Total                 8800
# O Sistema Operacional mais votado foi o Unix, com 3500 votos, correspondendo a 40% dos
# votos.


def atualizar_lista(posicao):
    contador = lista_contador[posicao]
    contador += 1
    del (lista_contador[posicao])
    lista_contador.insert(posicao, contador)


lista_votacao = [0, 1, 2, 3, 4, 5, 6]
sistemas_operacionais = ['', 'Windows Server ', 'Unix        ', 'Linux        ', 'Netware      ', 'Mac OS      ', 'Outros      ']
lista_contador = [0, 1500, 3500, 3000, 500, 150, 150]
# [0, 0, 0, 0, 0, 0, 0]

voto = 1
maior = 0

print('Qual o melhor Sistema Operacional para uso em servidores?')
print()
print('As possíveis respostas são:')
print()

while voto != 0:
    voto = int(input('1 - Windows Server\n'
                     '2 - Unix\n'
                     '3 - Linux\n'
                     '4 - Netware\n'
                     '5 - Mac OS\n'
                     '6 - Outro: '))
    while voto not in lista_votacao:
        print()
        print('Informe um valor entre 1 a 6 ou 0 para sair! ')
        voto = int(input('1 - Windows Server\n'
                         '2 - Unix\n'
                         '3 - Linux\n'
                         '4 - Netware\n'
                         '5 - Mac OS\n'
                         '6 - Outro: '))
        print()

    if voto == 1:
        atualizar_lista(1)

    elif voto == 2:
        atualizar_lista(2)

    elif voto == 3:
        atualizar_lista(3)

    elif voto == 4:
        atualizar_lista(4)

    elif voto == 5:
        atualizar_lista(5)

    elif voto == 6:
        atualizar_lista(6)


print()

print()

total_votos = sum(lista_contador)

print('Sistema Operacional\t\tVotos\t\t%: ')
print()
for sistema, voto in zip(sistemas_operacionais, lista_contador):
    if voto != 0:
        porc = (voto / total_votos) * 100
        print(f'{sistema}\t\t\t{voto}  \t\t{porc:0.0f}%')
        if porc > maior:
            maior = porc
            nome = sistema.strip()
            qtd = voto
print(f'Total\t\t\t\t\t{total_votos}')
print(f'O melhor jogador foi o número {nome}, com {qtd} votos, correspondendo a {maior:.0f}% do total de votos.')
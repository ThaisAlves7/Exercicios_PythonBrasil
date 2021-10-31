# Jogo de Craps. Faça um programa de implemente um jogo de Craps. O jogador lança um par de dados, obtendo um valor
# entre 2 e 12. Se, na primeira jogada, você tirar 7 ou 11, você um "natural" e ganhou. Se você tirar 2, 3 ou 12 na primeira jogada,
# isto é chamado de "craps" e você perdeu. Se, na primeira jogada, você fez um 4, 5, 6, 8, 9 ou 10,este é seu "Ponto". Seu
# objetivo agora é continuar jogando os dados até tirar este número novamente. Você perde, no entanto, se tirar um 7 antes de
# tirar este Ponto novamente.

import random

# 1- Natural, 2- Craps, 3- Ponto, 4 - Valor do dado
placar = [0, 0, 0, 0]

def atualizar_placar(ponto, valor_dado):
    contador = placar[ponto]
    contador += 1
    del (placar[ponto])
    placar.insert(ponto, contador)
    if valor_dado != 0:
        del (placar[ponto])
        placar.insert(ponto, valor_dado)


def Craps(rodada, valor_dado):
    dado_ponto = placar[3]
    if rodada == 1:

        if valor_dado in [7, 11]:
            print('Você é um natural - VOCÊ GANHOU')
            atualizar_placar(0, 0)

        elif valor_dado in [2, 3, 12]:
            print('Que Pena CRAPS - VOCÊ PERDEU')
            atualizar_placar(1, 0)

        elif valor_dado in [4, 5, 6, 8, 9, 10]:
            atualizar_placar(2, 0)
            dado_ponto = valor_dado
            atualizar_placar(3, valor_dado)
            print(f'Você fez um 1 PONTO - Deve tirar {dado_ponto} para ganhar')

    else:
        if valor_dado == 7:
            print('Voce perdeu')
            atualizar_placar(1, 0)

        elif dado_ponto == valor_dado:
            print(f'Você tirou numero {valor_dado} e o número anterior é {dado_ponto} - VOCÊ GANHOU')

        else:
            print(f'Você tirou numero {valor_dado} e o número anterior é {dado_ponto} - TENTE DENOVO')


vitoria = False
rodada = 1
while not vitoria:
    partida = int(input('Deseja jogar o dado 1 - Sim ou 2 - Não: '))
    while partida not in [1, 2]:
        print('Escolha uma opção valida')
        partida = int(input('Deseja jogar o dado 1 - Sim ou 2 - Não: '))
    if partida == 1:
        print('Vamos Jogar Craps')
        dado = random.randint(2, 12)
        print(f'Você tirou {dado}')

        Craps(rodada, dado)
        rodada += 1
        if placar[0] == 1:
            vitoria = True

        elif placar[1] == 1:
            vitoria = True

        else:
            if placar[2] == 1:
                dado_ponto = dado
            vitoria = False

    else:
        print('Até mais - Espero que tenha curtido o jogo!!!')
        vitoria = False

    print()


# Uma grande emissora de televisão quer fazer uma enquete entre os seus telespectadores para saber qual o melhor jogador após
# cada jogo. Para isto, faz-se necessário o desenvolvimento de um programa, que será utilizado pelas telefonistas, para a
# computação dos votos. Sua equipe foi contratada para desenvolver este programa, utilizando a linguagem de programação C++.
# Para computar cada voto, a telefonista digitará um número, entre 1 e 23, correspondente ao número da camisa do jogador. Um
# número de jogador igual zero, indica que a votação foi encerrada. Se um número inválido for digitado, o programa deve ignorá-
# lo, mostrando uma breve mensagem de aviso, e voltando a pedir outro número. Após o final da votação, o programa deverá
# exibir:
    # a. O total de votos computados;
    # b. Os númeos e respectivos votos de todos os jogadores que receberam votos;
    # c. O percentual de votos de cada um destes jogadores;
    # d. O número do jogador escolhido como o melhor jogador da partida, juntamente com o número de votos e o percentual de
    # votos dados a ele.
# Observe que os votos inválidos e o zero final não devem ser computados como votos. O resultado aparece
# ordenado pelo número do jogador. O programa deve fazer uso de arrays. O programa deverá executar o cálculo
# do percentual de cada jogador através de uma função. Esta função receberá dois parâmetros: o número de votos
# de um jogador e o total de votos. A função calculará o percentual e retornará o valor calculado. Abaixo segue
# uma tela de exemplo. O disposição das informações deve ser o mais próxima possível ao exemplo. Os dados são
# fictícios e podem mudar a cada execução do programa. Ao final, o programa deve ainda gravar os dados
# referentes ao resultado da votação em um arquivo texto no disco, obedecendo a mesma disposição apresentada
# na tela.
# Enquete: Quem foi o melhor jogador?
# Número do jogador (0=fim): 9
# Número do jogador (0=fim): 10
# Número do jogador (0=fim): 9
# Número do jogador (0=fim): 10
# Número do jogador (0=fim): 11
# Número do jogador (0=fim): 10
# Número do jogador (0=fim): 50
# Informe um valor entre 1 e 23 ou 0 para sair!
# Número do jogador (0=fim): 9
# Número do jogador (0=fim): 9
# Número do jogador (0=fim): 0
# Resultado da votação:
# Foram computados 8 votos.
# Jogador   Votos   %
# 9         4       50,0%
# 10        3       37,5%
# 11        1       12,5%
# O melhor jogador foi o número 9, com 4 votos, correspondendo a 50% do total de votos.

def atualizar_lista(posicao):
    contador = lista_contador[posicao]
    contador += 1
    del (lista_contador[posicao])
    lista_contador.insert(posicao, contador)


lista_votacao = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23]
lista_contador = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]


print(lista_contador)
voto = 1
maior = 0

print('Enquete: Quem foi o melhor jogador?')
while voto != 0:
    voto = int(input('Número do jogador (0=fim): '))
    while voto not in lista_votacao:
        print()
        print('Informe um valor entre 1 e 23 ou 0 para sair! ')
        voto = int(input('Número do jogador (0=fim): '))
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

    elif voto == 7:
        atualizar_lista(7)

    elif voto == 8:
        atualizar_lista(8)

    elif voto == 9:
        atualizar_lista(9)

    elif voto == 10:
        atualizar_lista(10)

    elif voto == 11:
        atualizar_lista(11)

    elif voto == 12:
        atualizar_lista(12)

    elif voto == 13:
        atualizar_lista(13)

    elif voto == 14:
        atualizar_lista(14)

    elif voto == 15:
        atualizar_lista(15)

    elif voto == 16:
        atualizar_lista(16)

    elif voto == 17:
        atualizar_lista(17)

    elif voto == 18:
        atualizar_lista(18)

    elif voto == 19:
        atualizar_lista(19)

    elif voto == 20:
        atualizar_lista(20)

    elif voto == 21:
        atualizar_lista(21)

    elif voto == 23:
        atualizar_lista(22)

    elif voto == 23:
        atualizar_lista(23)

print()
print('Resultado da votação: ')
print()

total_votos = sum(lista_contador)
print(total_votos)
print()

print('Jogador Votos e %')
for jogador, voto in zip(lista_votacao, lista_contador):
    if voto != 0:
        porc = (voto / total_votos) * 100
        print(f'{jogador} - {voto} - {porc:.1f}%')
        if porc > maior:
            maior = porc
            nome = jogador
            qtd = voto

print(f'O melhor jogador foi o número {nome}, com {qtd} votos, correspondendo a {maior:.0f}% do total de votos.')
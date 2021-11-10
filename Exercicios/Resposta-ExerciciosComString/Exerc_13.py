# Jogo da palavra embaralhada. Desenvolva um jogo em que o usuário tenha que adivinhar uma palavra que será mostrada com
# as frases embaralhadas. O programa terá uma lista de palavras lidas de um arquivo texto e escolherá uma aleatoriamente. O
# jogador terá seis tentativas para adivinhar a palavra. Ao final a palavra deve ser mostrada na tela, informando se o usuário
# ganhou ou perdeu o jogo.


from random import choice, sample

arquivo_palavras = open('arquivo_palavras.txt', 'r')
lista_palavras = arquivo_palavras.readlines()
palavra_sorteada = choice(lista_palavras)
palavra_sorteada = palavra_sorteada.lower().replace('\n', '')
palavra = sample(palavra_sorteada, (len(palavra_sorteada)))



tentativa = 6

chute = []

print(f'A palavra sorteada foi:  {palavra}')

while True:
    print(tentativa)
    print(f"Você tem: {tentativa} tentativas")
    print()
    print(f'A palavra sorteada foi:  {palavra}')
    print()

    for repetidas in chute:
        print(repetidas)


    frase = input('\nDigite um chute ou SAIR para sair do Jogo: ').lower().strip()
    if frase == 'sair':
        break


    if frase == '':
        print('Chute de frase inválido tente denovo!!!')
        continue

    elif frase in chute:
        print('Você ja tentou essa frase vamos denovo')
        continue
    chute.append(frase)

    if tentativa == 0:
        print('Você perdeu, Gamer Over!!!')
        break

    if set(palavra_sorteada).issubset(set(frase)):
        print('Parabens, você é DEMAIS acerto a palavra')
        break

    else:
        print('É você erro infelizmente não foi um bom chute vamos de denovo?')
        tentativa -= 1

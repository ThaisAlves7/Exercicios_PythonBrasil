# Jogo de Forca. Desenvolva um jogo da forca. O programa terá uma lista de palavras lidas de um arquivo texto e escolherá uma
# aleatoriamente. O jogador poderá errar 6 vezes antes de ser enforcado.
    # Digite uma letra: A
    # -> Você errou pela 1ª vez. Tente de novo!
    # Digite uma letra: O
    # A palavra é: _ _ _ _ O
    # Digite uma letra: E
    # A palavra é: _ E _ _ O
    # Digite uma letra: S
    # -> Você errou pela 2ª vez. Tente de novo!
from random import choice

arquivo_palavras = open('palavras_jogo_da_forca.txt', 'r')
lista_palavras = arquivo_palavras.readlines()
palavra = choice(lista_palavras)
palavra = palavra.lower().replace('\n', '')
print(palavra)

alfabeto = list('abdcefghijklmnopqrstuvwxyz')
chute = []
tentativa = 6


while True:
    print(tentativa)
    print(f"Você tem: {tentativa} tentativas")

    for letra in palavra:
        if letra in chute:
            print(letra, end=' ')

        else:
            print('X', end=' ')

    letra = input('\nDigite um chute ou SAIR para sair do Jogo: ').lower().strip()
    if letra == 'sair':
        break
    else:
        letra = letra[0]

    if letra not in alfabeto or letra == '':
        print('Chute de letra inválido tente denovo!!!')
        continue

    elif letra in chute:
        print('Você ja tentou essa letra vamos denovo')
        continue
    chute.append(letra)

    if letra in palavra:
        print('Bom chute você acertou a letra. Você é bom !!!')

    else:
        print('É você erro infelizmente não foi um bom chute vamos de denovo?')
        tentativa -= 1

    if tentativa == 0:
        print('Você perdeu, Gamer Over!!!')
        break

    elif set(palavra).issubset(set(chute)):
        print('Parabens, você é DEMAIS acerto a palavra')
        break



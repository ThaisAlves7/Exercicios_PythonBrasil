# Numa eleição existe 3 candidatos. Faça um programa que peça o número total de eleitores. Peça para cada eleitor votar
    # e ao final mostrar o numero de votos de cada candidato:


continuar = 1
candidato_1, candidato_2, candidato_3 = 1, 1, 1

while continuar != 2:
    voto = int(input('Informe o numero do candidato\n'
                     '1 - Candidato 1\n'
                     '2 - Candidato 2\n'
                     '3 - Candidato 3: '))
    print()
    continuar = int(input('Deseja continuar votando ? 1 - Sim e 2 - Não: '))
    if continuar == 1:
        voto = int(input('Informe o numero do candidato\n'
                         '1 - Candidato 1\n'
                         '2 - Candidato 2\n'
                         '3 - Candidato 3: '))
        while voto not in [1, 2, 3]:
            print()
            print('Informe um voto valido')
            voto = int(input('Informe o numero do candidato\n'
                             '1 - Candidato 1\n'
                             '2 - Candidato 2\n'
                             '3 - Candidato 3: '))
    if voto == 1:
        candidato_1 += 1

    elif voto == 2:
        candidato_2 += 1

    else:
        candidato_3 += 1


print(f'O Candidato 1 recebeu {candidato_1} votos')
print(f'O Candidato 2 recebeu {candidato_2} votos')
print(f'O Candidato 3 recebeu {candidato_3} votos')

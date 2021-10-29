# Desenvolver um programa para verificar a nota do aluno em uma prova com 10 questões, o programa deve perguntar
# ao aluno a resposta de cada questão e ao final comparar com o gabarito da prova e assim calcular o total de acertos e a nota (atribuir 1
# ponto por resposta certa). Após cada aluno utilizar o sistema deve ser feita uma pergunta se outro aluno vai utilizar o sistema.
# Após todos os alunos terem respondido informar:
    # a. Maior e Menor Acerto;
    # b. Total de Alunos que utilizaram o sistema;
    # c. A Média das Notas da Turma.
        # Gabarito da Prova:
        # 01 - A
        # 02 - B
        # 03 - C
        # 04 - D
        # 05 - E
        # 06 - E
        # 07 - D
        # 08 - C
        # 09 - B
        # 10 - A
# Após concluir isto você poderia incrementar o programa permitindo que o professor digite o gabarito da prova antes dos
# alunos usarem o programa.

import numpy as np

acertos = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
total_acertos = []


def add_pontos_acertos(posicao):
    contador = acertos[posicao]
    contador += 1
    del (acertos[posicao])
    acertos.insert(posicao, contador)


def gabarito_prova(aluno: list, gabarito: dict):
    k_value, elemento = 1, 0
    if gabarito == None:
        gabarito = {1: 'A', 2: 'B', 3: 'C', 4: 'D', 5: 'E', 6: 'E', 7: 'D', 8: 'C', 9: 'B', 10: 'A'}
    else:
        gabarito = gabarito
        print(gabarito)

    for valor in aluno:
        if valor == gabarito.get(k_value):
            add_pontos_acertos(elemento)
        k_value += 1
        elemento += 1

alternativas = ['A', 'B', 'C', 'D', 'E']
resp_aluno = []
gabarito_novo = {}

gabarito_resposta = int(input('Deseja adicionar um novo Gabarito 1 - Sim ou 2 - Não: '))
while gabarito_resposta not in [1, 2]:
    print('Responda apenas com 1 ou 2')
    gabarito_resposta = int(input('Deseja adicionar um novo Gabarito 1 - Sim ou 2 - Não: '))

if gabarito_resposta == 1:
    for i in range(1, 11):
        resp_prof = input(f'Resposta da {i}° pergunta: ').upper()
        while resp_prof not in alternativas:
            print('Responda com uma alternativa valida de A a E')
            resp_prof = input(f'Resposta da {i}° pergunta: ').upper()
        gabarito_novo.update({i: resp_prof})
else:
    gabarito_novo = None
print()
continuar = 1
while continuar == 1:
    for i in range(1, 11):
        resposta = input(f'Digite a resposta da alternativa da {i} pergunta: ').upper()
        while resposta not in alternativas:
            print('Informe uma alternativa correta: ')
            resposta = input(f'Digite a resposta da alternativa da {i} pergunta: ').upper()
        resp_aluno.append(resposta)

    gabarito_prova(resp_aluno, gabarito_novo)

    total = sum(acertos)
    total_acertos.append(total)
    print()
    continuar = int(input('Mais algum aluno ira responder a prova? 1 - Sim ou 2 Não: '))
    while continuar not in [1, 2]:
        print('Responda apenas com 1 ou 2')
        continuar = int(input('Mais algum aluno ira responder a prova? 1 - Sim ou 2 Não: '))
        print()

media = np.mean(total_acertos)
print()
print(f'A maior acerto foi {max(total_acertos)}')
print(f'A menor acerto foi {min(total_acertos)}')
print(f'A media das notas da Turma é {media:.2f}')

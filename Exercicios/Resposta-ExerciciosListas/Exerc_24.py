# Faça um programa que simule um lançamento de dados. Lance o dado 100 vezes e armazene os resultados em um vetor .
# Depois, mostre quantas vezes cada valor foi conseguido. Dica: use um vetor de contadores(1-6) e uma função para gerar
# numeros aleatórios, simulando os lançamentos dos dados.

import random

lista_contador = [0, 0, 0, 0, 0, 0]
# [0, 1500, 3500, 3000, 500, 150, 150]
fim = 100

def atualizar_lista(posicao):
    contador = lista_contador[posicao]
    contador += 1
    del (lista_contador[posicao])
    lista_contador.insert(posicao, contador)

for i in range(1, fim+1):
    number = random.randint(1, 6)
    number -= 1
    atualizar_lista(number)

print()
print(f'Quantidade de vezes que o lado de um dado pode aparecer jogando ele {fim}')
print()
print(f'O número 1 apareceu {lista_contador[0]}')
print(f'O número 2 apareceu {lista_contador[1]}')
print(f'O número 3 apareceu {lista_contador[2]}')
print(f'O número 4 apareceu {lista_contador[3]}')
print(f'O número 5 apareceu {lista_contador[4]}')
print(f'O número 6 apareceu {lista_contador[5]}')

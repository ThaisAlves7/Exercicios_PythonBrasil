#  Sua organização acaba de contratar um estagiário para trabalhar no Suporte de Informática, com a intenção de fazer um
# levantamento nas sucatas encontradas nesta área. A primeira tarefa dele é testar todos os cerca de 200 mouses que se
# encontram lá, testando e anotando o estado de cada um deles, para verificar o que se pode aproveitar deles.
    #  Foi requisitado que você desenvolva um programa para registrar este levantamento. O programa deverá receber um
    # número indeterminado de entradas, cada uma contendo: um número de identificação do mouse o tipo de defeito:
    # necessita da esfera;
    # necessita de limpeza; a.necessita troca do cabo ou conector;
    # a.quebrado ou inutilizado
    # Uma identificação igual a zero
    # encerra o programa. Ao final o programa deverá emitir o seguinte relatório:
    # Quantidade de mouses: 100
    # Situação                               Quantidade          Percentual
    # 1- necessita da esfera                    40                  40%
    # 2- necessita de limpeza                   30                  30%
    # 3- necessita troca do cabo ou conector    15                  15%
    # 4- quebrado ou inutilizado                15                  15%


situacao = ['Necessita de Esfera', 'Necessita de Limpeza', 'Necessita troca do cabo ou conector', 'Quebrado ou Inutilizado']
quantidade = [0, 0, 0, 0]
continuar, maior, x = 1, 1, 1

def aumentar_quantidade(posicao):
    contador = quantidade[posicao]
    contador += 1
    del (quantidade[posicao])
    quantidade.insert(posicao, contador)

print()
while continuar != 0:
    mouse = int(input('Informe o defeito do mouse\n'
                      f'1 - {situacao[0]}\n'
                      f'2 - {situacao[1]}\n'
                      f'3 - {situacao[2]}\n'
                      f'4 - {situacao[3]}: '))
    print()
    while mouse not in [1, 2, 3, 4]:
        print('Informe um número de seleção valido')
        mouse = int(input('Informe o defeito do mouse\n'
                          f'1 - {situacao[0]}\n'
                          f'2 - {situacao[1]}\n'
                          f'3 - {situacao[2]}\n'
                          f'4 - {situacao[3]}: '))
        print()

    mouse -= 1
    aumentar_quantidade(mouse)
    print()
    continuar = int(input('Deseja continuar 1 - Sim ou 0 - Não: '))
    while continuar not in [0, 1]:
        print('Informe uma opção válida entre 1 e 2')
        continuar = int(input('Deseja continuar 1 - Sim ou 0 - Não: '))
        print()

for palavra in situacao:
    espaco = len(palavra)
    if espaco > maior:
        maior = espaco

total_itens = sum(quantidade)
tab = ''
print()
print(f'Situação{tab.ljust(maior)}Quantidade{tab.ljust(maior)}Percentual')


for estado, qtde in zip(situacao, quantidade):
    percentual = (total_itens * qtde) / 100
    print(f'{x}- {estado.ljust(maior)}\t\t\t{str(qtde).ljust(maior)}\t\t\t{percentual:.0f}%')
    x += 1
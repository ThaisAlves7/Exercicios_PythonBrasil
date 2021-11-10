#  A ACME Inc., uma empresa de 500 funcionários, está tendo problemas de espaço em disco no seu servidor de arquivos.
#  Para tentar resolver este problema, o Administrador de Rede precisa saber qual o espaço ocupado pelos usuários, e identificar os
# usuários com maior espaço ocupado. Através de um programa, baixado da Internet, ele conseguiu gerar o seguinte arquivo, chamado "usuarios.txt":
        # alexandre          456123789
        # anderson          1245698456
        # antonio            123456456
        # carlos              91257581
        # cesar                 987458
        # rosemary           789456125
# Neste arquivo, o nome do usuário possui 15 caracteres. A partir deste arquivo, você deve criar um programa que gere um
# relatório, chamado "relatório.txt", no seguinte formato:
        # ACME Inc. Uso do espaço em disco pelos usuários
        # ------------------------------------------------------------------------
        # Nr.    Usuário        Espaço utilizado        % do uso
        # 1     alexandre       434,99 MB               16,85%
        # 2     anderson        1187,99 MB              46,02%
        # 3     antonio         117,73 MB               4,56%
        # 4     carlos          87,03 MB                3,37%
        # 5     cesar           0,94 MB                 0,04%
        # 6     rosemary        752,88 MB               29,16%

        # Espaço total ocupado: 2581,57 MB
        # Espaço médio ocupado: 430,26 MB
# O arquivo de entrada deve ser lido uma única vez, e os dados armazenados em memória, caso sejam necessários, de forma a
# agilizar a execução do programa. A conversão da espaço ocupado em disco, de bytes para megabytes deverá ser feita através de
# uma função separada, que será chamada pelo programa principal. O cálculo do percentual de uso também deverá ser feito
# através de uma função, que será chamada pelo programa principal.



# Obs.: caso queira testar apague o "relatório.txt" ele ira criar o arquivo novamente
import numpy as np

total_ocupado = 2581.57
users, espaco_utilizado, porcento = [], [], []

arquivo_original = open('usuarios.txt', 'r')
relatorio = open('relatório.txt', 'a')

def byte_mega(bytes):
    mega = bytes / (1024 * 1024)
    mega = round(mega, 2)
    calculo_percentual_uso(mega)
    espaco_utilizado.append(mega)

def calculo_percentual_uso(MB):
    porcentual = (MB * 100) / total_ocupado
    porcentual = round(porcentual, 2)
    porcento.append(porcentual)

for linha in arquivo_original:
    nome = linha.split()
    usuario = nome[0]
    byte = int(nome[1])
    users.append(usuario)
    byte_mega(byte)

arquivo_original.close()

tab, tab2 = ''.ljust(33), ''.ljust(13)
x = 1
media = np.mean(espaco_utilizado)

print()
print(f'ACME Inc.{tab} Uso o espaço em disco pelo usuários')
relatorio.write(f'ACME Inc.{tab} Uso o espaço em disco pelo usuários\n')
print('-'*90)
relatorio.write('-'*90)
relatorio.write('\n')
print(f'Nr.   Usuário {tab2} Espaço utilizado {tab2} %do uso')
relatorio.write(f'Nr.   Usuário {tab2} Espaço utilizado {tab2} %do uso\n')
print()
relatorio.write('\n')
for nome, espaco, porcentual in zip(users, espaco_utilizado, porcento):
    print(f'{x}     {nome.ljust(9)}{tab2} {str(espaco).ljust(7)} MB\t\t {tab2} {str(porcentual).ljust(5)} %')
    relatorio.write(f'{x}     {nome.ljust(9)}{tab2} {str(espaco).ljust(7)} MB\t\t {tab2} {str(porcentual).ljust(5)} %\n')
    x += 1
print()
relatorio.write('\n')
print(f'Espaço total ocupado: {sum(espaco_utilizado)} MB')
relatorio.write(f'Espaço total ocupado: {sum(espaco_utilizado)} MB\n')
print(f'Espaço médio ocupado: {media:.2f} MB')
relatorio.write(f'Espaço médio ocupado: {media:.2f} MB\n')

relatorio.close()
# print(users)
# print(espaco_utilizado)
# print(porcento)



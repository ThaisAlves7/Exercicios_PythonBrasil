# Faça um programa que leia um arquivo texto contendo uma lista de endereços IP e gere um outro arquivo, contendo um
# relatório dos endereços IP válidos e inválidos.
#     O arquivo de entrada possui o seguinte formato:
#         200.135.80.9
#         192.168.1.1
#         8.35.67.74
#         257.32.4.5
#         85.345.1.2
#         1.2.3.4
#         9.8.234.5
#         192.168.0.256
# O arquivo de saída possui o seguinte formato:
#     [Endereços válidos:]
#         200.135.80.9
#         192.168.1.1
#         8.35.67.74
#         1.2.3.4
#
#     [Endereços inválidos:]
#         257.32.4.5
#         85.345.1.2
#         9.8.234.5
#         192.168.0.256

endereco_valido, endereco_invalido = [], []
arquivo = open('enderecoIP.txt', 'r')
lista_arquivo = arquivo.readlines()
valido = '255.255.224.255'  # 224 do sufixo D de endereços IP

def validar_ip_addres(lista_IP: list, validador):
    for endereco in lista_arquivo:
        endereco = endereco.replace('\n', '')
        posicao = endereco.index('.')
        if int(validador[:3]) > int(endereco[:posicao]):
            aux = endereco[posicao + 1:]
            posicao = aux.index('.')
            if int(validador[4:7]) > int(aux[:posicao]):
                aux = aux[posicao + 1:]
                posicao = aux.index('.')
                if int(validador[8:11]) > int(aux[:posicao]):
                    aux = aux[posicao + 1:]
                    if int(valido[12:]) > int(aux):
                        endereco_valido.append(endereco)

                    else:
                        endereco_invalido.append(endereco)
                else:
                    endereco_invalido.append(endereco)
            else:
                endereco_invalido.append(endereco)
        else:
            endereco_invalido.append(endereco)


validar_ip_addres(lista_arquivo, valido)
print(f'{endereco_valido}\n'
      f'{endereco_invalido}')
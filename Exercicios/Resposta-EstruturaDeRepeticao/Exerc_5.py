# Altere o programa anterior permitindo ao usuario informar as populações e as taxas de crescimento iniciais. Valide a entrada
    # e permita repetir a operação


def calculo_populacional(pais_A, pais_B, cresc_A, cresc_B):
    cont_anos = 0

    if (pais_A < pais_B):
        validar = True if (pais_A >= pais_B) else False

        while (validar != True):
            pais_A = pais_A + ((pais_A * cresc_A) / 100)
            pais_B = pais_B + ((pais_B * cresc_B) / 100)
            cont_anos += 1
            validar = True if (pais_A >= pais_B) else False
        return print(f'O pais A vai ultrapassar o Pais B em {cont_anos} anos.')
    else:
        validar = True if (pais_B >= pais_A) else False

        while (validar != True):
            pais_A = pais_A + ((pais_A * cresc_A) / 100)
            pais_B = pais_B + ((pais_B * cresc_B) / 100)
            cont_anos += 1
            validar = True if (pais_B >= pais_A) else False
        return print(f'O pais B vai ultrapassar o Pais A em {cont_anos} anos.')

def validar_entrada(validar1, validar2):
    validar = True if ((validar1 != 0) and (validar2 != 0)) else False
    if validar:
        return True
    else:
        return False

continuar = 1
while (continuar != 2):
    paisA = int(input('Informe quantidade de HABITANTES da população do Pais A: '))
    paisB = int(input('Informe quantidade de HABITANTES da população do Pais B: '))
    validar_pais = validar_entrada(paisA, paisB)
    while validar_pais != True:
        paisA = int(input('Informe quantidade de HABITANTES da população do Pais A: '))
        paisB = int(input('Informe quantidade de HABITANTES da população do Pais B: '))
        validar_pais = validar_entrada(paisA, paisB)
    print()
    taxaA = float(input('Informe a TAXA de crescimento do Pais A: '))
    taxaB = float(input('Informe a TAXA de crescimento do Pais B: '))
    validar_taxa = validar_entrada(taxaA, taxaB)
    while validar_taxa != True:
        taxaA = float(input('Informe a TAXA de crescimento do Pais A: '))
        taxaB = float(input('Informe a TAXA de crescimento do Pais B: '))
        validar_taxa = validar_entrada(taxaA, taxaB)
    print()
    calculo_populacional(paisA, paisB, taxaA, taxaB)
    print()
    continuar = int(input('Escolha a opção do Menu\n'
                          '1 - Deseja continuar ?\n'
                          '2 - Deseja Sair?: \n'
                          ''))



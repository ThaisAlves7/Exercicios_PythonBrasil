# Verificação de CPF. Desenvolva um programa que solicite a digitação de um número de CPF no formato xxx.xxx.xxx-xx e
# indique se é um número válido ou inválido através da validação dos dígitos verificadores edos caracteres de formatação.

from validate_docbr import CPF

cpf_valido = CPF()

def inserir_mascara(cpf):
    mascara = cpf_valido.mask(cpf)
    return print(f'O CPF {mascara} é um CPF válido')

def validar_cpf(documento):
    if len(documento) == 11:
        valido = cpf_valido.validate(documento)
        if valido:
            return inserir_mascara(documento)
        return print('CPF Falso')
    return print('Quantidade de digítos incorreta')


print('Insira o CPF no formato "XXX.XXX.XXX-XX')
cpf_user = input('Insira um CPF: ')
cpf_user = cpf_user.replace('.', '').replace('-', '')

validar_cpf(cpf_user)
# Faça um programa que leia e valide as seguintes informações:
    # A - Nome: maior que 3 caracteres
    # B - Idade: entre 0 e 150
    # C - Sexo: 'f' ou 'm'
    # D - Estado Civil: 's', 'c', 'v', 'd'


def validar_nome(palavra):
    if (len(palavra) <= 3):
        print(f'Nome {palavra} é valido')
    else:
        print(f'Nome {palavra} Invalido')

def validar_idade(number):
    if ((number >= 0) and (number <= 150)):
        print(f'Idade {number} Valida')
    else:
        print(f'Idade {number} Inválida')

def validar_sexo(sexo):
    if ((sexo == 'f') or (sexo == 'm')):
        print(f'Sexo Válido {sexo} é válido')
    else:
        print(f'Sexo {sexo} é inválido')

def validar_estado_civil(estado):
    estado_civil = ['s', 'c', 'v', 'd']
    if (estado in estado_civil):
        print(f'Estado Civil {estado} é válido')
    else:
        print('Estado Civil Inválido')


nome = input('Informe um nome: ')
validar_nome(nome)

idade = int(input('Informe uma idade: '))
validar_idade(idade)

sexo = input('Informe o sexo: f - feminino e m - masculino: ').lower()
validar_sexo(sexo)

estado = input('Informe o seu estado civil: s - solteiro, c - casado, v - viuvo, d - divorciado: ').lower()
validar_estado_civil(estado)
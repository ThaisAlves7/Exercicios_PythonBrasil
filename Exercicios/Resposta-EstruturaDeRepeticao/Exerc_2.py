# Faça um programa que leia um nome de usuario e a senha e não aceite a senha igual ao nome do usuario, mostrando uma
    # mensagem de erro e voltando a pedir as informações

user = []

usuario = input('Informe um usuario: ').lower()
user.append(usuario)

senha = input('Informe uma senha: ').lower()
while senha in user:
    print('Insira uma senha válida')
    senha = input('Informe uma senha: ')

print('Usuario e senha - Criado')
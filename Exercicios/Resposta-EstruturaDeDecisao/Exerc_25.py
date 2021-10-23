# Faça um programa que faça 5 perguntas para uma pessoa sobre um crime. As perguntas são:
    # A - "Telefonou para a vítima?"
    # B - "Esteve no local do crime?"
    # C - "Mora perto da vítima?"
    # D - "Devia para a vítima?"
    # E - "Já trabalhou com a vítima?"
# O programa deve no final emitir uma classificação sobre a participação da pessoa no crime. Se a pessoa responder positivamente
    #a 2 questões ela deve ser classificada como "Suspeita", entre 3 e 4 como "Cúmplice" e 5 como "Assassino". Casso contrário
    # ele será classificado como "Inocente".


print('Questionário de um crime - Responda apenas com 1-Sim ou 2-Não')

perguntas = ["Telefonou para a vítima? 1-Sim ou 0-Não: ", "Esteve no local do crime? 1-Sim ou 0-Não: ",
             "Mora perto da vítima? 1-Sim ou 0-Não: ", "Devia para a vítima? 1-Sim ou 0-Não: ",
             "Já trabalhou com a vítima? 1-Sim ou 0-Não: "]
resp = []
valor_resp = 0
condicao = [0, 1]

for i in range(len(perguntas)):
    print(perguntas[i])
    validar = int(input())
    if validar in condicao:
        resp.append(validar)
    else:
        while validar not in condicao:
            print(perguntas[i])
            validar = int(input())
            if validar in condicao:
                resp.append(validar)
                break

for valor in range(len(resp)):
    valor_resp += resp[valor]

if (valor_resp == 2):
    print('Essa pessoa é Suspeita')

elif ((valor_resp <= 3) or (valor_resp <= 4)):
    print('Essa pessoa foi Cúmplice - Prendam-na e a Interroguem')

elif (valor_resp == 5):
    print('Prendam esse Assassino !!!!')

else:
    print('Essa pessoa é Inocente - Soltem-na')

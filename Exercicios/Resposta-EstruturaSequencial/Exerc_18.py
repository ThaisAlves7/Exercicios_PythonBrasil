# Faça um programa que peça o tamanho de um arquivo para download (em MB) e a velocidade de um link de Internet(em Mbps)
# , calcule e informe o tempo aproximado de download do arquivo usando este link (em minutos)

tamanho_arquivo = float(input('Informe o tamanho do arquivo em MB: '))
velocidade = float(input('Informe a velocidade da sua internet em Mbps: '))

minutos = (tamanho_arquivo / (velocidade / 8)) / 60

print(f'O Arquivo de {tamanho_arquivo:.0f}MB levará {minutos:.2f}min para baixar')



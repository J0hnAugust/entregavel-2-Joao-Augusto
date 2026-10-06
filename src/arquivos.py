import csv

# Funções de leitura do arquivo CSV
def ler_anotacoes():
    anotacoes = []
    with open('dados/anotacoes.csv', 'r') as arquivo:
        leitor = csv.reader(arquivo)
        for linha in leitor:
            anotacoes.append(linha)
    return anotacoes
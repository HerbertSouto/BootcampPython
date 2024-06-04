import csv

# Definindo o caminho do arquivo CSV
caminho_csv: str = "dados.csv"

# Lista para armazenar os dados lidos do CSV
dados: list = []

# Abrindo o arquivo CSV para leitura
with open(caminho_csv, mode="r") as arquivo:
    leitor_csv = csv.DictReader(arquivo)

    # Percorrendo cada linha do arquivo CSV e adicionando à lista de dados
    for linha in leitor_csv:
        dados.append(linha)

# Imprimindo os dados lidos do CSV
print(dados)

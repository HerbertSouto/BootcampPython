aluno: dict = {}

while True:
    nome_aluno: str = input("digite seu nome: ")
    if nome_aluno.isalpha():
        aluno["nome"] = nome_aluno
        break
    else:
        print("Nome inválido, digite novamente")

for i in range(1, 4):
    while True:
        try:
            nota: float = float(input(f"Digite a nota {i}: "))
            if 0 <= nota <= 10:
                aluno[f"nota {i}"] = nota
                break
            else:
                print("Nota menor ou igual a zero, digite novamente")
        except ValueError:
            print("Nota inválida, digite novamente")
        except Exception as e:
            print(f"Erro inesperado: {e}\nPor favor, tente novamente.")

media = round(float((aluno["nota 1"] + aluno["nota 2"] + aluno["nota 3"]) / 3), 2)

print(f"Nome do aluno: {aluno['nome']}")
print(
    f"Primeira nota: {aluno['nota 1']} \nSegunda nota: {aluno['nota 2']} \nTerceira nota: {aluno['nota 3']}"
)
print(f"Média do aluno: {media}")

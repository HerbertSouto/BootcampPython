aluno:dict = {}

while True:
  nome_aluno:str = input("digite seu nome: ")
  if nome_aluno.isalpha():
    aluno["nome"] = nome_aluno
    break 
  else:
    print("Nome inválido, digite novamente")

while True:
    try:
        nota1:float = float(input("Digite a primeira nota: "))
        if nota1 > 0:
            aluno["nota 1"] = nota1
            break
        else:
           print("Nota menor ou igual a zero, digite novamente")
    except:
        print("Nota inválida, digite novamente")  

while True:
    try:
        nota2:float = float(input("Digite a segunda nota: "))
        if nota2 > 0:
            aluno["nota 2"] = nota2
            break
        else:
           print("Nota menor ou igual a zero, digite novamente")
    except:
        print("Nota inválida, digite novamente")  

while True:
    try:
        nota3:float = float(input("Digite a terceira nota: "))
        if nota3 > 0:
            aluno["nota 3"] = nota3
            break
        else:
           print("Nota menor ou igual a zero, digite novamente")
    except:
        print("Nota inválida, digite novamente")  

print(aluno)
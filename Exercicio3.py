#Exercício 4: Validação de Dados de Entrada
#Antes de processar os dados de usuários em um sistema de recomendação, você precisa garantir que cada usuário tenha idade entre 18 e 65 anos e tenha fornecido um email válido. Escreva um programa que valide essas condições e imprima "Dados de usuário válidos" ou o erro específico encontrado.

import re

def validar_email(email):
    padrao = r'^[\w\.-]+@[\w\.-]+\.\w+$'
    if re.match(padrao, email):
        return True
    else:
        return False

dado_incorreto = True

while dado_incorreto:
    try:
        nome_usuario = input("Digite seu usuário: ")
        usuario_str = str(nome_usuario)
        if not re.search("[a-zA-Z]", nome_usuario):
            raise ValueError("O campo deve conter pelo menos uma letra.")
        dado_incorreto = False
    except ValueError as e:
     print(e)   

menor_de_idade = True

while menor_de_idade:
    try:
        idade = int(input("Digite sua idade: "))
        if idade < 18 or idade > 65:
            raise ValueError("Idade não permitida. Permitido apenas para maiores de 18 e menores de 65.")
        menor_de_idade = False
    except ValueError as e:
        print(e)

email_invalido = True

while email_invalido:
    email = input("Digite seu e-mail: ")
    if validar_email(email):
        email_invalido = False
    else:
        print("E-mail inválido")

print("Dados inseridos com sucesso!")

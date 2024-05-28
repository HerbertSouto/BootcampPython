#Exercício 1: Verificação de Qualidade de Dados
#Você está analisando um conjunto de dados de vendas e precisa garantir que todos os registros tenham valores positivos para quantidade e preço. Escreva um programa que verifique esses campos e imprima "Dados válidos" se ambos forem positivos ou "Dados inválidos" caso contrário.

qtdLoop = False
precoLoop = False

while not qtdLoop:
    try:
        quantidade = input("Digite a quantidade: ")
        qtd_int = int(quantidade)
        if qtd_int <= 0: 
            raise ValueError("A quantidade deve ser um número positivo.")      
        qtdLoop = True    
    except ValueError:
        print("valor inválido, insira um novo valor") 

while not precoLoop:
    try:
        preco = float(input("Digite o preço: "))
        preco_flt = float(preco)
        if preco_flt <= 0: 
            raise ValueError("A preço deve ser um número positivo.") 
        precoLoop = True      
    except ValueError:
       print("valor inválido, insira um novo valor.")

if qtd_int > 0 and preco_flt > 0:
        print("Dados válidos")
        print(f"Quantidade: {qtd_int}, Preço: {preco_flt}")


"""
Exercício 1: Variáveis e Entrada do Usuário
Escreva um programa que peça ao usuário seu nome e idade, e então imprima uma mensagem dizendo "Olá, [nome], você tem [idade] anos."

"""

nome: str = str(input("Digite seu nome: "))
idade: int = int(input("Digite sua idade: "))
print(f"Olá {nome}! Sua idade é {idade} anos.")

nome_loop:bool = True
idade_loop:bool = True

while nome_loop:
  try:
    nome: str = str(input("Digite seu primeiro nome: "))
    if nome.isalpha():
      nome_loop = False
    else:
      raise ValueError("Valor inválido!.")
  except ValueError as e:
    print("Erro:", e)

while idade_loop:
  try:
    idade: int = int(input("Digite sua idade: "))
    if idade > 0:
      idade_loop = False
    else:
      raise ValueError("Idade inválida.")
  except ValueError as e:
    print("Erro:", e)

print(f"Olá {nome}! Sua idade é {idade} anos.")

"""Exercício 2: Condições e Operadores
Escreva um programa que peça ao usuário um número e determine se ele é par ou ímpar.
"""

numero_loop:bool = True

while numero_loop:
  try:
    numero:int = int(input("Digite aqui seu número: "))
    if numero <= 0:
      raise ValueError("Número negativo ou igual a zero, digite um número válido.")
    else:
      numero_loop = False
  except ValueError as e:
    print("Erro:", e)

if numero % 2 == 0:
  print(f"O número {numero} é par.")
else:
  print(f"O número {numero} é ímpar.")

"""Exercício 3: Laços de Repetição Crie um programa que imprima os números de 1 a 10 usando um loop for."""

for i in range(1, 11):
  print(i)

"""Exercício 4: Listas Faça um programa que peça ao usuário 5 números e armazene-os em uma lista. Depois, exiba a lista completa, a soma e a média dos números."""

numeros = []

for i in range(1,6):
  while True:
    try:
      numero:int = int(input("Digite um número: "))
      if numero > 0:
        numeros.append(numero)
        break
      else:
        raise ValueError("Erro,  digite um número válido!")
    except ValueError as e:
      print("Erro:", e)

print(f"\nNúmeros fornecidos: {numeros}")

soma = sum(numeros)
print(f"A soma dos números é: {soma}.")
media = soma / len(numeros)
print(f"A média dos números é: {media}.")

"""Exercício 5: Funções
Escreva uma função chamada soma que receba dois números como parâmetros e retorne a soma deles. Teste a função no seu programa principal.
"""

def somar():

  numero1_loop: bool = True
  numero2_loop: bool = True

  while numero1_loop:

    try:
      numero1:float = float(input("Digite um número:"))
      numero1_loop = False
    except ValueError:
       print("Valor inválido!")

  while numero2_loop:

    try:
      numero2:float = float(input("Digite outro número:"))
      numero2_loop = False
    except ValueError:
       print("Valor inválido!")

    soma = numero1 + numero2
    return print(f"A soma dos números é: {soma}")

somar()

"""Exercício 6: Strings
Escreva um programa que peça ao usuário uma frase e conte quantas vogais (a, e, i, o, u) há na frase.
"""

vogais = "aeiouAEIOUáéíóúÁÉÍÓÚâêîôûÂÊÎÔÛã"

while True:
  try:
    frase:str = input("Escreva uma frase: ")
    if any(char.isdigit() for char in frase):
      raise ValueError("Erro: Digite uma frase válida que contenha apenas letras e pontuações!")
    break
  except ValueError as e:
      print("Erro:", e)

contador = 0

for letra in frase:
  if letra in vogais:
    contador += 1

print(f"A sua frase contém {contador} vogais.")

"""Exercício 7: Dicionários
Crie um dicionário para armazenar informações de um aluno: nome, idade e notas (uma lista de três notas). Calcule a média das notas e imprima as informações do aluno e sua média.

"""
aluno:dict = {}

while True:
  nome_aluno:str = input("digite seu nome: ")
  if nome_aluno.isalpha():
    aluno["nome"] = nome_aluno
    break
  else:
    print("Nome inválido, digite novamente")

for i in range(1, 4):
  while True:
    try:
        nota:float = float(input(f"Digite a nota {i}: "))
        if 0 <= nota <= 10:
            aluno[f"nota {i}"] = nota
            break
        else:
           print("Nota menor ou igual a zero, digite novamente")
    except:
        print("Nota inválida, digite novamente")

media = round(float((aluno["nota 1"] + aluno["nota 2"] + aluno["nota 3"]) / 3),2)

print(f"Nome do aluno: {aluno['nome']}")
print(f"Primeira nota: {aluno['nota 1']} \nSegunda nota: {aluno['nota 2']} \nTerceira nota: {aluno['nota 3']}")
print(f"Média do aluno: {media}")

"""Exercício 8: Manipulação de Arquivos
Escreva um programa que leia o conteúdo de um arquivo chamado texto.txt e exiba o conteúdo na tela.
"""

with open('texto.txt', "r") as arquivo:
  txt = arquivo.read()
print(txt)

"""Exercício 9: Números Aleatórios
Crie um programa que gere um número aleatório entre 1 e 100 e peça ao usuário para adivinhar o número. Diga ao usuário se sua tentativa foi muito alta, muito baixa ou correta.
"""

import random

numero_secreto = random.randint(1, 100)

while True:
  try:
    numero_usuario:int = int(input("Adivinhe o número de 1 a 100: "))
    if numero_usuario < 1 or numero_usuario > 100:
      raise ValueError("Valor inválido, digite um valor válido de 1 a 100!")
    if numero_usuario < numero_secreto:
      print("Muito baixo!")
    elif numero_usuario > numero_secreto:
      print("Muito alto!")
    else:
      print("Acertou!")
      break
  except ValueError as e:
    print(f"Erro:, {e} \nDigite novamente.")

"""Exercício 10: While Loop
Escreva um programa que continue pedindo ao usuário um número até que ele digite 0. Quando ele digitar 0, o programa deve exibir a soma de todos os números digitados.
"""

soma: int = 0

while True:
    try:
        numero: int = int(input("Insira um número (0 para sair): "))
        if numero == 0:
            break
        else:
            soma += numero
    except ValueError as e:
        print(f"Erro: {e}. \nDigite novamente.")
print(f"A soma dos números é: {soma}")
# -*- coding: utf-8 -*-
"""Exercicios Python Aula 04

Exercício 1:
Percorra uma lista de nomes e imprima apenas aqueles que começam com a letra "A".
"""

nomes = ["Ana", "Carlos", "Amanda", "Bruno", "Alice", "Roberto", "Aline", "Fernanda", "Alberto", "Beatriz"]
for nome in nomes:
    if nome.startswith("A"):
      print(nome)

"""Exercício 2
Percorra uma lista de números e imprima a soma dos números que são múltiplos de 3.
"""

multiplos = 0
numeros = [4, 9, 15, 22, 33, 18, 40, 27, 12, 6]
for numero in numeros:
  if numero % 3 == 0:
   multiplos += numero
print(multiplos)

"""Exercício 3:
Percorra uma lista de palavras e imprima apenas aquelas que têm mais de 5 caracteres.
"""

palavras = ["python", "java", "c++", "javascript", "html", "css", "ruby", "swift"]
for palavra in palavras:
  if len(palavra) > 5:
    print(palavra)

"""Exercício 4:
Percorra uma lista de números e imprima apenas aqueles que são números primos.
"""

from sympy import isprime
numeros = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 13, 17, 19, 23, 24, 29, 30]
for numero in numeros:
  if isprime(numero):
    print(numero)

"""Exercício 5:
Percorra uma lista de números e imprima o maior e o menor número da lista.

Aqui está uma lista de números para usar:
"""

numeros = [12, 5, 8, 19, 22, 1, 34, 25, 3, 7, 9]
maior = numeros[0]
menor = numeros[0]
for numero in numeros:
  if numero > maior:
    maior = numero
  if numero < menor:
    menor = numero
print(f"O menor número é {menor}, o maior é {maior}.")

"""Exercício 6:
Percorra uma lista de strings e imprima a string mais longa.

Aqui está uma lista de strings para usar:
"""

palavras = ["banana", "apple", "watermelon", "cherry", "strawberries", "blueberry"]
maior = palavras[0]
for palavra in palavras:
  if len(palavra) > len(maior):
    maior = palavra
print(maior)

"""Exercício 7:
Percorra uma lista de números e imprima apenas aqueles que são números pares.

Aqui está uma lista de números para usar:
"""

numeros = [14, 23, 56, 78, 19, 30, 45, 92, 67, 84]
for numero in numeros:
  if numero % 2 == 0:
    print(numero)

"""Exercício 8:
Percorra uma lista de nomes e imprima a quantidade de nomes que começam com uma vogal.

Aqui está uma lista de nomes para usar:
"""

nomes = ["Ana", "Carlos", "Amanda", "Bruno", "Alice", "Roberto", "Aline", "Fernanda", "Alberto", "Beatriz"]
contador = 0
vogal = "aeiouAEIOU"
for nome in nomes:
  if nome[0] in vogal:
    contador += 1
print(contador)

"""Exercício 9:
Percorra uma lista de números e crie uma nova lista apenas com os números positivos.

Aqui está uma lista de números para usar:
"""

numeros = [-4, 3, -9, 15, -22, 33, -18, 40, -27, 12, -6]
positivos = []
for numero in numeros:
  if numero > 0:
    positivos.append(numero)
print(positivos)

"""Exercício 10:
Percorra uma lista de listas de números e imprima a soma de cada sublista.
"""

listas_de_numeros = [[1, 2, 3], [4, 5], [6, 7, 8, 9], [10, 11]]

for lista in listas_de_numeros:
  soma = 0
  for numero in lista:
    soma += numero
  print(f"A soma da {lista} é {soma}")

"""1. Lista de números ao quadrado"""

numeros = [1, 2, 3, 4, 5]
for numero in numeros:
    print(numero**2)

"""2. Modificar lista de linguagens"""

linguagens = ["Python", "Java", "C++", "JavaScript"]
linguagens.append("R")
print(linguagens)
linguagens.remove("Java")
print(linguagens)

livro = {"titulo": "1984", "autor": "George Orwell", "ano": 1949}
for chave, valor in livro.items():
    print(f"{chave}: {valor}")

"""3. Função para contar caracteres"""

def contar_caracteres(s):
    contagem = {}
    for caractere in s:
        contagem[caractere] = contagem.get(caractere, 0) + 1
    return contagem

print(contar_caracteres("engenharia de dados"))

"""4. Somando preços em listas"""

lista_compras = ["maçã", "banana", "cereja"]
precos = {"maçã": 0.45, "banana": 0.30, "cereja": 0.65}
total = sum(precos[item] for item in lista_compras)
print(f"Preço total: {total}")

"""5. Ordenação"""

pessoas = [
    {"nome": "Alice", "idade": 30},
     {"nome": "Carol", "idade": 20},
    {"nome": "Bob", "idade": 25},

]
pessoas.sort(key=lambda pessoa: pessoa["nome"])

print(pessoas)

"""6. For dentro de listas"""

valores = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
pares = [valor for valor in valores if valor % 2 == 0]
impares = [valor for valor in valores if valor % 2 != 0]
print(f"Os valores pares são: {pares} \n Os valores ímpares são: {impares}")

"""7. Contando caracteres"""

frase: str = "Engenharia de Dados"
contagem = {}
for letra in frase:
  if letra in contagem:
    contagem[letra] += 1
  else:
    contagem[letra] = 1
print(contagem)

def contar_caracteres(s):
    contagem = {}
    for caractere in s:
        contagem[caractere] = contagem.get(caractere, 0) + 1
    return contagem

print(contar_caracteres("Engenharia de Dados"))

"""8. Juntando Dicionários"""

dicionario1 = {"a": 1, "b": 2}
dicionario2 = {"c": 3, "d": 4}

dicionario_fundido = {**dicionario1, **dicionario2}

print(dicionario_fundido)

"""9. Filtragem de Dados em Dicionário"""

estoque = {"Teclado": 10, "Mouse": 0, "Monitor": 3, "CPU": 0}

estoque_positivo = {produto: quantidade for produto, quantidade in estoque.items() if quantidade > 0}

print(estoque_positivo)
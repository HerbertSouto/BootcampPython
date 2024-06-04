"""
Escreva uma função que receba uma lista de números e retorne a soma de todos os números.\

"""

def somar_lista(s):
  soma: int = 0
  numeros_somados: list = []
  for numero in s:
    soma += numero
  numeros_somados.append(soma)
  return(numeros_somados)
print(numeros_somados)

lista = [1,2,3,4,5,6,7,8,9,10,22,33,44,55,66]

somar_lista(lista)

"""Crie uma função que receba um número como argumento e retorne True se o número for primo e False caso contrário."""

def verificar_numero_primo(numero):
    if numero <= 1:
        return False
    for i in range(2, int(numero**0.5) + 1):
        if numero % i == 0:
            return False
    return True

numero = 5
if verificar_numero_primo(numero):
    print(f"{numero} é primo.")
else:
    print(f"{numero} não é primo.")

"""Desenvolva uma função que receba uma string como argumento e retorne essa string revertida."""

def inverter_palavra(i):
  palavra_invertida:str = i[::-1]
  return palavra_invertida
print(palavra_invertida)

inverter_palavra("dlroW olleH")

"""Implemente uma função que receba dois argumentos: uma lista de números e um número. A função deve retornar todas as combinações de pares na lista que somem ao número dado."""

def calcular_lista_valor (valor:int, lista:list):
  resultado = []
  for numero in lista:
    if (numero + valor) % 2 == 0:
      resultado.append(numero)
  print(resultado)

calcular_lista_valor(valor =1, lista=[1,2,3,4,6,7,8,9,10])

"""Escreva uma função que receba um dicionário e retorne uma lista de chaves ordenadas"""

def ordenador_dicionario(x):
  cadastro_ordenado = sorted(x)
  print(cadastro_ordenado)

dados = {
    "01:Adriano",
    "03:Mariana",
    "04:Luciano",
    "02:Fabiana",
    "05:José",
    "07:Lúcio",
    "06:Marlo",
    "08:Fábio",
}
ordenador_dicionario(dados)

"""**DESAFIO:** Refatorar nosso código usando Dicionário, Type Hint e Funcões."""

def cadastrar_usuario():

  nomeLoop:bool = False
  salarioLoop:bool = False
  bonusLoop:bool = False
  COMISSAO_FIXA:int = 1000

  usuarios:dict ={}

  while not nomeLoop:
      try:
          nome_usuario:str = input("Digite seu nome: ")
          if not nome_usuario.isalpha():
              raise ValueError("O nome deve conter apenas letras.")
          else:
              usuarios['nome'] = nome_usuario
              nomeLoop = True
      except ValueError as e:
          print("Erro:", e)

  while not salarioLoop:
      try:
          salario:float = input("Digite seu salário: ")
          salario = float(salario)  # Tenta converter a entrada para float
          if salario is not float(salario):
              raise ValueError("O nome deve conter apenas números.")
          else:
              usuarios['salario'] = salario
              salarioLoop = True
      except ValueError as e:
          print("Erro:", e)

  while not bonusLoop:
      try:
          bonus:float = input("Digite o valor do seu bônus: ")
          bonus = float(bonus)  # Tenta converter a entrada para float
          if bonus is not float(bonus):
              raise ValueError("O nome deve conter apenas números.")
          else:
              usuarios['bonus'] = bonus
              bonusLoop = True
              salario_bonado:float = COMISSAO_FIXA + salario * bonus
              usuarios['salario_bonado'] = salario_bonado
              print(f"Olá, {nome_usuario}! Seu salário é {salario}, o bônus foi de {bonus}, salário bonificado é de: {salario_bonado}")
      except ValueError as e:
          print("Erro:", e)

  return usuarios

dados_usuario = cadastrar_usuario()
print(dados_usuario)
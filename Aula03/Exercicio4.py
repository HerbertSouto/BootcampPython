

#Exercício 4: Detecção de Anomalias em Dados de Transações Você está trabalhando em um sistema de detecção de fraude e precisa identificar transações suspeitas. Uma transação é considerada suspeita se o valor for superior a R$ 10.000 ou se ocorrer fora do horário comercial (antes das 9h ou depois das 18h). Dada uma transação como transacao = {'valor': 12000, 'hora': 20}, verifique se ela é suspeita.

import re

usuario_invalido = True

while usuario_invalido:
    try:
        nome_usuario = input("Digite seu usuário: ")
        usuario_str = str(nome_usuario)
        if not re.search("[a-zA-Z]", nome_usuario):
            raise ValueError("O campo deve conter pelo menos uma letra.")
        usuario_invalido = False
    except ValueError as e:
     print(e)

valor_invalido = True    

while valor_invalido:
      try:
          valor = float(input('Digite o valor:' ))
          valor_flt = float(valor)
          if valor_flt < 0:
            raise ValueError("Valor Negativo")
          valor_invalido = False
      except ValueError:
          print("Valor inválido")

hora_invalida = True

while hora_invalida:
    try:
        hora = int(input('Digite a hora: '))
        if hora < 0:
            raise ValueError("Hora inválida")
        hora_invalida = False
    except ValueError as e:
        print(e)

if valor_flt > 10000 or hora < 9 or hora > 18:
  print("Transação suspeita")
else:
  print("Transação ok")      
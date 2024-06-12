nomeLoop = False
salarioLoop = False
bonusLoop = False
COMISSAO_FIXA = 1000

while not nomeLoop:
    try:
        nome_usuario = input("Digite seu nome: ")
        if not nome_usuario.isalpha():
            raise ValueError("O nome deve conter apenas letras.")
        else:
            nomeLoop = True
    except ValueError as e:
        print("Erro:", e)

while not salarioLoop:
    try:
        salario = input("Digite seu salário: ")
        salario = float(salario)  # Tenta converter a entrada para float
        if salario is not float(salario):
            raise ValueError("O nome deve conter apenas números.")
        else:
            salarioLoop = True
    except ValueError as e:
        print("Erro:", e)

while not bonusLoop:
    try:
        bonus = input("Digite o valor do seu bônus: ")
        bonus = float(bonus)  # Tenta converter a entrada para float
        if bonus is not float(bonus):
            raise ValueError("O nome deve conter apenas números.")
        else:
            bonusLoop = True
            salario_bonado = COMISSAO_FIXA + salario * bonus
            print(
                f"Olá, {nome_usuario}! Seu salário é {salario}, o bônus foi de {bonus}, salário bonificado é de: {salario_bonado}"
            )

    except ValueError as e:
        print("Erro:", e)

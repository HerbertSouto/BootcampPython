#Exercício 2: Classificação de Dados de Sensor

#Imagine que você está trabalhando com dados de sensores IoT. Os dados incluem medições de temperatura. Você precisa classificar cada leitura como 'Baixa', 'Normal' ou 'Alta'. Considerando que:

#Temperatura < 18°C é 'Baixa'
#Temperatura >= 18°C e <= 26°C é 'Normal'
#Temperatura > 26°C é 'Alta'

temp = False

while not temp:
    try:
        temperatura = float(input('Digite a temperatura:' ))
        temp_flt = float(temperatura)
        temp = True
    except ValueError:
        print("Valor inválido")
if temperatura < 18:
    print(f"A temperatura {temperatura}°C é considerada baixa")
elif temperatura >= 18 and temperatura <= 26:
    print(f"A temperatura {temperatura}°C é considerada normal")
elif temperatura > 26:
    print(f"A temperatura {temperatura}°C é considerada alta")   
from datetime import datetime, timedelta

# criando data e hora

# data = datetime(2025, 3, 19, 13, 30)

# data += timedelta(weeks = 1)
# print(data)

data_atual = datetime.now()

menu = """
Selecione o tipo de carro:
P - Pequeno
M - Medio
G - Grande
->"""
tipo_carro = input(menu) # p, m ou g
tempo_peq = 30
tempo_med = 45
tempo_gra = 60

if tipo_carro == 'P':
    data_estimada = data_atual + timedelta(minutes = tempo_peq)
    print(f'o carro chegou: {data_atual} e ficará pronto às {data_estimada}')
    
elif tipo_carro == 'M':
    data_estimada = data_atual + timedelta(minutes = tempo_med)
    print(f'o carro chegou: {data_atual} e ficará pronto às {data_estimada}')
    
elif tipo_carro == 'G':
    data_estimada = data_atual + timedelta(minutes = tempo_gra)
    print(f'o carro chegou: {data_atual} e ficará pronto às {data_estimada}')
else:
    pass
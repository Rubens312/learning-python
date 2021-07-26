import random

def function():
    pesos = []
    for i in range(5):
        pesos.append(float(input(f'{i + 1}° Pessoa, Peso: ')))
    pesos.sort()
    # print(pesos)
    print(f'O maior peso lido foi {pesos[4]} e o menor peso lido foi {pesos[0]}')

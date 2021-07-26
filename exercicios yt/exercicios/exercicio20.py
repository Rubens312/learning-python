import random

def function():
    i = 0
    lista = []
    for i in range(6):
        lista.append(input('Candidato: '))

    random.shuffle(lista)
    print(lista)

from random import randint


def function():
    lista = []
    i = 0
    for i in range(6):
        lista.append(input(f'Aluno {i + 1}: '))

    i = randint(0, 6)
    print(f'O vencedor do sorteio foi {lista[i]}')

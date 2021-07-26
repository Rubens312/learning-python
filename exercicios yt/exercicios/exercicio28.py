from random import randint


def function():
    print(30*'-=')
    print('Estou pensando em um número entre 0 e 5')
    print(30*'-=')
    tentativa = float(input('Adivinhe o numero que eu pensei: '))
    numero = randint(0,5)
    print('parabéns, você acertou...') if numero == tentativa else print(f'Eu pensei em {numero}, errou bonito trouxa!!!')

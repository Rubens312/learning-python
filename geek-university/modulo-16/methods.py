# stoy a morrer pero tengo que continuar
# methods()

class Lampada:
    def __init__(self, cor, voltagem, luminosidade):
        self.cor = cor
        self.voltagem = voltagem
        self.luminosidade = luminosidade

    def metodo(self):
        print('Métodos são funções')


lamp = Lampada('azul', 220, 1800)
lamp.metodo()
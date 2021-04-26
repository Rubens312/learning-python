class Lampada:
    def __init__(self, voltagem, cor):
        self.voltagem = voltagem
        self.cor = cor

lamp = Lampada(220, 'azul')

print(lamp.cor)
print(lamp.voltagem)
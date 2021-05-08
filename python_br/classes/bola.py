class Bola:
    cor = 'azul'
    circunferencia = 5
    material = 'couro'

    def muda_cor(self):
        self.cor = input('Insira a nova cor da bola: ')

    def mostra_cor(self):
        print(self.cor)


Futebol = Bola()

Futebol.muda_cor()
Futebol.mostra_cor()
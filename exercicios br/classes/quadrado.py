class Square:
    def __init__(self, lado):
        self.lado = lado

    def changeSide(self):
        self.lado = float(input('Insira o novo valor do lado'))
    
    def returnSide(self):
        return self.lado
    
    def squareArea(self):
        return self.lado**2

Quadrado = Square(4)

Quadrado.changeSide()
print(Quadrado.returnSide())
print(Quadrado.squareArea())
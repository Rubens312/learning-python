class Retangle:
    def __init__(self, height, width):
        self.height = height
        self.width = width
    
    def retangleArea(self):
        return self.height * self.width
    
    def retanglePerimeter(self):
        return 2 * (self.height + self.width)

    def returnSides(self):
        height_width = [self.height, self.width]
    
width = float(input('Insira uma das dimensões do local: '))
height = float(input('Insira a outra dimensão: '))

Local = Retangle(height, width)

print(f'Você vai precisar de {Local.retangleArea()} ladrilhos de 1x1m para o chão')
print(f'Você vai precisar de {Local.retanglePerimeter()} ladrilhos 1x1 para o rodapé do local')
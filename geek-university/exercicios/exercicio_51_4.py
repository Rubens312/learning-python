def raio(x, y):
    r = (x ** 2 + y ** 2)**(1/2)
    return r

x = float(input('Insira a coordenada x: '))
y = float(input('Insira a coordenada y: '))

print(f'O ponto está à {raio(x, y)} de distância do ponto (0, 0)')
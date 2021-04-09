def function():
    largura = float(input('Largura da parede: '))
    altura = float(input('Altura da parede: '))
    area = largura * altura
    litros_tinta = area/2
    print(f'A sua parede de dimensões {largura}m X {altura}m possui {area}m^2 de área. Para pinta-la, serão necessarios {litros_tinta}l de tinta para pinta-la')
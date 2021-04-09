def function():
    distancia = float(input('Km percorridos com o carro: '))
    dias = int(input('Dias com o carro: '))
    valor = 60 * dias + 0.15 * distancia

    print(f'Valor a pagar: R${valor:.2f}')

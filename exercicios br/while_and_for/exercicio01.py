numero = None
while True:
    try:
        numero = float(input('numero de 1 à 10: '))
    except ValueError:
        print('Valor invalido')
    if numero != None:
        if 1 <= numero <= 10:
            print(numero)
            break
        else:
            print('Numero invalido')

    
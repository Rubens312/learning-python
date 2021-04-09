def function():
    distancia = float(input('Distancia a se percorrer: '))
    print(f'O valor por essa disância é: R${distancia*0.5:.2f}') if distancia <=200 else print(f'O valor por essa disância é: R${distancia*0.45:.2f}')
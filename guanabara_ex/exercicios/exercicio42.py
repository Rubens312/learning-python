from exercicios import exercicio35
def function():
    primeirolado = float(input('Primeiro lado: '))
    segundolado = float(input('Segundo lado: '))
    terceirolado = float(input('Terceiro lado: '))
    conti = exercicio35.function(primeirolado, segundolado, terceirolado)
    if conti == True:
        if primeirolado == segundolado == terceirolado:
            print('É um triangulo equilatero')
        elif primeirolado == segundolado or primeirolado == terceirolado or segundolado == terceirolado:
            print('É um triângulo isosceles')
        else:
            print('é um triangulo escaleno')
    
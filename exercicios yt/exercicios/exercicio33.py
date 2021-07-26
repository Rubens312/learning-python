def function():
    a = float(input('Primeiro número: '))
    b = float(input('Segundo número: '))
    c = float(input('Terceiro número: '))

    if a > b and a > c:
        print('O primeiro valor é o maior')
    elif b > a and b > c:
        print('O segundo valor é o maior')
    elif c>a and c>b:
        print('O terceiro é o maior')
    else:
        print('Não existe maior valor dentre os 3')

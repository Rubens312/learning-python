def function():
    ano = int(input('Informe o ano: '))
    if ano%4 == 0 and ano%100!= 0:
        print('é bissexto')
    else:
        print('Não é bissexto')
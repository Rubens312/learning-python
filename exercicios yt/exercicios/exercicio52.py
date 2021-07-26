def function():
    valor = int(input('Número: '))
    i = 1
    j = 1
    teste = True
    for i in range(2, valor -1):
        if valor%i == 0:
            print('Não é um número primo')
            print(i)
            teste = False
            break
    
    if teste:
        print('É um número primo')

    # for i in range(3, 99999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999):
    #     teste = True
    #     for j in range(2, i - 1):
    #         if i%j == 0:
    #             teste = False
    #             break
    #     if teste:
    #         print(i)    
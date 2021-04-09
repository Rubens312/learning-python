def function(lado1, lado2, lado3):
    # lado1 = float(input('Primeira reta: '))
    # lado2 = float(input('Segunda reta: '))
    # lado3 = float(input('Terceira reta: '))

    if lado1 > lado2 + lado3 or lado2 > lado1 + lado3 or lado3 > lado1 + lado2:
        print('Essas três retas não podem formar um triângulo')
    else:
        # print('essas três retas podem formar um triangulo')
        conti = True
        return conti

def quantos_anos(A, B, crescimento_A, crescimento_B):
    anos = 0
    while B > A:
        anos +=1
        A = A + A*3/100
        B = B + B*1.5/100

    return anos

A = int(input('Numero de habitantes da menor cidade: '))
crescimento_A = float(input('Taxa de crescimento dela: '))
B = int(input('Numero de habitantes na maior cidade: '))
crescimento_B = float(input('Taxa de crescimento da segunda cidade'))

quantos_anos_demora = quantos_anos(A, B, crescimento_A, crescimento_B)
print(quantos_anos_demora)
def salario(salario=1000):
    correcao = 1.5/100
    for i in range(26):
        salario += salario * correcao
        # print(salario)
        correcao += correcao
    return salario

print(salario())
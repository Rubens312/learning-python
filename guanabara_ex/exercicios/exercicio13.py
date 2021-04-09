def function():
    salario = float(input('Salario antes do reajuste: '))
    porcentagem = float(input('Porcentagem de reajuste: '))
    reajustado = salario + salario * porcentagem/100
    print(f'O salario após o reajuste é igual a {reajustado}')
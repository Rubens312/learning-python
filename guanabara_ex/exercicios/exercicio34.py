def function():
    salario = float(input('Salario atual: '))
    if salario >= 1250:
        print(f'O novo salario é: {salario + salario/10}')
    else:
        print(f'O novo salario é de: {salario + salario*15/100}')

def exercicio51(n):
    soma = 0
    x = 0
    y = 1
    for i in range (1, n + 1):
        x = i
        # print(f'{x}/{y}')
        soma = soma + x/y
        y = y + 2
    return soma

n = int(input('Insira até que termo quer que a sequencia vá: '))
print(exercicio51(n))
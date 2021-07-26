x = int(input('Valor inicial: '))
y = int(input('Valor inicial: '))
soma = 0
for i in range(x, y + 1):
    soma += i
    print(i, end=', ')
print()
print(soma)
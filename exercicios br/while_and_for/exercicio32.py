fatorial = int(input('Número: '))
print(f'{fatorial}! = {fatorial} . ', end='')
for i in range(fatorial - 1, 1, -1):
    fatorial = fatorial * i
    print(i, end=' . ')
print(f'1 = {fatorial}')




lista = []
vogais = ('a', 'e', 'i', 'o', 'u')
result = 0
for i in range(10):
    tester = True
    lista.append(input('Item: '))
    for letra in vogais:
        if lista[i] == letra:
            tester = False
            break
    if tester:
        result += 1
print(result)

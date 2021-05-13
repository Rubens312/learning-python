base = int(input('Base: '))
expoente = int(input('Expoente: '))
result = 1
for i in range(expoente):
    result = result*base
print(result)
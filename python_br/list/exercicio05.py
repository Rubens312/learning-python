vetor_geral = []
impares = []
pares = []
for i in range(20):
    numero = int(input('Número: '))
    vetor_geral.append(numero)
    if not numero % 2:
        pares.append(numero)
    else:
        impares.append(numero)

print(vetor_geral)
print(impares)
print(pares)
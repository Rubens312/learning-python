notas = []
for i in range(4):
    notas.append(float(input('Nota: ')))

print(f'Média: {sum(notas)/len(notas)}')
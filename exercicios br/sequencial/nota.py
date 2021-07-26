notas = []
for i in range(4):
    notas.append(float(input('Insira a nota do aluno: ')))

media = sum(notas)/len(notas)
print(f'A média do aluno foi: {media}')
alunos = []
counter = 0
for i in range(10):
    nota = 0
    for j in range(4):
        nota += float(input(f'Nota {j + 1}: '))/4
    alunos.append(nota)
    if nota >= 7:
        counter += 1
print(counter)

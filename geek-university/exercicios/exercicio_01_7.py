def read_matrix():
    matrix = []
    soma = 0
    for i in range(4):
        item = []
        for j in range(4):
            item.append(float(input(f'Insira o {j + 1}° item da linha {i + 1}: ')))
            if item[j] > 10:
                soma = soma + 1
        matrix.append(item)
    return soma

# def print_matrix(matriz):
#     for i in range(len(matriz)):
#         for item in matriz[i]:
#             print(item, end=' ')
#         print()
# print_matrix(read_matrix())

print(read_matrix())
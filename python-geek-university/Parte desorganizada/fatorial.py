quantidade_de_fatoriais = int(input('Quantidade de fatoriais '))
lista_de_fatoriais = [1]
for i in range(2, quantidade_de_fatoriais + 1):
    lista_de_fatoriais.append(i * lista_de_fatoriais[i - 2])

print(lista_de_fatoriais)
# fatorial = 1
# for i in range(1, 200):
#     fatorial = i * fatorial

# print(fatorial)
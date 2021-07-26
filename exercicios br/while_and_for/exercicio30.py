preco = float(input('Preço: '))
for i in range(1, 51):
    print(f'{i} produtos = R$: {i * preco:.2f}')
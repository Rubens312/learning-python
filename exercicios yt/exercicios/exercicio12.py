def function():
    preco = float(input('Preço do produto: '))
    reajustado = preco - preco/20
    print(f'O valor do produto após o reajuste de 5% é: {reajustado}')
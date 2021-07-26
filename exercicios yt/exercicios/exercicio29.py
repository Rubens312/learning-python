def function():
    velocidade = float(input('Velocidade do veículo: '))
    print('Tudo certo, dentro do limite') if velocidade <= 80 else print(f'Você está acima da velocidade, vai ser multado em: R$:{(velocidade - 80)*7:.2f}')
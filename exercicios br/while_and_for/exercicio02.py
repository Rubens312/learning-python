nome = input('Nome: ')
senha = input('Senha: ')
while senha == nome:
    print('Error(Senha não pode ser igual ao nome)')
    senha = input('Senha: ')
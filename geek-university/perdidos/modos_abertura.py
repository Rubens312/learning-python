# Que sono meu parceiro, estou completamente sem energia pleas 14:10
# Mas vamos lá
# Open('nome_do_arquivo.extencao', 'x') funciona apenas para criar um novo arquivo e em seguida escrever nele, ou seja, não funciona para arquivos que já existem
# Open('nome_do_arquivo.extencao', 'a') Funciona para que adicione escritas no arquivo apenas no final dele, ou seja anexa conteúdo. appending to the end of the file if it exists

# with(open('novo_arquivo.txt', 'a')) as novo_arquivo:
#     novo_arquivo.write('Teste bem sucedido?\n Sim!\n')

# Estava testando para ver se iria funcionar com um arquivo que não existia antes. Funcionou.

# with(open('novo_arquivo.txt', 'a')) as file:
#     file.seek(0)
#     file.write('não rolou \n')

# Meu professor é um retardado e ao invés de checar antes decidiu testar enquanto ensinava e eu decidi testar também
# Mas basicamente esse modo de escrita não funciona com base no cursor, ele apenas adiciona tudo no final.

# with(open('novo_arquivo.txt', 'w+')) as file:
#     file.seek(0)
#     file.write('Testando novamente \n ')

# Continua substituindo o conteudo mesmo com o +

with(open('novo_arquivo.txt', 'r+')) as file:
    file.seek(0)
    file.write('tentado novamente novamente \n')
    file.seek(0)
    file.write('Uma terceira vez \n')
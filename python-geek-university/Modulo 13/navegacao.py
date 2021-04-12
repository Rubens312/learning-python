'''
Sistemas de arquivos - Navegação

Para manipular arquivos do sistema operacional, necessitamos importar o módulo OS

'''
import os

# teste = os.getcwd()
# # Pegando o diretório do arquivo onde estamos

# print(teste)

# # print('hello world')

# os.chdir('..')

# print(os.getcwd())

# os.chdir('..')

# print(os.getcwd())

# os.chdir('..')

# print(os.getcwd())

# os.chdir('..')

# print(os.getcwd())

# os.chdir('..')
# # operational sistem . change directory

# print(os.getcwd())

# print(os.path.isabs('C:\\Users '))
# Verificando se o path é absoluto
# Utilizar dupla barra contraria a fim de identificar que é uma barra contraria e não caracter de scape


print(os.getcwd())

os.chdir('../../')

print(os.getcwd())

res = os.path.join(os.getcwd(), 'GitHub')

os.chdir(res)

print(os.getcwd())
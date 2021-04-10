# A função seek() é utilizada para mover o cursor dentro do texto

file = open('exemplo.txt')

file.read()

file.seek(2)

# print(file.read())

# Como é de se esperar por ser uma string o seek está fazendo algo similar a trabalhar com uma string
# exemplo = 'Texto aleatório'

# print(exemplo[0])

file.seek(0)

# print(file.readline())

# Readline lê apenas uma linha, como voce deve estar chocado em saber

# print(file.readlines(132))

file.close() #Essa função fecha a conexão com o arquivo 
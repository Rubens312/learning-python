# With é um bloco que fecha automaticamente o item solicitado após o fim do bloco

with open('exemplo.txt') as File:
    # print(File.read())
    five_o_five = File.read()

# print(File.read())
print(five_o_five)

# O with está recebedo um arquivo, esse arquivo pode ser chamado de contexto do bloco
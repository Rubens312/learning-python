# Lambdas são funções anônimas

# mult = lambda x: x * 3

# print(mult(16))

# teste = lambda *args: args

# print(teste('joao', 'julio', 'leonardo'))
# *args funciona em lambdas

lista = ['Nome Sobrenome', 'Rubens Kaiserman', 'Mariana Avelina', 'Rafaelly Dias', 'Julio Cesar']
lista.sort(key = lambda sobrenome: sobrenome.split(' ')[-1].lower())
print(lista)
# Vamos tentar traduzir isso aqui, enfim:
# O key é o parametro que define a chave para a ordenação do conteúdo
# daí o key recebe uma função anonima
# A função anonima por sua vez recebe um parametro que é o 'sobrenome'
# mas na realidade o parametro é o termo da lista
# Daí a função retorna a chave como sendo o termo da lista separado em uma outra lista com os dois nomes, daí vem o ultimo termo
# coloca em lower bonitinho
# essa vai ser a key do comparativo o segundo nome
# minha logica pra fazer isso em linhas de codigo faria utilizar muitas linhas, aiai

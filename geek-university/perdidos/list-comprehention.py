lista = [1,2,3,4,5,6,7,8,9,10]

# print(lista*3) Jeito errado, isso vai repetir os itens da lista 3 vezes
resultado = [numero * 3 for numero in lista]
print(resultado)


# o 'numero' é a forma de chamar o termo da lista, creio que possa ser qualquer nome, enfim isso quer dizer, para cada numero presente na lista, apresente o item multiplicado por 3
# traduzindo:

# resultado = []
# for i in range(len(lista)):
#    resultado.append(lista[i]*3)
# print(resultado)

# é o que é realizado

nome = 'Rubens Guedes Kaiserman'
print(nome.upper())
upado = [letra.upper() for letra in nome]
print(upado)

# Esse é basicamente um meio de fazer um loop for em uma linha só, bacaninha
from collections import Counter

lista = [1,1,1,1,1,1,1,1,1,1,1,1,23,2,2,2,2,2,2,23,3,3,3,3,3,3,7,6,6,6,7,7,3,8,7,6,5]

# teste = Counter(lista)

# print(teste)

# Achei interessante poder montar um mapa com a quantidade de ocorrencia de cada termo, isso pode ter várias utilidades

# no_repeat_list = list(set(lista))
# final_list = []
# for i in range(len(no_repeat_list)):
#     variavel_qualquer = (no_repeat_list[i], lista.count(no_repeat_list[i]))
#     final_list.append(variavel_qualquer)

# print(dict(final_list))
print(Counter(lista))

# Acabei fazendo a função Counter por conta própria, enfim, funciona menos a parte de colocar os elementos em ordem, mas enfim. acabou ficando em ordem crescente por key e não por valor

# pra ele strings também são listas
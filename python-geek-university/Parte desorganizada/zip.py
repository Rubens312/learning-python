lista01 = [1,3,5,7,9]
lista02 = [2,4,6,8,10,11,12]
lista03 = [100,200,300,400,500]

zipado = list(zip(lista01, lista02,lista03))

print(zipado)
# basicamente pega os termos das listas com mesmo indice e coloca em uma tupla, e forma uma lisrta com essass tuplas
# se houver mais termos em uma lista do que em outra os excedentes são ignorados
# é possivel adicionar mais de duas listas para o zip

deszipado = list(zip(*zipado))
# o '*' deszipa o conteúdo assim podendo converter para uma lista de tuplas onde cada tupla é composta por uma das listas antes de zipar
print(deszipado)
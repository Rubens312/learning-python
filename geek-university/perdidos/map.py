import math

# raios = [1,2,3,4]

# def area_circulo(r):
#     return r ** 2 * math.pi

# mapa_de_areas = map(area_circulo, raios)

# print(mapa_de_areas)
# print(list(mapa_de_areas))
# print(list(mapa_de_areas)) #se tentar repetir o processo ele irá apresetar uma lista vazia

# lista_de_areas = list(map(area_circulo, raios)) #portanto vale a pena salvar a lista em uma váriavel
# print(lista_de_areas)
# print(lista_de_areas)

# areas = []
# for r in raios:
#     areas.append(area_circulo(r))

# print(areas)

cidades = [('Berlim', -60), ('Londres', 12), ('Mexico', 34), ('Brasil', 27)]

celcios_kelvin = list(map(lambda termo: (termo[0], termo[1] + 273), cidades))

print(celcios_kelvin)
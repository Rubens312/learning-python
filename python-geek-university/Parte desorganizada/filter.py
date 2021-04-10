# import statistics

# val = []
# for i in range(1,21):
#     val.append(i)

# tuple_val = tuple(val)
# # mid = sum(tuple_val)/len(tuple_val)
# mean = statistics.mean(val)

# # val = []
# # for i in range(len(tuple_val)):
# #     if tuple_val[i] > mean:
# #         val.append(tuple_val[i])
# # Acima vemos a versão verbosa do que temos em baixo

# val = list(filter(lambda dado: dado > mean, tuple_val))
# # versão menos verbosa

# print(val)

# paises = ['Brasil', '', 'EUA', '', 'Canadá', 'Austrália', 'Mexico', '', '', '', 'Alemanha']
# print(paises)

# # paises = list(filter(lambda pais: pais != '', paises)) Versão não verbosa verbosa
# paises = list(filter(None, paises))# Versão não verbosa
# print(paises)

dados = [{'usuario': 'Rubens', 'twites': ['LOL', 'lasanha']},
{'usuario': 'Lanjer', 'twites': ['LOL', 'Cateau']},
{'usuario': 'la vie', 'twites': ['Pogchamps', 'lasanha']},
{'usuario': 'en rose', 'twites': []},
{'usuario': 'Starboy', 'twites': ['The', 'Weeknd']},
{'usuario': 'Fifty', 'twites': ['shades', 'of grey']},
{'usuario': 'twenty', 'twites': []}]

ativos = list(filter(lambda dado: dado['twites'] != [], dados))

print(ativos)
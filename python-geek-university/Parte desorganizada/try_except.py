# test = True
# while test:
#     try: 
#         value = int(input('Insira um valor numerico: '))
#         print('Valor numerico recebido')
#         test = False
#     except:
#         print('O valor adicionado não é numérico')
#         print()
#         res = input('Deseja tentar novamente? ')
#         if res != 'Sim':
#             test = False

try:
    len(99)
except NameError:
    print('A função solicitada não tem o nome reconhecido')
except TypeError as err:
    print(f'O código gerou o seguinte erro: {err}')

# O except funciona como um switch case de erros, o except é um default, caso algum erro aconteceu mas você não sabe qual foi, e pode-se dar uma resposta para cada tipo de erro
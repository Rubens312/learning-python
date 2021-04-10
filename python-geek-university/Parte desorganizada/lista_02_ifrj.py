# valor = int(input('Insira um valor inteiro: '))
# print('É par') if valor % 2 == 0 else print('É impar')

# primeiro_numero = float(input('Insira o primeiro número: '))
# segundo_numero = float(input('Insira o segundo numero: '))

# if primeiro_numero > segundo_numero:
#     print(f'O primeiro número({primeiro_numero}) é maior')
# elif primeiro_numero == segundo_numero:
#     print(f'Os números são iguais')
# else:
#     print(f'O segundo número({segundo_numero}) é maior')

# valores = []
# for i in range(3):
#     valores.append(float(input(f'Insira o {i + 1}° valor: ')))
# print(f'O maior valor digitado foi: {max(valores)}')

# notas = []

# for i in range(3):
#     notas.append(float(input(f'Insira a {i + 1}° nota do aluno: ')))

# media = sum(notas)/len(notas)

# if media >= 7:
#     print(f'O aluno foi aprovado com media {media:.1f}')
# elif 3 < media < 7:
#     print(f'O aluno fará prova final pois teve média {media:.1f}')
# else:
#     print(f'Aluno reprovado pois teve média {media:.1f}')

# primeiro_valor = float(input('Insira o primeiro número: '))
# segundo_valor = float(input('Insira o segundo número: '))
# terceiro_valor = float(input('Insira o terceiro número: '))

# if primeiro_valor == segundo_valor == terceiro_valor:
#     print('Todos os valores são iguais')
# elif primeiro_valor != segundo_valor != terceiro_valor:
#     print('São todos diferentes')
# else:
#     print('Dois deles são iguais')

# valores = []
# for i in range(3):
#     valores.append(float(input(f'Insira o {i + 1}° numero: ')))
# print(f'A média entre o maior e o menor número é: {(min(valores) + max(valores))/2}')
# valores.sort()
# print(f'O valor do meio é: {valores[1]}')

# valores = []
# for i in range(3):
#    valores.append(float(input(f'Insira o {i + 1}° valor'))) 
# valores.sort()
# valores.reverse()

# for valor in valores:
#     print(valor)

# from datetime import date

# data_atual = date.today()
# data = date(data_atual.year, data_atual.month, data_atual.day)

# ingresso = float(input('Valor do ingresso: '))

# idade = int(input('Idade do cliente: '))

# if data.weekday():
#     if idade > 65 or idade < 12:
#         valor_final = ingresso - (ingresso*0.6)
#     else:
#         valor_final = ingresso - (ingresso*0.35)
# else:
#     if idade > 65 or idade < 12:
#         valor_final = ingresso - (ingresso*0.4)
#     else:
#         valor_final = ingresso - (ingresso*0.05)

# print(f'O valor final do ingresso: {valor_final}')
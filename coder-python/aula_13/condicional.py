print('''Apenas uma estrutura comum.
Notas importantes: sem () e sem {}, apenas com  :
Ex:
if variavel operador valor ou outra variavel == true:
    ação determinada
elif variavel operador valor ou outra variavel == true:
    Operação
else:
    operação se não for nenhum dos casos
    
    exemplo abaixo de uma estrutura com 4 casos, cada caso printando um ciclo
    ''')

i = 0
j = 20
k = 40
l = 60

for i in range(80):
    if i < 20:
        print('Primeiro ciclo')
    elif i <40:
        print('Segundo ciclo')
    elif i <60:
        print('Terceiro ciclo')
    else:
        print('Ultimo ciclo')

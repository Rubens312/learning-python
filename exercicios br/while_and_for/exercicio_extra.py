numero = int(input('Número: '))
teste = True
count = 0
if 0 < numero < 3:
    print('Ele é primo')
    print('foram realizadas 0 divisões')
elif numero > 3:
    if numero % 2 == 0:
        print('Ele não é primo')
        print('Foi necessária 1 divisão para determinar')
    else:
        for i in range(3, numero//2 + 1, 2):
            count +=1
            if numero % i == 0:
                print(f'Não é primo. Foram necessárias {count} divisões para determinar')
                teste = False
                break
        if teste == True:
            print(f'O número é primo, {count} divisões foram necessárias para descobrir')
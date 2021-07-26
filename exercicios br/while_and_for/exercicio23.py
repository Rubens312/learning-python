num = int(input('Número: '))
for i in range(1, num + 1):
    if i < 3:
        print(i)
        print('Foram necessárias 0 divisões para determinar')
    else:
        count = 0
        test = True
        if i % 2:
            for j in range(3, i//3 + 1, 2):
                count += 1
                if not i % j: 
                    test = False
                    break
            if test:
                print(f'{i} É primo')
                print(f'Foram necessárias {count} divisões para determinar')

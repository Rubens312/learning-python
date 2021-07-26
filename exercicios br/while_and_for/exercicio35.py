limite = int(input('limite: '))
for i in range(1, limite + 1):
    if i < 4:
        print(i, end=' ,')
    else:
        validator = True
        if i % 2: 
            for j in range(3, i//3 + 1, 2):
                if i % j == 0:
                    validator = False
                    break
            if validator:
                print(i, end=', ')
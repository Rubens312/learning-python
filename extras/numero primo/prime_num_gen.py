num = []
prime_number =[]
size = 100001
prime_num = []
for i in range(2, size):
    num.append(i)

for number in num:
    for numero in num:
        if number != numero:
            if not numero % number:
                del(num[num.index(numero)])

print(num)

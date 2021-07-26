prime_num = [1, 2, 3, 5, 7, 11]
for i in range(13, 1000000, 2):
    even = False
    for j in range(2, int(i/3 + 1)):
        if not i % j:
            even = True
            break
    if not even: 
        prime_num.append(i)

print(prime_num)

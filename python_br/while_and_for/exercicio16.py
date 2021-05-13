fibonacci = [1,1]
while fibonacci[-1] < 500:
    fibonacci.append(fibonacci[-1] + fibonacci[-2])
print(fibonacci)
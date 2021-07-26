for a in range(100, 1000):
    for b in range(100, 1000):
        if list(str(a * b)) == list(reversed(list(str(a * b)))):
            palindromo = a * b

print(palindromo)

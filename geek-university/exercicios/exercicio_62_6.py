from num2words import num2words

soma = 0
for num in range(1, 1001):
    soma = soma + len(num2words(num, lang='pt_BR'))

print(soma)

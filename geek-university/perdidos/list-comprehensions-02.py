# Também é possível utilizar códigos condicionais em listas
lista = []
for i in range(100):
    lista.append(i)

resultado = [numero for numero in lista if numero % 2 == 0]

print(resultado)

def soma(a, b):
    return  a + b

def sub(a, b):
    return a - b

def mult(a, b):
    return a * b

def op(a, b, function):
    return function(a, b)


print(op(99,2, mult))

# Funções de maior grandeza são funções que podem receber outras funções como parametro ou retornar funções
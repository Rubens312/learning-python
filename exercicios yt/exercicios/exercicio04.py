def function():
    valor = input('Digite algo: ')
    print(type(valor))
    print(valor.isalnum())
    print(valor.isalpha())
    print(valor.isspace())
    # Para pegar os atributos de uma váriavel basta usar o método is, que irá determinar isso para você.
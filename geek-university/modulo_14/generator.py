'''
Aparentemente o generator é baseado na palavra reservada yield
Aparentemente o que isso significa
Quando você utiliza o yeild você realiza um retorno da função
Se ssa função for chamada novamente, ela dará o retorno que viria na sequencia daquela função

Funciona similarmente a um cursor
Quando o yield é chamado, você sai da função e o cursor ficaria parado ali
Se é chamada a função novamente, ela continua na linha seguinte ao yield chamado anteriormente

OK, não é o que eu acabei de dizer. aparentemente a explicação que recebi estava mal formulada para variar.

O que o yield faz é retornar um objeto do tipo iteravel que contem todos os iterados dentro da função. como no exemplo abaixo que ele retorna um objeto com uma sequencia de 0 à 98

'''

def conte_ate():
    i = 0
    while i < 99:
        yield i 
        i = i + 1


testando = iter(conte_ate())
print(next(testando))
print(next(testando))


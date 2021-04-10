''' Para ler ou escrever dados do sistema operacional. o software que estaremos desenvolvendo necessitará de permissão

Aparentemente stringIO serve basicamente para gravar dados na memória ram do computador'''

from io import StringIO

texto = 'Testando um texto, o professor ão está explicando muito bem na minha opinião mas verei no que vai dar eu mesmo.'

arquivo = StringIO(texto)

print(arquivo)

print(arquivo)

print(arquivo.read())

print(arquivo.read())

# Então, o que está sendo feito é a criação de um arquivo salvo dentro de uma váriavel, daí pode ser feito todo o processo como demonstrado anteriormente
# Ou seja caso seja realizada a leitura do arquivo ela não poderá ser repetida por toda aquela história do cursor


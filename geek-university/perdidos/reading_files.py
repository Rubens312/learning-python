#A função open() realiza a abertura de um arquivo
#A forma mais simples de utilização é passar apenas um parametro de entrada que é o nome do caminho para o arquivo a ser lido.
#Essa função retorna um _io.TextIOWrapper que é um objeto 
#Por padrão essa função abre o arquivo para leitura. 

FiveOFive = open('exemplo.txt')

# help(fiveofive)

# print(FiveOFive)
# print(FiveOFive.read())

# A função read funciona com o principio do cursor
# De modo simplifiado a leitura só pode ser realizada uma unica vez
# Isso se dá porque a leitura é realizada desde o inicio até o final, ou seja, se a leitura é solicitada novamente você irá ler a partir do final, ou seja, não a conteúdo a frente para ser lido. 

ArcticMonkeys505 = FiveOFive.read()

print(ArcticMonkeys505)
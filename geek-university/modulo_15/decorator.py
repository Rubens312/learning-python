'''
Decorators são funções que alteram outras funções.
Ou seja
Funções que adicionam funcionalidades a outras funções
'''

def testando_decoretors(function):
    def interna():
        print('Aparentemente se eu escrever isso aqui...')
        function()
        print('...e colocar isso aqui, a função la em baixo vai aparecer no meio')
    return interna

@testando_decoretors
def funcao():
    print('Realmete apareci no meio')
# @testando_decoretors
# def outra():
#     print('Eu não devo aparecer')

funcao()
# outra()

# Então rubens do futuro que provavelmente nunca vai ver isso novamente
# O que acontece
# O @funcao_decoradora é uma fução que recebe outra fução como parametro
# e assim que chamada como decorador entende que a função que estiver abaixo dela é a função parametro
# Quando você chama a função parametro, ela vem decorada